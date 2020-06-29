# mainControl.py
# Copyright 2018 Diana Prado Lopes Aude Craik

# Permission is hereby granted, free of charge, to any person 
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#Imports
import connectionConfig as conCfg
import sequenceControl as seqCtl
import SRScontrol as SRSctl
import DAQcontrol as DAQctl
import PBcontrol as PBctl
import matplotlib.pyplot as plt
import numpy as np
from spinapi import ms,us,ns
from random import shuffle
from os.path import isdir 
from os import makedirs
import sys
import math
from importlib import import_module

# Define t_min, time resolution of the PulseBlaster, given by 1/(clock frequency):
t_min = 1e3/conCfg.PBclk #in ns
def validateUserInput(expCfg):
# This function validates the user inputs in the experiment config file (e.g. ESRconfig, Rabiconfig, etc).
	
	# Check that N_scanPts, Nsamples, Navg are all integers and Nsamples>=1, Navg>= 1, N_scanPts>=2
	if (not isinstance(expCfg.Nsamples, int)) or (expCfg.Nsamples<1):
		print('Error: Nsamples must be an integer >= 1.')
		sys.exit()
	if (not isinstance(expCfg.Navg, int)) or (expCfg.Navg<1):
		print('Error: Navg must be an integer >= 1.')
		sys.exit()
	if (not isinstance(expCfg.N_scanPts, int)) or (expCfg.N_scanPts<2):
		print('Error: N_scanPts must be an integer >= 2.')
		sys.exit()
	
	#Pulse-sequence parameter checks:
	#Check that IQpadding is a multiple of t_min and >5*t_min:
	if expCfg.sequence in ['T2seq','XY8seq','correlSpecSeq']:
		if (expCfg.IQpadding<(5*t_min)) or (expCfg.IQpadding%t_min):
			print('Error: IQpadding is set to', expCfg.IQpadding,'which is either <',5*t_min,'or not a multiple of',t_min,'. Please edit IQpadding to ensure that it is >',5*t_min,'ns and a multiple of',t_min,'.')
	#Check t_duration in ESRseq is a multiple of (2*t_min):
	if expCfg.sequence == 'ESRseq':
		if expCfg.t_duration%(2*t_min):
			print('Warning: t_duration set to ', expCfg.t_duration,'ns, which is not an integer multiple of ',(2*t_min),'ns. Rounding t_duration to nearest multiple of ',(2*t_min),'ns...')
			expCfg.t_duration = (2*t_min)*round(t_duration_ns/(2*t_min))
			print('t_duration now set to ', expCfg.t_duration,'ns')
	
	#Check that t_readoutDelay and t_AOM are multiples of t_min: 
	if expCfg.sequence in ['RabiSeq','T2seq','XY8seq', 'correlSpecSeq', 'T1seq']:
		if expCfg.t_readoutDelay%t_min:
			print('Error: t_readoutDelay is set to ', expCfg.t_readoutDelay,'ns, which is not a multiple of ',t_min,'ns. Please set t_readoutDelay to an integer multiple of ',t_min,'ns.')
			sys.exit()
		if expCfg.t_AOM%t_min:
			print('Error: t_AOM is set to ', expCfg.t_AOM,'ns, which is not a multiple of ',t_min,'ns. Please set t_AOM to an integer multiple of ',t_min,'ns.')
			sys.exit()
		#Check that t_readoutDelay and t_AOM are >5*t_min:
		if expCfg.t_AOM<(5*t_min):
			print('Error: t_AOM must be >',(5*t_min),'ns!')
			sys.exit()
		if expCfg.t_readoutDelay<(5*t_min):
			print('Error: t_readoutDelay must be >',(5*t_min),'ns!')
			sys.exit()
	#Check that tau0 in the correlation spectroscopy sequence is an integer multiple of 2*t_min:
	if expCfg.sequence == 'correlSpecSeq':
		if expCfg.tau0%(2*t_min):
			print('Error: tau0 is set to ', expCfg.tau0,'ns, which is not a multiple of ',(2*t_min),'ns. Please set tau0 to an integer multiple of ',(2*t_min),'ns.')
			sys.exit()
	#Number of XY8 repeats check:
	if expCfg.sequence in ['XY8seq', 'correlSpecSeq']:
		if expCfg.N<1 or (not isinstance(expCfg.N, int)):
			print('Error: number of XY8 repeats, N, must be an integer >=1.')
			sys.exit()
	
	#Pi-pulse length checks:
	if expCfg.sequence == 'T1seq':
		if expCfg.t_pi<t_min or expCfg.t_pi%t_min:
			print('Error: requested pi pulse length ',expCfg.t_pi,'ns is either <',t_min,'ns or not an integer multiple of ',t_min,'ns.')
			sys.exit()
	if expCfg.sequence in ['T2seq','XY8seq','correlSpecSeq']:
		# Check if the user has input a pi-pulse length which is shorter than (2*t_min) or not a multiple of 2*t_min:
		if expCfg.t_pi<(2*t_min):
			print('Error: requested pi pulse length=',expCfg.t_pi,'ns is <',(2*t_min),'ns. t_pi must be set to at least',(2*t_min),'ns.')
			sys.exit()
		if expCfg.t_pi%(2*t_min):
			print('Warning: t_pi set to ', expCfg.t_pi,'ns, which is not an integer multiple of ',(2*t_min),'ns. Rounding t_pi to nearest multiple of ',(2*t_min),'ns...')
			expCfg.t_pi = (2*t_min)*round(float(expCfg.t_pi)/(2*t_min))
			print('t_pi now set to ', expCfg.t_pi,'ns')
			
	# Scan step-size checks:
	stepSize = expCfg.scannedParam[1]-expCfg.scannedParam[0]
	if (expCfg.sequence == 'ESRseq'):
		#If requested frequency stepsize is smaller than the SRS frequency resolution (1uHz), round step to 1uHz:
		if ((stepSize*1e6)%1):
			roundedFreqStepSize = (1e-6)*round((1e6)*stepSize)
			expCfg.scannedParam[-1] = (expCfg.N_scanPts-1)*roundedFreqStepSize + expCfg.scannedParam[0] 
			print('Warning: Requested frequency step is ',stepSize,'Hz, which is not an integer multiple of the SRS frequency resolution, 1uHz. Rounding step size to the nearest multiple of 1uHz.\nStep size is now',roundedFreqStepSize,'\n',expCfg.scanStartName,'= ',expCfg.scannedParam[0],' and \n',expCfg.scanEndName,'= ',expCfg.scannedParam[-1])
			expCfg.scannedParam = np.linspace(expCfg.scannedParam[0],expCfg.scannedParam[-1], expCfg.N_scanPts,endpoint= True)
	if (expCfg.sequence in ['RabiSeq', 'T1seq']) or (expCfg.sequence == 'T2seq' and expCfg.numberOfPiPulses==1):
		if stepSize<t_min:
			print('Error: requested time step is ',stepSize,'ns, which is shorter than ',t_min,'ns. Please change N_scanPts, or ',expCfg.scanStartName,' and ',expCfg.scanEndName,' to increase time step size.')
			sys.exit()
		# If requested step size is >t_min but not a multiple of t_min:
		if (stepSize%t_min):
			roundedStepSize = t_min*round(stepSize/t_min)
			expCfg.scannedParam[-1] = (expCfg.N_scanPts-1)*roundedStepSize + expCfg.scannedParam[0] 
			print('Warning: requested time step is ',stepSize,'ns, which is not an integer multiple of ',t_min,'ns. Rounding step size to the nearest multiple of ',t_min,':\nStep size is now',roundedStepSize,'\n',expCfg.scanStartName,'= ',expCfg.scannedParam[0],' and \n',expCfg.scanEndName,'= ',expCfg.scannedParam[-1])
			expCfg.scannedParam = np.linspace(expCfg.scannedParam[0],expCfg.scannedParam[-1], expCfg.N_scanPts,endpoint= True)
			
	if expCfg.sequence =='RabiSeq':
		# Pulseblaster bug - our PulseBlaster boards do not seem to be able to output 8ns pulses. So, check if we asked for 8ns and remove this point:
		if 8 in expCfg.scannedParam:
			expCfg.scannedParam = list(expCfg.scannedParam)
			expCfg.scannedParam.remove(8)				
			expCfg.N_scanPts = len(expCfg.scannedParam)
			print('Warning: will not collect data at 8ns scan point due to unofficial reports of a possible issue with some PB boards whereby the instruction for outputting 8ns pulses generates 10ns pulses. Removing the 8ns scan point from the list of scan points.')	
	
	if (expCfg.sequence == 'XY8seq') or (expCfg.sequence=='T2seq' and expCfg.numberOfPiPulses > 1):
		#Check if requested scan step is too short or not a multiple of 2*t_min:
		if stepSize<(2*t_min):
			print('Error: requested time step is ',stepSize,'ns, which is shorter than ', (2*t_min),'ns. Please change N_scanPts, or ',expCfg.scanStartName,' and ',expCfg.scanEndName,' to increase time step size.')
			sys.exit()
		# If requested step size is >2*t_min but not a multiple of t_min, round to nearest multiple of (2*t_min) and warn user:
		if (stepSize%(2*t_min)):
			roundedStepSize = (2*t_min)*round(stepSize/(2*t_min))
			expCfg.scannedParam[-1] =  (expCfg.N_scanPts-1)*roundedStepSize + expCfg.scannedParam[0] 
			print('Warning: requested time step is ',stepSize,'ns, which is not an integer multiple of ',(2*t_min),'ns. Rounding step size to the nearest multiple of ',(2*t_min),':\n Step size is now ',roundedStepSize,'\n ',expCfg.scanStartName,'= ',expCfg.scannedParam[0],' and \n',expCfg.scanEndName,'= ',expCfg.scannedParam[-1])
			expCfg.scannedParam = np.linspace(expCfg.scannedParam[0],expCfg.scannedParam[-1], expCfg.N_scanPts,endpoint= True)
	
	# Scan-start (minimum delay duration) checks:
	if (expCfg.sequence in ['RabiSeq', 'correlSpecSeq']) or (expCfg.sequence == 'T2seq' and expCfg.numberOfPiPulses==1):
	# Check if requested start delay/pulse length is positive and a multiple of t_min:
		if expCfg.scannedParam[0]<0:
			print('Error: requested ',expCfg.scanStartName,' = ',expCfg.scannedParam[0],'is <0. ',expCfg.scanStartName,' must be >=0.')
			sys.exit()
		if expCfg.scannedParam[0]%t_min:
			print('Error: ',expCfg.scanStartName,' is set to ', expCfg.scannedParam[0],', which is not a multiple of ',t_min,'ns. Please set', expCfg.scanStartName,' to an integer multiple of ',t_min,'ns.')
			sys.exit()
	
	if (expCfg.sequence == 'XY8seq') or (expCfg.sequence=='T2seq' and expCfg.numberOfPiPulses > 1):
	# Check if requested start delay/pulse length is a multiple of 2*t_min:
		if expCfg.scannedParam[0]%(2*t_min):
			print('Error: ',expCfg.scanStartName,' is set to ', expCfg.scannedParam[0],', which is not a multiple of ',(2*t_min),'ns. Please set', expCfg.scanStartName,' to an integer multiple of ',(2*t_min),'ns.')
			sys.exit()
		
	if expCfg.sequence == 'T1seq':
		if expCfg.scannedParam[0]<(expCfg.t_readoutDelay + t_min*round((1*us)/t_min)):
			print('Error: requested ',expCfg.scanStartName,' is too short.', expCfg.scanStartName,' must be >=0.')
			sys.exit()
		if expCfg.scannedParam[0]%t_min:
			print('Error: ',expCfg.scanStartName,' is set to ', expCfg.scannedParam[0],', which is not a multiple of ',t_min,'ns. Please set', expCfg.scanStartName,' to an integer multiple of',t_min,'ns.')
			sys.exit()
	
	if expCfg.sequence in ['T2seq','XY8seq']:
		# Check if requested start delay is shorter than 3*(5*t_min):
		if expCfg.scannedParam[0]<3*(5*t_min):
			print('Error: requested ',expCfg.scanStartName,' of ',expCfg.scannedParam[0],'ns is too short. For this pulse sequence, ',expCfg.scanStartName,' must be set to at least',3*(5*t_min),'ns')
			sys.exit()
	
	if expCfg.sequence == 'T2seq':
		if (not isinstance(expCfg.numberOfPiPulses, int)) or (expCfg.numberOfPiPulses<1):
			print('Error: numberOfPiPulses must be a positive integer!')
			sys.exit()
		if expCfg.numberOfPiPulses == 1:
			if expCfg.scannedParam[0]<(2*expCfg.IQpadding + (3/4)*expCfg.t_pi + (5*t_min)):
				# Check if start delay is too short to allow for PB timing resolution:
				print('Error: ',expCfg.scanStartName,' too short. For your pi_pulse length, ',expCfg.scanStartName,' must be at least', (2*expCfg.IQpadding + (3/4)*expCfg.t_pi + (5*t_min)),'ns.')
				sys.exit()
		else: #number of pi pulses>1
			if expCfg.scannedParam[0]<(2*(2*expCfg.IQpadding + (3/4)*expCfg.t_pi + (5*t_min))):
				print('Error: ',expCfg.scanStartName,' too short. For your pi_pulse length, ',expCfg.scanStartName,' must be at least', (2*(2*expCfg.IQpadding + (3/4)*expCfg.t_pi + (5*t_min))),'ns.')
				sys.exit()
				
	if expCfg.sequence == 'XY8seq':
		if expCfg.scannedParam[0]<(2*(2*expCfg.IQpadding + (3/4)*expCfg.t_pi + (5*t_min))):
			print('Error: ',expCfg.scanStartName,' too short. For your pi_pulse length, ',expCfg.scanStartName,' must be at least', (2*(2*expCfg.IQpadding + (3/4)*expCfg.t_pi + (5*t_min))),'ns.')
			sys.exit()
		
	# Free precession time checks. The spacing between the rising edge of a pi or pi/2 pulse and the rising edge of the subsequent pi
	# or pi/2 pulse in the T2, XY8 and correlation spectroscopy sequences has to be an integer multiple of t_min. The user-input 
	# free precession time is defined as the time between the center of subsequent pulses. Hence, for a given pi-pulse length, 
	# we check that the user has selected a starting free precession time which produces an edge-to-edge time that is a multiple of t_min.
	# If not, we shift the free precession time vector by t_min/2 and warn the user.
	if (expCfg.sequence=='T2seq' and expCfg.numberOfPiPulses == 1):
		if (expCfg.scannedParam[0]-(expCfg.t_pi/4))%t_min:
			expCfg.scannedParam = [x+(t_min/2) for x in expCfg.scannedParam]
			print('Warning: Each element of the scanned time vector has been shifted by ',t_min/2,'ns so that the rising-edge-to-rising-edge spacing between microwave pulses is a multiple of ',t_min,'ns.\
\nDetails: The spacing between the rising edge of a pi or pi/2 pulse and the rising edge of the subsequent pi or pi/2 pulse in the T2 and XY8 sequences \
has to be an integer multiple of ',t_min,'ns. The user-input free-precession time is defined as the time between the center of subsequent pulses.\
Your pi pulse length,',expCfg.t_pi,'ns, produces an edge-to-edge time of', (expCfg.scannedParam[0]-(expCfg.t_pi/4)),'ns (at the start of the scan), which is not a multiple of ',t_min,'ns.\
Hence, we shift the times by ',t_min/2,'ns.')	
	if (expCfg.sequence =='XY8seq') or (expCfg.sequence=='T2seq' and expCfg.numberOfPiPulses > 1):
		half_t_delay = expCfg.scannedParam[0]/2
		if (half_t_delay-(expCfg.t_pi/4))%t_min:
			expCfg.scannedParam = [x+(t_min/2) for x in expCfg.scannedParam]
			print('Warning: Each element of the scanned time vector has been shifted by ',t_min/2,'ns so that the rising-edge-to-rising-edge spacing between microwave pulses is a multiple of ',t_min,'ns.\
\nDetails: The spacing between the rising edge of a pi or pi/2 pulse and the rising edge of the subsequent pi or pi/2 pulse in the T2 and XY8 sequences \
has to be an integer multiple of ',t_min,'ns. The user-input free-precession time is defined as the time between the center of subsequent pulses.\
Your pi pulse length,',expCfg.t_pi,'ns, produces an edge-to-edge time of', (half_t_delay-(expCfg.t_pi/4)),'ns (at the start of the scan), which is not a multiple of ',t_min,'ns.\
Hence, we shift the times by ',t_min/2,'ns.')
	if expCfg.sequence == 'correlSpecSeq':
		half_t_delay = expCfg.tau0/2
		if (half_t_delay-(expCfg.t_pi/4))%t_min:
			expCfg.tau0 = expCfg.tau0 +(t_min/2)*ns
			print('Warning: tau0 has been shifted by ',t_min/2,'ns so that the rising-edge-to-rising-edge spacing between microwave pulses is a multiple of ',t_min,'ns. tau0 is now set to', expCfg.tau0,'\
\nDetails: The spacing between the rising edge of a pi or pi/2 pulse and the rising edge of the subsequent pi or pi/2 pulse in the XY8 sequence \
has to be an integer multiple of ',t_min,'ns. The user-input tau0 is defined as the time between the center of subsequent pi pulses in the XY8 sequence.\
For your pi pulse length,',expCfg.t_pi,'ns, your chose tau0 produces an edge-to-edge time of', half_t_delay-(expCfg.t_pi/4),'ns, which is not a multiple of ',t_min,'ns.\
Hence, we shift the tau0 by ',t_min/2,'ns.')
					
