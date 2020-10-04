# Write your code here :-)
import time
from pycubed import cubesat

# ------- MAIN LOOP -------
delay = 2
package_num = 0

while True:
  temp = cubesat.temperature
  x_accel, y_accel, z_accel = cubesat.acceleration
  x_mag, y_mag, z_mag = cubesat.magnetic
  x_gyro, y_gyro, z_gyro = cubesat.gyro
  vbatt = cubesat.battery_voltage
  ichrg = cubesat.charge_current
  vsys = cubesat.system_voltage
  isys = cubesat.current_draw
  data = [package_num,
          [x_accel, y_accel, z_accel],
          [x_mag, y_mag, z_mag],
          [x_gyro, y_gyro, z_gyro],
          vbatt, ichrg, vsys, isys]
  print(data)
  package_num += 1
  time.sleep(delay)
