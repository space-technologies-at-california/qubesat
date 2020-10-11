from pycubed import cubesat
from enum import Enum
import time

class States(Enum):
	DEPLOY = 0
	NORMAL = 1
	LOW_POWER = 2

while(!check_deployed()): 
	mode = 'deploy_mode'
	deploy()
while True:
	switch(mode):
		case DEPLOY:

		case NORMAL:
			get_payload_data()
			process_data()
			send_for_comms()
		case LOW_POWER:
			# openLST during low_power mode, check in with comms
			# low power mode in payload (how to reduce the power from their end?)
			# change time for interrupt (greater time differences to reduce power)
			# when to enter low power? When we are in the Earth's shadow?
			# check the battery voltage, current from the solar panels



#include interrupt_vectorA1
def timer_interrupt_handler():
	mode = get_power_status()
	if mode != current_mode:
		change_mode(mode)
	command = get_command()
	if command:
		handle_command(command)
	get_IMU()

# Useful feature if possible:
#	- interrupts
#		- timer interrupt to get telemetry
#		- interrupt for incomming command
#		- interrupt for incoming data

def deploy():
	wait(20)
	deploy_antenna()
	detumble()

def check_deployed():
	pass

def deploy_antenna():
	pass

def get_IMU():
	x_accel, y_accel, z_accel = cubesat.acceleration
    x_mag, y_mag, z_mag = cubesat.magnetic
    x_gyro, y_gyro, z_gyro = cubesat.gyro
	data = [[x_accel, y_accel, z_accel],
            [x_mag, y_mag, z_mag],
            [x_gyro, y_gyro, z_gyro]]
	return data

def get_command():
	pass

def handle_command(command):
	pass

def get_power_status():
	# there are three modes: deploy_mode, normal, low_power
	# deploy_mode -> no power during the first hour or so after deployment
	# normal_mode -> everything is allowed
	# low_power -> receiving commands only
	threshold_voltage = 3 # TBR
	vbatt = cubesat.battery_voltage
	if vbatt < threshold_voltage:
		status = 'low_power'
	else:
		status = 'normal_mode'
	return status

def change_mode(mode):
	if mode == 'low_power':
		# cut power on something
	status = mode

def get_payload_data():
	pass

def process_data():
	pass

def send_for_comms(): # send IMU data via UART to the comms board
	pass
