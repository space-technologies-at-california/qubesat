from pycubed import cubesat
from digitalio import DigitalInOut, Direction
import adafruit_pca9685 as pca
import board
import time
import math
import busio

class Vector:

    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x / other, self.y / other, self.z / other)
        elif type(other) == Vector:
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            raise TypeError(f"{type(other)} not supported by vector division")

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y * other, self.z * other)
        elif type(other) == Vector:
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError(f"{type(other)} not supported by vector multiplication")

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x + other, self.y + other, self.z + other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f"{type(other)} not supported by vector addition")

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x - other, self.y - other, self.z - other)
        elif type(other) == Vector:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError(f"{type(other)} not supported by vector subtraction")

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dot(self, other):
        assert type(other) == Vector
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Magnetorquer:
    def __init__(self, resistance, max_current, magnetic_gain, current_model = None):
        """
        Resistance - ohms
        Max Current - min(max current that the board can supply, max rated contiuous current) in Amps
        Magnetic Gain - Am^2/A
        current_model - quadtratic model tuple (a0, a1, a2) that maps current to duty cycle
        """
        self.resistance = resistance
        self.max_current = max_current
        self.magnetic_gain = magnetic_gain
        self.current_model = current_model

    def current_to_duty_cycle(self, current):
        assert self.current_model is not None
        if current == 0:
            return 0
        else:
            duty_cycle = self.current_model[0] + self.current_model[1] * current + self.current_model[2] * (current ** 2)
            return min(max(duty_cycle, 0), 1)

class MagnetorquerInterface:
    """
    3-axis magnetoquer hardware interface
    """
    MAX_PWM = 0xffff #65535

    @staticmethod
    def get_current_from_dipole(dipole, profile):
        return dipole / profile.magnetic_gain

    @staticmethod
    def _map_current_to_duty_cycle(current, profile):
        """
        DEPRECATED - USE QUADRATIC MODEL FROM EXPERIMENTAL DATA INSTEAD
        Takes in the desired current (A) and converts it to a duty cycle
        """
        voltage = cubesat.system_voltage
        current = current if current < current_limit else current_limit
        max_current = voltage / resistance
        duty_cycle = int(min(current / max_current, 1.0) * MagnetorquerInterface.MAX_PWM)
        return duty_cycle

    @staticmethod
    def _set_magnetorquer_current(pos, neg, current, profile):
        # Currently using a quadratic curent model
        duty_cycle = int(profile.current_to_duty_cycle(abs(current)) * MagnetorquerInterface.MAX_PWM)
        if current > 0:
            pos.duty_cycle = duty_cycle
            neg.duty_cycle = 0
        else:
            pos.duty_cycle = 0
            neg.duty_cycle = duty_cycle

    @staticmethod
    def _set_magnetorquer_dipole(pos, neg, dipole, profile):
        # May use a quadratic dipole model
        pass

    @staticmethod
    def _set_magnetorquer(pos, neg, dipole, profile):
        current = MagnetorquerInterface.get_current_from_dipole(dipole, profile)
        # clip the current so it does not go beyond max_current
        current = min(abs(current), profile.max_current) * (dipole / abs(dipole))
        MagnetorquerInterface._set_magnetorquer_current(pos, neg, current, profile)

    def __init__(self, x_profile, y_profile, z_profile):
        self.pwm = pca.PCA9685(cubesat.i2c, address=0x40)
        self.pwm.frequency = 100

        # Setup pin the enables/disables magnetorquers
        self.mtrEnPin = board.PA17
        self.mtrEn = DigitalInOut(self.mtrEnPin)
        self.mtrEn.direction = Direction.OUTPUT
        self.disable()  # start disabled

        # Magnetorquer models and information
        self.x_profile = x_profile
        self.y_profile = y_profile
        self.z_profile = z_profile

        self.magXPos = self.pwm.channels[0]
        self.magXNeg = self.pwm.channels[1]

        self.magYPos = self.pwm.channels[2]
        self.magYNeg = self.pwm.channels[3]

        self.magZPos = self.pwm.channels[4]
        self.magZNeg = self.pwm.channels[5]

    def write(self, x_m, y_m, z_m):
        """
        Takes in target dipoles and writes them to the magnetorquers based on internal model
        """
        self._set_magnetorquer(self.magXPos, self.magXNeg, x_m, self.x_profile)
        self._set_magnetorquer(self.magYPos, self.magYNeg, y_m, self.y_profile)
        self._set_magnetorquer(self.magZPos, self.magZNeg, z_m, self.z_profile)

    def enable(self):
        self.mtrEn.value = True

    def disable(self):
        self.mtrEn.value = False