def calculateContrast(contrastMode,signal,background):
# Calculates contrast based on the user's chosen contrast mode (configured in the experiment config file e.g. ESRconfig, Rabiconfig, etc)
	if contrastMode =='ratio_SignalOverReference':
		contrast = np.divide(signal,background)
	elif contrastMode =='ratio_DifferenceOverSum':
		contrast = np.divide(np.subtract(signal,background),np.add(signal,background))
	elif contrastMode == 'signalOnly':
		contrast = signal
	else:
		print('Error: Unrecognised contrast mode. Valid contrast modes are: \'ratio_SignalOverReference\',\'ratio_DifferenceOverSum\' or \'signalOnly\'. Please edit contrastMode variable in config script to match a valid contrast mode.')
		sys.exit()
	return contrast
	
def runExperiment(expConfigFile):
# This function runs the experiment with input parameters configured by the user in the experiment config file (e.g. ESRconfig, Rabiconfig, etc) and plots and saves the data.
	try:
		'''Runs the experiment.'''
		expCfg = import_module(expConfigFile)
		expCfg.N_scanPts = len(expCfg.scannedParam) #protection against non-integer user inputs for N_scanPts.
		validateUserInput(expCfg)
		#Check if save directory exists, and, if not, creates a "Saved Data" folder in the current directory, where all data will be saved.
		if not (isdir(expCfg.savePath)):
			 makedirs(expCfg.savePath)
			 print('Warning: Save directory did not exist, creating folder named Saved_Data in the working directory. Data will be saved to this directory.')
		
		#Initialise SRS and program PulseBlaster
		SRS = SRSctl.initSRS(conCfg.GPIBaddr,conCfg.modelName)
		SRSctl.setSRS_RFAmplitude(SRS,expCfg.microwavePower)
		SRSctl.setupSRSmodulation(SRS,expCfg.sequence)
		sequenceArgs = expCfg.updateSequenceArgs()
		expParamList = expCfg.updateExpParamList()
		if expCfg.sequence != 'ESRseq':
			SRSctl.setSRS_Freq(SRS, expCfg.microwaveFrequency)
			#Program PB
			seqArgList = [expCfg.scannedParam[-1]]
			seqArgList.extend(sequenceArgs)
			instructionArray=PBctl.programPB(expCfg.sequence,seqArgList)
		else:
			SRSctl.setSRS_Freq(SRS, expCfg.scannedParam[0])
			#Program PB
			instructionArray=PBctl.programPB(expCfg.sequence,sequenceArgs)
		SRSctl.enableSRS_RFOutput(SRS)
					
		#Configure DAQ
		DAQclosed = False
		DAQtask = DAQctl.configureDAQ(expCfg.Nsamples)
			
		if expCfg.plotPulseSequence:
		# Plot sequence
			plt.figure(0)
			[t_us,channelPulses,yTicks]=seqCtl.plotSequence(instructionArray,expCfg.PBchannels)
			for channel in channelPulses:
				plt.plot(t_us, list(channel))
				plt.yticks(yTicks)
				plt.xlabel('time (us)')
				plt.ylabel('channel')
				# If we are plotting a Rabi with pulse length <5*t_min, warn the user in the sequence plot title that the instructions sent to the PulseBlaster microwave channel are for a 5*t_min pulse, but that the short pulse flags are simultaneously pulsed to produce the desired pulse length
				if expCfg.sequence == 'RabiSeq' and (seqArgList[0]<(5*t_min)):
					plt.title('Pulse Sequence plot (at last scan point). Close to proceed with experiment...\n(note: we plot the instructions sent to the PulseBlaster (PB) for each channel. For microwave pulses<',5*t_min,'ns, the microwave\nchannel (PB_MW) is instructed to pulse for',5*t_min,'ns, but the short-pulse flags of the PB are pulsed simultaneously (not shown) to\nproduce the desired output pulse length at PB_MW. This can be verified on an oscilloscope.)', fontsize=7)
				else:
					plt.title('Pulse Sequence plot (at last scan point)\n close to proceed with experiment...')
			plt.show()
		
		#Initialize data arrays
		meanSignalCurrentRun = np.zeros(expCfg.N_scanPts)
		meanBackgroundCurrentRun = np.zeros(expCfg.N_scanPts)
		contrastCurrentRun = np.zeros(expCfg.N_scanPts)
		signal = np.zeros([expCfg.N_scanPts,expCfg.Navg])
		background = np.zeros([expCfg.N_scanPts,expCfg.Navg])
		contrast = np.zeros([expCfg.N_scanPts,expCfg.Navg])

		#Run experiment
		for i_run in range (0,expCfg.Navg):
			print('Run ',i_run+1,' of ',expCfg.Navg)
			if expCfg.randomize:
				if i_run>0:
					shuffle(expCfg.scannedParam)
			for i_scanPoint in range (0, expCfg.N_scanPts):
				#setup next scan iteration (e.g. for ESR experiment, change microwave frequency; for T2 experiment, reprogram pulseblaster with new delay)
				if expCfg.sequence == 'ESRseq':
					SRSctl.setSRS_Freq(SRS, expCfg.scannedParam[i_scanPoint])
				else:
					seqArgList[0] = expCfg.scannedParam[i_scanPoint]
					instructionArray= PBctl.programPB(expCfg.sequence,seqArgList)
				print('Scan point ',i_scanPoint+1,' of ',expCfg.N_scanPts)
				
				#read DAQ
				cts=DAQctl.readDAQ(DAQtask,2*expCfg.Nsamples,expCfg.DAQtimeout)
		
				#Extract signal and background counts
				sig = cts[0::2]
				bkgnd = cts[1::2]
							
				#Take average of counts
				meanSignalCurrentRun[i_scanPoint] = np.mean(sig)
				meanBackgroundCurrentRun[i_scanPoint] = np.mean(bkgnd)
				if expCfg.shotByShotNormalization:
					contrastCurrentRun[i_scanPoint] = np.mean(calculateContrast(expCfg.contrastMode,sig,bkgnd))
				else:
					contrastCurrentRun[i_scanPoint] = calculateContrast(expCfg.contrastMode,meanSignalCurrentRun[i_scanPoint],meanBackgroundCurrentRun[i_scanPoint])
				if i_run==0:
					if expCfg.livePlotUpdate:
						xValues=expCfg.scannedParam[0:i_scanPoint+1]
						plt.plot([x/expCfg.plotXaxisUnits for x in xValues],contrastCurrentRun[0:i_scanPoint+1], 'b-')
						plt.ylabel('Contrast')
						plt.xlabel(expCfg.xAxisLabel)
						plt.draw()
						plt.pause(0.0001)
					
					# Save data at intervals dictated by saveSpacing_inPulseLengthPts and at final delay point
					if (i_scanPoint%expCfg.saveSpacing_inScanPts == 0) or (i_scanPoint==expCfg.N_scanPts-1):
						data = np.zeros([i_scanPoint+1,3])
						data[:,0] = expCfg.scannedParam[0:i_scanPoint+1]
						data[:,1] = meanSignalCurrentRun[0:i_scanPoint+1]
						data[:,2] = meanBackgroundCurrentRun[0:i_scanPoint+1]
						dataFile = open(expCfg.dataFileName, 'w')
						for line in data:
							dataFile.write("%.0f\t%.8f\t%.8f\n" % tuple(line))
						paramFile = open(expCfg.paramFileName, 'w')
						expParamList[1] = i_scanPoint+1
						paramFile.write(expCfg.formattingSaveString % tuple(expParamList))
						dataFile.close()
						paramFile.close()
					
			#Sort current run counts in order of increasing delay
			dataCurrentRun = np.transpose(np.array([expCfg.scannedParam,meanSignalCurrentRun,meanBackgroundCurrentRun,contrastCurrentRun]))
			sortingIndices = np.argsort(dataCurrentRun[:,0])
			dataCurrentRun = dataCurrentRun[sortingIndices]
			#Fill in current run data:
			sortedScanParam = dataCurrentRun[:,0]
			signal[:,i_run] = dataCurrentRun[:,1]
			background[:,i_run] = dataCurrentRun[:,2]
			contrast[:,i_run] = dataCurrentRun[:,3]
			
			#Update quantities for plotting
			updatedSignal = np.mean(signal[:,0:i_run+1],1)
			updatedBackground = np.mean(background[:,0:i_run+1],1)
			updatedContrast = np.mean(contrast[:,0:i_run+1],1)
			
			#Update plot:
			if expCfg.livePlotUpdate: 
				plt.clf()
			plt.plot([x/expCfg.plotXaxisUnits for x in sortedScanParam] ,updatedContrast,'b-')
			plt.ylabel('Contrast')
			plt.xlabel(expCfg.xAxisLabel)
			plt.draw()
			plt.pause(0.001)
			
			# Save data at intervals dictated by saveSpacing_inAverages and after final scan
			if (i_run%expCfg.saveSpacing_inAverages == 0) or (i_run==expCfg.Navg-1):
				data = np.zeros([expCfg.N_scanPts,3])
				data[:,0] = sortedScanParam
				data[:,1] = updatedSignal
				data[:,2] = updatedBackground
				dataFile = open(expCfg.dataFileName, 'w')
				for item in data:
					dataFile.write("%.0f\t%.8f\t%.8f\n" % tuple(item))
				paramFile = open(expCfg.paramFileName, 'w')
				expParamList[3] = i_run+1
				paramFile.write(expCfg.formattingSaveString % tuple(expParamList))
				dataFile.close()
				paramFile.close()
		
		#Turn off SRS output
		SRSctl.disableSRS_RFOutput(SRS)

		#Close DAQ task:
		DAQctl.closeDAQTask(DAQtask)
		DAQclosed=True
		plt.show()
	except	KeyboardInterrupt:
		print('User keyboard interrupt. Quitting...')
		sys.exit()
	finally:
		if 'SRS' in vars():	
			#Turn off SRS output
			SRSctl.disableSRS_RFOutput(SRS)
		if ('DAQtask' in vars()) and  (not DAQclosed):
			#Close DAQ task:
			DAQctl.closeDAQTask(DAQtask)
			DAQclosed=True
	
if __name__ == "__main__":
	if len(sys.argv)>1 and (sys.argv[1] in ['ESRconfig','Rabiconfig','T1config','T2config','XY8config','correlSpecconfig']):
		expConfigFile=sys.argv[1]
	else:
		print('Usage: python mainControl.py <ESRconfig|Rabiconfig|T1config|T2config|XY8config|correlSpecconfig>')
		sys.exit()
	runExperiment(expConfigFile)