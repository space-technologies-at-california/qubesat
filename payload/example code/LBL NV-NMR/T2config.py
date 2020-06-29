# T2config.py
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

"""
T2 experiment config

This script can be used to configure mainControl.py to run a T2 experiment. Fluorescence emitted by an NV diamond sample is recorded as a function of the duration of a scanned delay in the T2 pulse sequence (see protocol), and the data is saved as a tabulated text file (see below for saving options). If the user chooses to have only one pi pulse in the sequence (i.e. if the user input numberOfPiPulses is set to 1), the scanned delay is the delay between the pi/2 pulses and the pi pulse. If the user instead selects to apply more than one pi pulse in the T2 sequence (i.e. numberOfPiPulses>1), the scanned delay is the delay between pi pulses. The delay is scanned from startTau to endTau in N_scanPts steps. At each scan point, the script takes 2*Nsamples fluorescence readings, phase-shifting the last pi/2 pulse in the pulse sequence by 180 degrees in successive samples in order to obtain two fluorescence-count readouts, R1 and R2, from which the contrast will be calculated (as explained below under 'Contrast setting'). We hence have Nsamples for the first readout and Nsamples for the second readout. After the first scan is complete, the script proceeds to repeat the scan Navg times, averaging the contrast at each scan point over all runs (see below for contrast definitions and averaging options).

-- Contrast setting --
The contrast mode for experiment should be set to 'ratio_DifferenceOverSum'. In this mode, the contrast C is calculated from the two readouts R1 and R2 by taking the ratio of their difference to their sum, i.e. C= (R1-R2)/(R1+R2). For debugging purposes, the user may also select the one of the other two contrast modes: 'signalOnly', in which only R1 will be plotted, or 'ratio_SignalOverReference', in which R1/R2 will be plotted.

-- Averaging options --
By default, for each scan point, the script calculates the contrast as a function of the averaged R1 counts (averaged over the Nsamples R1 readings at a given scan point) and the averaged R2 counts. If you prefer to instead calculate contrast C as a function of subsequent R1 and R2 samples and then average C across all samples, set the shotByShotNormalization option to True - e.g. with contrastMode set to 'ratio_DifferenceOverSum' and shotByShotNormalization set to True, the contrast will be calculated by taking the ratio (R1-R2)/(R1 + R2) for each pair of R1 and R2 samples and then taking the average of these ratios.

The first time the script scans over the delays, it does so in order from the shortest to the longest delay. If Navg>1, the script then repeats the scan Navg times and averages the results. By default, the order of the scan points is randomized for all but the first scan. If you wish to turn off this randomization, set the randomize option below to False.

-- Plotting options --
Set livePlotUpdate to True to plot the data as it is acquired. Note that, after the first scan is completed, the plot will only update at the end of every subsequent scan. If livePlotUpdate is set to False, the data will only be plotted at the end of the experiment.

Set plotPulseSequence to True to plot the pulse sequence which has been programmed into the PulseBlaster. Note that the program will wait for the user to close this plot before continuing.

-- Saving options --
The user can choose how often the data is saved. For the first scan, there is an option to save at intervals of saveSpacing_inScanPts (i.e. if this variable is set to 2, the script will resave the data at every other scan point). For subsequent scans, the script will resave the data at the end of a scan, for averaging runs spaced by intervals of saveSpacing_inAverages (e.g. if this is set to 3, the data will be resaved after every 3 averages). Regardless of how the user sets these options, data will always be saved at the end of the first scan and at the end of the experiment (i.e. after the last averaging run).

-- IQ padding --
In order to account for cable/instrumentation delays, we add a delay, IQpadding, between the pulse edges which turn on and off the I and/or Q modulation of the SRS and the pulse edges which turn on and off the microwaves, to ensure that the I and/or Q modulation is on for the entire duration of the microwave pulse. This delay should only be edited with careful monitoring of the pulse sequence on an oscilloscope. If the user wishes to change it, it is listed under 'Advanced user options' in the user-input section below.

To run this script:
 1) Edit connectionConfig.py to define the PulseBlaster, SRS and DAQ channel connections being used in your setup.
 2) Edit the user inputs section below.
 3) Run the script. From a windows command prompt, the script can be run by calling python mainControl.py T2config
 
 User inputs:
 -->Note: t_min is defined as the time resolution of your PulseBlaster card (i.e.t_min = 1/(clock frequency)). E.g. for a 500MHz card, t_min = 2ns. 
 *startTau: if numberOfPiPulses is set to 1, this is the shortest delay (in ns) between pi/2 and pi pulses and must be  >(2*IQpadding + (3/4)*t_pi + (5*t_min)); 
			if numberOfPiPulses>1, this is the shortest delay (in ns) between pi-pulses and must be >(2*(2*IQpadding + (3/4)*t_pi + (5*t_min)))
 *endTau: longest delay in scan, in ns. 
 *N_scanPts: number of points in the scan. Note: the delay being scanned in this script is the delay between pi pulses in the pulse sequence, which is double the delay between the initial/final pi/2 pulse and the first/last pi pulse. Therefore, the step size for this delay must be at least 2*t_min, double the PulseBlaster's finest timing resolution (1/clock frequency).
 *microwavePower: output power of the SRS signal generator, in dBm. CAUTION: this should not exceed the input power of any amplifiers connected to the SRS output.
 *microwaveFrequency: microwave frequency output by SRS signal generator (Hz)
 *t_AOM: duration of AOM pulse, in ns
 *t_readoutDelay: delay between start of AOM pulse and DAQ readout pulse (ns). The optimum delay can be found using optimReadoutDelay.py (see step 54 in our protocol paper)
 *t_pi: pi pulse duration, in ns
 *numberOfPiPulses: number of pi pulses applied during each pulse sequence
 *Nsamples: number of fluorescence measurement samples to take at each scan point
 *Navg: number of averaging runs (i.e. number of times the delay scan is repeated)
 *DAQtimeout: amount of time (in seconds) for which the DAQ will wait for the requested number of samples to become available (ie. to be acquired)
 *contrastMode: for this experiment, this should be set to set this to 'ratio_DifferenceOverSum'. Other available contrast modes are 'ratio_SignalOverReference' and 'signalOnly' (see 'Contrast setting' description above)
 *livePlotUpdate: set this to True to update the plot as data is acquired (see 'Plotting options' above)
 *plotPulseSequence: set this to True to plot the pulse sequence at the start of the experiment (see 'Plotting options' above)
 *plotXaxisUnits: sets x-axis units on the data plot. Select from ns, us or ms
 *xAxisLabel: sets x-axis label on the data plot
 *saveSpacing_inScanPts: interval, in number of frequency points, at which data is saved during the first scan.
 *saveSpacing_inAverages: interval, in number of averaging runs, at which data is saved after the first complete scan.
 *savePath: path to folder where data will be saved. By default, data is saved in a folder called Saved_Data in the directory where this script is saved
 *saveFileName: file name under which to save the data. This name will later be augmented by the date and time at which the script was run.
 *shotByShotNormalization: set this option to True to do shot by shot contrast normalization (see 'Averaging Options' above).
 *randomize: set this option to True to randomize the order of frequency points in all scans after the first one.
 *IQpadding: delay between the pulse edges which turn on and off the IQ and the pulse edges which turn on and off the microwaves, in ns. 
"""
from spinapi import ns,us,ms
import os
import numpy as np
from time import localtime, strftime
from connectionConfig import *
# Define t_min, time resolution of the PulseBlaster, given by 1/(clock frequency):
t_min = 1e3/PBclk #in ns
#-------------------------  USER INPUT  ---------------------------------------#