class DetumblingController:
    MAX_STATE_DATA_LEN = 64

    @staticmethod
    def _average_state_data(state_data):
        ang_vel_sum = Vector(0, 0, 0)
        mag_sum = Vector(0, 0, 0)
        for ang_vel, mag in state_data:
            ang_vel_sum += ang_vel
            mag_sum += mag
        return ang_vel_sum / len(state_data), mag_sum / len(state_data)

    """
    Detumble the satellite. This should be stepped at a rate of a 2 * (1 / step_time)
    """
    def __init__(self, hardware_interface, controller_gains, step_time=0.05):
        """
        Basic control loop:
        1. Disable magnetorquers (1)
        2. Read angular acceleration and magnetic field over step_time (1)
        3. Average values from both angular acceleration and magnetic field (2)
        4. Write desired current to magnetoquers based on readings from 2 (2)
        5. Enable magnetoquers (2)
        6. Wait for step_time (2)
        7. Repeat
        """
        self.k = controller_gains
        self.step_time = step_time
        self.control_vector = None
        self.interface = hardware_interface

        self.stage_start_time = time.monotonic()
        self.state_data = []

    def clear(self):
        self.control_vector = None
        self.state_data = []
        self.interface.disable()

    def step(self, angular_vecolcity, magnetic_field):
        """
        Expects angular velocity as a Vector with units rad/s and magnetic field as a Vector with units of Gauss
        """
        # time differece
        td = time.monotonic() - self.stage_start_time

        # If not data has been collected we must have just finished a cycle or are starting the detumbling
        if len(self.state_data) == 0:
            # Start stage
            self.stage_start_time = time.monotonic()
            self.state_data.append((angular_vecolcity, magnetic_field))
        elif td < self.step_time:
            # Collect state data
            if len(self.state_data) >= self.MAX_STATE_DATA_LEN:
                self.state_data.pop(0)
            self.state_data.append((angular_vecolcity, magnetic_field))
        elif td < 2 * self.step_time:
            # Execute control
            if self.control_vector is None:
                # Compute the control vector and write it to the
                angular_velocity, magnetic_field = self._average_state_data(self.state_data)
                b_dot = angular_velocity.cross(magnetic_field)
                # print(b_dot)
                # print(abs(magnetic_field))
                self.control_vector = self.k / abs(magnetic_field) * b_dot
                # print("Control vector", self.control_vector)

                # Compute a scale factor so we dont try to drive the magnetorquer current higher than it can go
                x_i = self.interface.get_current_from_dipole(self.control_vector.x, self.interface.x_profile)
                x_r = abs(self.interface.x_profile.max_current / x_i)
                y_i = self.interface.get_current_from_dipole(self.control_vector.y, self.interface.y_profile)
                y_r = abs(self.interface.y_profile.max_current / y_i)
                z_i = self.interface.get_current_from_dipole(self.control_vector.z, self.interface.z_profile)
                z_r = abs(self.interface.z_profile.max_current / z_i)
                scale_factor = min(x_r, y_r, z_r, 1)
                self.control_vector *= scale_factor

                # Send control to the hardware interface
                self.interface.write(self.control_vector.x, self.control_vector.y, self.control_vector.z)
                self.interface.enable()
        else:
            # Reset
            self.clear()


