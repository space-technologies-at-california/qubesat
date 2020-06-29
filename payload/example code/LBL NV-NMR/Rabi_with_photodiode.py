import PBcontrol as PBctl
import sequenceControl as seqCtl
import Rabiconfig as RABI
from spinapi import *
from ctypes import *
import numpy as np
import sys
import DAQcontrol as DAQ
import SRScontrol as SRSctl
import time

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#Plotting setup, xs is the frequencies, ys is the average intensities 
style.use("fivethirtyeight")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = [] 
bys = []

#Define number of measurements to throw away before starting experiment 
NThrow = 10

#Select Pulse Blaster Board
pb_select_board(0)

#Constants for PulseBlaster
MW_FREQ = 2.5
t_AOM = 30000 * ns
t_readoutDelay = 40000 * ns
sequence_name = "RabiSeq"

#Defines lengths of time that uw will sweep (nanoseconds is assumed and added in during loop)
START_LENGTH= 1000 
END_LENGTH = 30000
STEP_LENGTH = 1000
sequenceArgs = [START_LENGTH * ns, t_AOM, t_readoutDelay]

#initiate RF generator with channel and model type; set amplitude
#my_SRS = SRSctl.initSRS(27, 'SG386') UNCOMMENT THIS!
#SRSctl.setSRS_RFAmplitude(my_SRS, .14, units = "Vpp") UNCOMMENT THIS!

#set test frequency and modulation
#SRSctl.setSRS_Freq(my_SRS, MW_FREQ, 'GHz') UNCOMMENT THIS!
#SRSctl.setupSRSmodulation(my_SRS, 'RabiSeq') UNCOMMENT THIS!

#Try to initialize the PulseBlaster
if pb_init() != 0:
	print("Error initializing board: %s" % pb_get_error())
	input("Please press a key to continue.")
	exit(-1)

# Configure the core clock
pb_core_clock(500.0)

#Get the first instruction Array
instructionArray = PBctl.programPB(sequence_name, sequenceArgs)
print(instructionArray)

#Program the PulseBlaster
status = pb_start_programming(PULSE_PROGRAM)
for i in range(0, len(instructionArray)):
	PBctl.pb_inst_pbonly(instructionArray[i][0],instructionArray[i][1],instructionArray[i][2],instructionArray[i][3])
pb_stop_programming()

#Configure the DAQ
task = DAQ.configureDAQ(RABI.Nsamples)

#turn on the microwave excitation - changed the sequence here, zhao, 02/24/2020
#SRSctl.enableSRS_RFOutput(my_SRS) UNCOMMENT THIS! 

#Set t to be the start time and initalize the average variable to 0
t = START_LENGTH
average = 0

#Throw away the first NThrow samples to get the photodiode warmed up
for i in range(NThrow):
	pb_start()
	DAQ.readDAQ(task, RABI.Nsamples * 2, 10)
	pb_stop()

#This is the function that runs the experiment and does the plotting
def animate(i, xs, ys, bys):
	#Defines f as a global variable so we can update between function calls
	global t
	#If f goes past end frequency, we are done
	if t > END_LENGTH:
		closeExp()
		save = input("Save plot? y/n")
		if save == 'y':
			name = input("Enter a filename:")
			plt.savefig(name)
			task.close()
			sys.exit()
		elif save == 'n':
			task.close()
			sys.exit()
		else:
			print('Error, try again')
			return
	else:
		#Get the next instruction Array
		sequenceArgs = [t * ns, t_AOM, t_readoutDelay]
		instructionArray = PBctl.programPB(sequence_name, sequenceArgs)

		#Program the PulseBlaster
		status = pb_start_programming(PULSE_PROGRAM)
		for i in range(0, len(instructionArray)):
			PBctl.pb_inst_pbonly(instructionArray[i][0],instructionArray[i][1],instructionArray[i][2],instructionArray[i][3])
		pb_stop_programming()

		#start the pulse blaster
		pb_start()
		#Read from the DAQ
		output = DAQ.readDAQ(task, RABI.Nsamples * 2, 10)
		#Average all the samples that we got
		signal = output[0::2]
		background = output[1::2]
		sig_average = np.mean(signal)
		back_average = np.mean(background)
		#back_average = 1
		print('signal', sig_average)
		print('background', back_average)
		#stop the pulse blaster
		pb_stop()
		#Increment the frequency for the next round
		t += STEP_LENGTH
		#Bunch of plotting code
		xs.append(t)
		ys.append(sig_average)
		bys.append(back_average)
		ax1.clear()
		ax1.plot(xs, ys, 'r-', xs, bys, 'b-')
		plt.xticks(rotation=45, ha='right')
		plt.subplots_adjust(bottom=0.30)
		plt.title('Photodiode Readout vs MW Pulse Duration')
		plt.ylabel('Photodiode Voltage (V)')
		plt.xlabel('MW Pulse Duration (ns)')

#Begin the animation - All of the experiment work is done in the animate function
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, bys), interval = 200)
plt.show()


def closeExp():
	#turn off the microwave excitation
	SRSctl.disableSRS_RFOutput(my_SRS) 
	#stop the pulse blaster
	pb_stop()
	#Close the DAQ once we are done
	DAQ.closeDAQTask(task)
	return