# Scan parameters:-------------------------------------------------------------
# Start delay duration (in nanoseconds):
startTau =100
# End delay duration (in nanoseconds):
endTau = 10000
# Number of delay steps:
N_scanPts = 200
# Microwave power output from SRS(dBm) - DO NOT EXCEED YOUR AMPLIFIER'S MAXIMUM INPUT POWER:
microwavePower = -5
# Microwave frequency (Hz):
microwaveFrequency = 2e9 
# Pulse sequence parameters:----------------------------------------------------
# AOM pulse duration (in ns)
t_AOM= 5*us
# Readout delay (in ns)
t_readoutDelay = 2.3*us
# Pi-pulse duration (in ns)
t_pi = 24
# Number of pi pulses:
numberOfPiPulses = 1
# Number of fluorescence measurement samples to take at each delay point:
Nsamples = 10000
# Number of averaging runs to do:
Navg = 1
#DAQ timeout, in seconds:
DAQtimeout = 10
# Plotting options--------------------------------------------------------------
# Contrast mode
contrastMode ='ratio_DifferenceOverSum'
# Live plot update option
livePlotUpdate = True
# Plot pulse sequence option  - set to true to plot the pulse sequence
plotPulseSequence = True
# Plot x axis unit multiplier (ns, us or ms)
plotXaxisUnits = ns
# Plot x axis label
xAxisLabel = 'Delay (ns)'
# Save options------------------------------------------------------------------
# Save interval for first scan through all delay points:
saveSpacing_inScanPts = 2
# Save interval in averaging runs:
saveSpacing_inAverages = 3
# Path to folder where data will be saved:
savePath = os.getcwd()+"\\Saved_Data\\"
# File name for data file
saveFileName = "T2_"
# Averaging options:------------------------------------------------------------
# Option to do shot by shot contrast normalization:
shotByShotNormalization = False
# Option to randomize order of scan points
randomize = True
#Advanced user options--------------------------------------------------------------
# IQ padding, in ns (this should be left at t_min*round(30*ns/t_min),unless the user  
# requires an especially short free precession delay - this parameter should only be 
# editted with close monitoring of the pulse sequence on the scope.
IQpadding = t_min*round(30*ns/t_min)
#------------------------- END OF USER INPUT ----------------------------------#