def record_model():
    # WARNING, this script will go to max duty cycle which may put a lot of current through the attached device
    hardware_interface = MagnetorquerInterface(Magnetorquer(0, 0, 0), Magnetorquer(0, 0, 0), Magnetorquer(0, 0, 0))

    hardware_interface.enable()

    # We are using motor 0 for all magnetorquer model id
    p = hardware_interface.magXPos
    n = hardware_interface.magXNeg

    print("Starting routine")
    iterations = 10
    for i in range(iterations):
        duty_cycle = int(hardware_interface.MAX_PWM * (i / (iterations - 1)))
        p.duty_cycle = duty_cycle
        n.duty_cycle = 0
        print(cubesat.system_voltage, ',', duty_cycle)
        time.sleep(3)
    hardware_interface.disable()
    print("Finished")

def test_model():
    X_PROFILE = Magnetorquer(30, 0.15, 2.8, current_model=(8.61e-3, 18, -28.7))
    hardware_interface = MagnetorquerInterface(X_PROFILE, Magnetorquer(0, 0, 0), Magnetorquer(0, 0, 0))

    hardware_interface.enable()

    # We are using motor 0 for all magnetorquer model id
    p = hardware_interface.magXPos
    n = hardware_interface.magXNeg

    print("Starting test")
    iterations = 10
    for i in range(iterations):
        current = X_PROFILE.max_current * (i / (iterations - 1))
        print("Target current:", current)
        hardware_interface._set_magnetorquer_current(p, n, current, X_PROFILE)
        time.sleep(3)
    hardware_interface.disable()
    print("Finished")

"""
Test examples
(To validate w/ these numbers @ the wires you need to commenout out the scale factor)

(1) <- potential recording problem here?
angular_velocity = Vector(0.1017, 0.0968, 0.1017)
magnetic_field = Vector(1.095e-5, 3.404e-6, 2.108e-5) * 1e4
---
desired_dipole = Vector(0.418, -0.180, -0.0744)
current = Vector(0.149, -0.064, -0.03545)

(2)
angular_velocity = Vector(0.001349, 0.0003236, -0.001617)
magnetic_field = Vector(4.289e-6, -4.045e-6, -2.3518e-5) * 1e4
---
desired_dipole = Vector(-0.00245, 0.00429, -0.000359)
current = Vector(-0.000875, 0.00153, -0.00017)

(3)
angular_velocity = Vector(0.001349, 0.0003236, -0.001617)
magnetic_field = Vector(1.30087197e-05, -4.19480928e-06,  1.97188537e-05) * 1e4
---
desired_dipole = Vector(0.387, -0.124, -0.08507)
current = Vector(0.138, -0.044, -0.041)
"""


def main():
    # https://www.cubespace.co.za/products/adcs-components/cubetorquer/
    X_PROFILE = Magnetorquer(30, 0.14, 2.8, current_model=(0.0472, 12.9, -44.1))
    Y_PROFILE = Magnetorquer(30, 0.14, 2.8, current_model=(0.0472, 12.9, -44.1))
    Z_PROFILE = Magnetorquer(81.5, 0.061, 2.1, current_model=(8.61e-3, 18, -28.7))
    hardware_interface = MagnetorquerInterface(X_PROFILE, Y_PROFILE, Z_PROFILE)
    controller = DetumblingController(hardware_interface, Vector(4.2, 4.2, 1.27), 0.05)

    print("Starting controller")
    while True:
        mag_x, mag_y, mag_z = cubesat.magnetic
        mag_vec = Vector(mag_x, mag_y, mag_z)
        gyro_x, gyro_y, gyro_z = cubesat.gyro
        gyro_vec = Vector(gyro_x, gyro_y, gyro_z) * math.pi / 180

        # Test Case (1)
        # gyro_vec = Vector(0.1017, 0.0968, 0.1017)
        # mag_vec = Vector(1.095e-5, 3.404e-6, 2.108e-5) * 1e4

        # Test Case (2)
        # gyro_vec = Vector(0.001349, 0.0003236, -0.001617)
        # mag_vec = Vector(4.289e-6, -4.045e-6, -2.3518e-5) * 1e4

        # Test Case (3)
        # gyro_vec = Vector(0.10537412, 0.08955995, 0.105369)
        # mag_vec = Vector(1.30087197e-05, -4.19480928e-06,  1.97188537e-05) * 1e4

        controller.step(gyro_vec, mag_vec)

main()
#record_model()
#test_model()
