from pycubed import cubesat
import time

delay = 1

while True:

    # Read acceleration, magnetometer, gyroscope, temperature.
    temp = cubesat.temperature
    accel_x, accel_y, accel_z = cubesat.acceleration
    mag_x, mag_y, mag_z       = cubesat.magnetic
    gyro_x, gyro_y, gyro_z    = cubesat.gyro

    # Print values.
    print('Temperature: {}C'.format(temp))
    print('Acc  (m/s^2):   x: {}\ty: {}\tz: {}'.format(accel_x, accel_y, accel_z))
    print('Mag  (gauss):   x: {}\ty: {}\tz: {}'.format(mag_x, mag_y, mag_z))
    print('Gyro (deg/sec): x: {}\ty: {}\tz: {}'.format(gyro_x, gyro_y, gyro_z))
    print('')

    # Delay for a second.
    time.sleep(delay)