scannedParam = np.linspace(startTau,endTau, N_scanPts, endpoint=True) 
#Sequence string:
sequence = 'T2seq'
#Scan start Name
scanStartName = 'startTau'
#Scan end Name
scanEndName = 'endTau'
#PB channels
PBchannels = {'AOM':AOM,'uW':uW,'DAQ':DAQ,'STARTtrig':STARTtrig,'I':I,'Q':Q}
#Sequence args
sequenceArgs = [t_AOM,t_readoutDelay,t_pi,IQpadding,numberOfPiPulses]
#Make save file path
dateTimeStr = strftime("%Y-%m-%d_%Hh%Mm%Ss", localtime())
dataFileName = savePath + saveFileName+ dateTimeStr +".txt"
#Make param file path
paramFileName = savePath + saveFileName+dateTimeStr+'_PARAMS'+".txt"
#Param file save settings
formattingSaveString = "%s\t%d\n%s\t%d\n%s\t%d\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%r\n%s\t%r\n%s\t%r\n%s\t%d\n%s\t%d\n%s\t%s\n"
expParamList = ['N_scanPts:',N_scanPts,'Navg:',Navg,'Nsamples:',Nsamples,'startTau:',scannedParam[0],'endTau:',scannedParam[-1],'microwavePower:',microwavePower,'microwaveFrequency',microwaveFrequency,'t_AOM:',t_AOM, 't_readoutDelay:',t_readoutDelay,'t_pi',t_pi,'numberOfPiPulses',numberOfPiPulses,'IQpadding',IQpadding,'shotByShotNormalization:',shotByShotNormalization,'randomize:',randomize,'plotPulseSequence:',plotPulseSequence,'saveSpacing_inScanPts:',saveSpacing_inScanPts,'saveSpacing_inAverages:',saveSpacing_inAverages,'dataFileName:',dataFileName]

def updateSequenceArgs():
	sequenceArgs = [t_AOM,t_readoutDelay,t_pi,IQpadding,numberOfPiPulses]
	return sequenceArgs
	
def updateExpParamList():
	expParamList = ['N_scanPts:',N_scanPts,'Navg:',Navg,'Nsamples:',Nsamples,'startTau:',scannedParam[0],'endTau:',scannedParam[-1],'microwavePower:',microwavePower,'microwaveFrequency',microwaveFrequency,'t_AOM:',t_AOM, 't_readoutDelay:',t_readoutDelay,'t_pi',t_pi,'numberOfPiPulses',numberOfPiPulses,'IQpadding',IQpadding,'shotByShotNormalization:',shotByShotNormalization,'randomize:',randomize,'plotPulseSequence:',plotPulseSequence,'saveSpacing_inScanPts:',saveSpacing_inScanPts,'saveSpacing_inAverages:',saveSpacing_inAverages,'dataFileName:',dataFileName]
	return expParamList