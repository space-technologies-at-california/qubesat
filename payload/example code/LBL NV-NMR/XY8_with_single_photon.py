import PBcontrol as PBctl
import sequenceControl as seqCtl
import XY8config as XY8
from spinapi import *
from ctypes import *
import numpy as np
import sys
import single_photon as DAQ #NOTE THIS CHANGE FROM PHOTODIODE CODE
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
	config['t_readoutDelay'] = 2.3*us
	config['t_pi'] = 24
	config['sequence_name'] = "XY8seq"

	#Defines the frequency that the SRS will sweep (in GHz)
	config['start_tau'] = 300
	config['end_tau'] = 480
	config['step_tau'] = 20

	config['MW_FREQ'] = 2e9
	config['DAQtimeout'] - 120
	config['Navg'] = 1
	config['N'] = 12

	runExperiment()

def run(config_dic):
	global config
	config = config_dic
	runExperiment()

def runExperiment():
	try:
		config['IQpadding'] = XY8.t_min*round(30*ns/T2.t_min)

		#Plotting setup, xs is the frequencies, ys is the average intensities 
		style.use("fivethirtyeight")
		plt.ion()
		fig = plt.figure()
		ax = fig.add_subplot(111)
		xs = []
		ys = [] 
		bys = []
		line1, = ax.plot(xs, ys, 'b-')

		initPB()
		
		#initiate RF generator with channel and model type; set amplitude
		my_SRS = SRSctl.initSRS(27, 'SG386') 
		SRSctl.setSRS_RFAmplitude(my_SRS, .14, units = "Vpp") 

		#set test frequency and modulation
		SRSctl.setSRS_Freq(my_SRS, config['MW_FREQ'], 'GHz') 
		SRSctl.setupSRSmodulation(my_SRS, 'XY8seq') 

		instructionArray = []
		for i in np.arange(config['start_tau'], config['end_tau'] + config['step_tau'], config['step_tau']):
			sequenceArgs = [i*ns, config['t_AOM'] * ns, config['t_readoutDelay'] * ns, config['t_pi'] * ns, config['IQpadding'], config['N']]
			instructionArray.extend(PBctl.programPB(config['sequence_name'], sequenceArgs))
		print(instructionArray)

		status = pb_start_programming(PULSE_PROGRAM)
		for i in range(0, len(instructionArray)):
			PBctl.pb_inst_pbonly(instructionArray[i][0],instructionArray[i][1],instructionArray[i][2],instructionArray[i][3])
		pb_stop_programming()

		#Configure the DAQ
		config['task'], channel = DAQ.configureDAQ(ESR.Nsamples)

		#turn on the microwave excitation - changed the sequence here, zhao, 02/24/2020
		SRSctl.enableSRS_RFOutput(my_SRS)

		#Function to close all running tasks
		def closeExp():
			#turn off the microwave excitation
			SRSctl.disableSRS_RFOutput(my_SRS) 
			#stop the pulse blaster
			pb_stop()
			#Close the DAQ once we are done
			DAQ.closeDAQTask(config['task'])
			return

		#Function to save data 
		def save():
			saved = input("Save plot? y/n")
			if saved == 'y':
				name = input("Enter a filename:")
				plt.savefig(name)
				np.savetxt(name + '.csv', (xs, ys), delimiter=",")
				#task.close()
				sys.exit()
			elif saved == 'n':
				#task.close()
				sys.exit()
			else:
				print('Error, try again')
				save()

		#start the pulse blaster
		pb_start()

		#Throw away the first NThrow samples to get the photodiode warmed up
		for i in range(NThrow):
			DAQ.readDAQ(config['task'], channel, ESR.Nsamples * 2, 10)

		for n in np.arange(config['Navg']):
			#For loop to run the experiment and plot
			for f in np.arange(config['start_tau'], config['end_tau'] + config['step_tau'], config['step_tau']):
			    #Read from the DAQ
			    output = DAQ.readDAQ(config['task'], channel, ESR.Nsamples * 2, config['DAQtimeout'])
			    #Average all the samples that we got
			    signal = output[0::2]
			    background = output[1::2]
			    sig_average = np.mean(signal)
			    back_average = np.mean(background)
			    print('signal', sig_average)
			    print('background', back_average)
			    #append frequency to x-axis
			    xs.append(f)

			    #append counts to y-axis
			    ys.append(sig_average - back_average)

			    #clear the plot
			    plt.clf()

			    #Plot the variables
			    plt.plot(xs, ys)

			    #Make the plot look good
			    plt.xticks(rotation=45, ha='right')
			    plt.subplots_adjust(bottom=0.30)
			    plt.title('Photo Counter Readout vs Pulse Duration')
			    plt.ylabel('Photodiode Voltage (V)')
			    plt.xlabel('Pulse Duration (ns)')

			    #Draw the plot, pause is necessary to get it to show up
			    plt.draw()
			    plt.pause(0.0001)
	except KeyboardInterrupt:
		print('User keyboard interrupt. Quitting...')
		sys.exit()
	finally:
		#Idk if show is necessary, save the plot and close everything	
		plt.show()
		closeExp()
		save()