from pycubed import cubesat
import time

while(!check_deployed()):
	deploy()
while True:
	get_payload_data()
	process_data()
	send_for_comms()


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
	wait(20 minutes)
	deploy_antenna()
	detumble()

def get_IMU():
	pass

def get_command():
	pass

def handle_command(command):
	pass

def get_power_status():
	pass

def change_mode(mode):
	pass

def get_gyro_data():
	pass

def process_data():
	pass

def send_for_comms():
	pass 



