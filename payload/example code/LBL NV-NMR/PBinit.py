from spinapi import *

def initPB():
	#Select Pulse Blaster Board
	pb_select_board(0)

	#Try to initialize the PulseBlaster
	if pb_init() != 0:
		print("Error initializing board: %s" % pb_get_error())
		input("Please press a key to continue.")
		exit(-1)

	# Configure the core clock
	pb_core_clock(500.0)
