import PBcontrol as PBctl
import sequenceControl as seqCtl
import ESRconfig as ESR
from spinapi import *
from ctypes import *
import numpy as np
import sys
import DAQcontrol as DAQ
import SRScontrol as SRSctl
from PBinit import initPB

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


#Define number of measurements to throw away before starting experiment 
NThrow = 10

def main():
	'''For running experiment normally'''
	global config
	config = {}
	#Constants for PulseBlaster
	config['t_AOM'] = 50000 * ns
	config['sequence_name'] = "ESRseq"

	#Defines the frequency that the SRS will sweep (in GHz)
	config['START_FREQUENCY'] = 2.5
	config['END_FREQUENCY'] = 3.5
	config['STEP_FREQUENCY'] = 0.2

	runExperiment()

def run(config_dic):
	global config
	config = config_dic
	runExperiment()

def runExperiment():
	global my_SRS

	#Plotting setup, xs is the frequencies, ys is the average intensities for the signal, bys is avg intensities for background
	style.use("fivethirtyeight")
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	xs = []
	ys = [] 
	bys = []

	initPB()
	
	#initiate RF generator with channel and model type; set amplitude
	my_SRS = SRSctl.initSRS(27, 'SG386')
	SRSctl.setSRS_RFAmplitude(my_SRS, .14, units = "Vpp") 

	#set test frequency and modulation
	SRSctl.setSRS_Freq(my_SRS, config['START_FREQUENCY'], 'GHz') 
	SRSctl.setupSRSmodulation(my_SRS, config['sequence_name']) 

	#Get the instruction Array
	instructionArray = PBctl.programPB(config['sequence_name'], [config['t_AOM']])
	print(instructionArray)

	#Program the PulseBlaster
	status = pb_start_programming(PULSE_PROGRAM)
	for i in range(0, len(instructionArray)):
		PBctl.pb_inst_pbonly(instructionArray[i][0],instructionArray[i][1],instructionArray[i][2],instructionArray[i][3])
	pb_stop_programming()

	#Configure the DAQ
	global task
	task = DAQ.configureDAQ(ESR.Nsamples)

	#turn on the microwave excitation - changed the sequence here, zhao, 02/24/2020
	SRSctl.enableSRS_RFOutput(my_SRS) 

	global f
	#Set f to be the start frequency
	f = config['START_FREQUENCY']

	#start the pulse blaster  # you can start pulseblaster at the beginning the experiment and turn it off until everything is done -- Zhao, 6/11/2020
	pb_start()

	#Throw away the first NThrow samples to get the photodiode warmed up
	for i in range(NThrow):
		DAQ.readDAQ(task, ESR.Nsamples * 2, 10)

	#Begin the animation - All of the experiment work is done in the animate function. FuncAnimation runs animate in a loop automatically
	ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, bys), interval = 200)   ## not sure if this is the best approach. maybe try to use the "frames" variable for this function -- Zhao, 6/11/2020
	

#This is the function that runs the experiment and does the plotting
def animate(i, xs, ys, bys):
	global f, my_SRS, task
	#If f goes past end frequency, we are done
	if f > config['END_FREQUENCY']:
		conclude()
	else:
		#init RF generator with new frequency
		SRSctl.setSRS_Freq(my_SRS, f, 'GHz')  
		
		#Read from the DAQ
		output = DAQ.readDAQ(task, ESR.Nsamples * 2, 10)        ### please check this - Does this read out with external trigger? -- Zhao, 6/11/2020

		#Average all the samples that we got
		signal = output[0::2]
		background = output[1::2]
		sig_average = np.mean(signal)
		back_average = np.mean(background)
		print('signal', sig_average)
		print('background', back_average)

		#Increment the frequency for the next round
		f += STEP_FREQUENCY

		#Bunch of plotting code
		xs.append(f)
		ys.append(sig_average)
		bys.append(back_average)
		ax1.clear()
		ax1.plot(xs, ys, 'r-', xs, bys, 'b-') # Plots xs, ys, bys 
		plt.xticks(rotation=45, ha='right')
		plt.subplots_adjust(bottom=0.30)
		plt.title('Photodiode Readout vs Frequency')
		plt.ylabel('Photodiode Voltage (V)')
		plt.xlabel('Frequency (GHz)')

def conclude():
	global my_SRS, task
	save = input("Save plot and data? y/n")
	if save == 'y':
		name = input("Enter a filename:")
		plt.savefig(name)
		np.savetxt(name + '.csv', (xs, ys, bys), delimiter=",")
		task.close()
		#turn off the microwave excitation
		SRSctl.disableSRS_RFOutput(my_SRS)   
	elif save == 'n':
		task.close()
		SRSctl.disableSRS_RFOutput(my_SRS)
	else:
		print('Error, try again')
		return

	plt.show()

	#stop the pulse blaster
	pb_stop()

	#Close the DAQ once we are done
	DAQ.closeDAQtask(task)

	sys.exit()

if __name__ == "__main__":
    main()