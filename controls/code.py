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
    def __init__(self, resistance, max_continuous_current, magnetic_gain):
        """
        Resistance - ohms
        Max Continuous Current - Amps
        Magnetic Gain - Am^2/A
        """
        self.resistance = resistance
        self.max_continuous_current = max_continuous_current
        self.magnetic_gain = magnetic_gain

class MagnetorquerInterface:
    """
    3-axis magnetoquer hardware interface
    """
    BOARD_VOLTAGE = 5
    MAX_PWM = 0xffff

    @staticmethod
    def _map_duty_cycle(current, resistance, current_limit=0.15):
        """
        Takes in the desired current (A) and converts it to a duty cycle
        """
        current = current if current < current_limit else current_limit
        max_current = MagnetorquerInterface.BOARD_VOLTAGE / resistance
        duty_cycle = int(min(current / max_current, 1.0) * MagnetorquerInterface.MAX_PWM)
        return duty_cycle

    @staticmethod
    def _set_magnetorquer(pos, neg, dipole, profile):
        duty_cycle = MagnetorquerInterface._map_duty_cycle(abs(dipole) / profile.magnetic_gain, profile.resistance, profile.max_continuous_current)
        if dipole > 0:
            pos.duty_cycle = duty_cycle
            neg.duty_cycle = 0
        else:
            pos.duty_cycle = 0
            neg.duty_cycle = duty_cycle

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
    def __init__(self, x_profile, y_profile, z_profile, controller_gains, step_time=0.05):
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
        self.interface = MagnetorquerInterface(x_profile, y_profile, z_profile)

        self.stage_start_time = time.time()
        self.state_data = []

    def step(self, angular_vecolcity, magnetic_field):
        """
        Expects angular velocity as a Vector with units rad/s and magnetic field as a Vector with units of Gauss
        """
        # time differece
        td = time.time() - self.stage_start_time

        # If not data has been collected we must have just finished a cycle or are starting the detumbling
        if len(self.state_data) == 0:
            # Start stage
            self.stage_start_time = time.time()
            self.state_data.append((angular_vecolcity, magnetic_field))
        elif td < self.step_time:
            # Collect state data
            self.state_data.append((angular_vecolcity, magnetic_field))
        elif td < 2 * self.step_time:
            # Execute control
            if self.control_vector is None:
                # Compute the control vector and write it to the
                angular_velocity, magnetic_field = self._average_state_data(self.state_data)
                b_dot = angular_velocity.cross(magnetic_field)
                self.control_vector = self.k / (magnetic_field / abs(magnetic_field)) * b_dot
                self.interface.write(self.control_vector.x, self.control_vector.y, self.control_vector.z)
                self.interface.enable()
        else:
            # Reset
            self.control_vector = None
            self.state_data = []
            self.interface.disable()



def main():
    # https://www.cubespace.co.za/products/adcs-components/cubetorquer/
    X_PROFILE = Magnetorquer(30, 0.15, 2.8)
    Y_PROFILE = Magnetorquer(30, 0.15, 2.8)
    Z_PROFILE = Magnetorquer(81.5, 0.15, 2.1)
    controller = DetumblingController(X_PROFILE, Y_PROFILE, Z_PROFILE, Vector(4.2e-4, 4.2e-4, 1.27e-4), 1)

    while True:
        mag_x, mag_y, mag_z = cubesat.magnetic
        mag_vec = Vector(mag_x, mag_y, mag_z)
        gyro_x, gyro_y, gyro_z = cubesat.gyro
        gyro_vec = Vector(gyro_x, gyro_y, gyro_z) * math.pi / 180
        controller.step(gyro_vec, mag_vec)
        time.sleep(0.1)

main()
