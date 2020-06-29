# ESRconfig.py
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
ESR experiment config

This script can be used to configure mainControl.py to run an Electron Spin Resonance (ESR) experiment. Fluorescence emitted by an NV diamond sample is recorded as a function of the frequency of a microwave drive signal, and the data is saved as a tabulated text file (see below for saving options). The microwave frequency is scanned from startFreq to endFreq in N_scanPts steps. At each frequency point, the script takes 2*Nsamples fluorescence readings, turning the microwaves on and off for successive samples in order to establish the background fluorescence level. We hence have Nsamples with microwaves on (signal counts) and Nsamples with microwaves off (background, or reference, counts). After the first scan over frequencies is complete, the script proceeds to repeat the scan Navg times, averaging the contrast at each frequency point over all runs (see below for contrast definitions and averaging options).

-- Contrast setting --
From signal and background counts, the script will calculate contrast based on one of two formulas, defined by the contrastMode variable. If contrastMode is set to 'ratio_SignalOverReference', contrast is defined as the ratio of signal to background. If contrastMode is set to 'ratio_DifferenceOverSum', contrast is defined as the ratio of the difference between signal and background to the sum of signal and background. The user may also select a 'signalOnly' contrast mode, where only the signal counts are plotted and the background counts are ignored.

-- Averaging options --
By default, for each frequency point, the script calculates the contrast as a function of the averaged signal counts (averaged over the Nsamples signal readings at a given frequency point) and the averaged background counts - e.g. if the contastMode is set to ratio_SignalOverReference, the contrast is, by default, calculated by dividing the average of the Nsamples of signal by the average of the Nsamples of background. If you prefer to instead calculate contrast as a function of subsequent signal and background samples and then average across all samples, set the shotByShotNormalization option to True -e.g. if contrastMode is ratio_SignalOverReference and shotByShotNormalization is set to True, the contrast will be calculated by dividing each signal sample by the subsequent background sample taking the average of these ratios.

The first time the script scans over the microwave drive frequency of the signal generator, it does so in order from the smallest to the largest frequency. If Navg>1, the script then repeats the scan Navg times and averages the results. By default, the order of the frequency points is randomized for all but the first scan. If you wish to turn off this randomization, set the randomize option below to False.

-- Plotting options --
Set livePlotUpdate to True to plot the data as it is acquired. Note that, after the first scan is completed, the plot will only update at the end of every subsequent scan. If livePlotUpdate is set to False, the data will only be plotted at the end of the experiment.

Set plotPulseSequence to True to plot the pulse sequence which has been programmed into the PulseBlaster. Note that the program will wait for the user to close this plot before continuing.

-- Saving options --
The user can choose how often the data is saved. For the first scan, there is an option to save at intervals of saveSpacing_inScanPts (i.e. if this variable is set to 2, the script will resave the data at every other frequency point). For subsequent scans, the script will resave the data at the end of a frequency scan, for averaging runs spaced by intervals of saveSpacing_inAverages (e.g. if this is set to 3, the data will be resaved after every 3 averages). Regardless of how the user sets these options, data will always be saved at the end of the first frequency scan and at the end of the experiment (i.e. after the last averaging run).

To run this script:
 1) Edit connectionConfig.py to define the PulseBlaster, SRS and DAQ channel connections being used in your setup.
 2) Edit the user inputs section below.
 3) Run the script. From a windows command prompt, the script can be run by calling python mainControl.py ESRconfig
 
 User inputs:
 *startFreq: lowest frequency point in the scan, in Hz.
 *endFreq:  highest frequency point in the scan, in Hz.
 *N_scanPts: number of frequency points in the scan.
 *microwavePower: output power of the SRS signal generator, in dBm. CAUTION: this should not exceed the input power of any amplifiers connected to the SRS output.
 *t_duration: duration of the signal-aquisition half of one iteration of ESR pulse sequence.
 *Nsamples: number of fluorescence measurement samples to take at each frequency point.
 *Navg: number of averaging runs (i.e. number of times the frequency scan is repeated).
 *plotPulseSequence: if set to True, this script will generate a plot of the pulse sequence ouput by the PulseBlaster
 *DAQtimeout: amount of time (in seconds) for which the DAQ will wait for the requested number of samples to become available (ie. to be acquired)
 *contrastMode: set this to one of 'ratio_SignalOverReference', 'ratio_DifferenceOverSum' or 'signalOnly', depending on which contrast mode you want to use (see 'Contrast setting' description above)
 *livePlotUpdate: set this to True to update the plot as data is acquired (see 'Plotting options' above)
 *plotPulseSequence: set this to True to plot the pulse sequence at the start of the experiment (see 'Plotting options' above)
 *plotXaxisUnits: sets x-axis units on the data plot. Select from Hz, kHz, MHz or GHz
 *xAxisLabel: sets x-axis label on the data plot
 *saveSpacing_inScanPts: interval, in number of frequency points, at which data is saved during the first scan.
 *saveSpacing_inAverages: interval, in number of averaging runs, at which data is saved after the first complete scan.
 *savePath: path to folder where data will be saved. By default, data is saved in a folder called Saved_Data in the directory where this script is saved
 *saveFileName: file name under which to save the data. This name will later be augmented by the date and time at which the script was run.
 *shotByShotNormalization: set this option to True to do shot by shot contrast normalization (see 'Averaging Options' above).
 *randomize: set this option to True to randomize the order of frequency points in all scans after the first one.
"""
#Imports
from spinapi import ns,us,ms
from SRScontrol import Hz, kHz, MHz, GHz
import os
import numpy as np
from time import localtime, strftime
from connectionConfig import *
# Define t_min, time resolution of the PulseBlaster, given by 1/(clock frequency):
t_min = 1e3/PBclk #in ns

#-------------------------  USER INPUT  ---------------------------------------#

# Microwave scan parameters:----------------------------------------------------
# Start frequency (in Hz):
startFreq = 2.7e9
# End frequency (in Hz):
endFreq = 3.0e9
# Number of frequency steps:
N_scanPts = 101
# Microwave power output from SRS(dBm) - DO NOT EXCEED YOUR AMPLIFIER'S MAXIMUM INPUT POWER:
microwavePower = -5 
# Pulse sequence parameters:----------------------------------------------------
# Duration of the signal-aquisition half of one iteration of ESR pulse sequence:
t_duration = 80*us
# Number of fluorescence measurement samples to take at each frequency point:
Nsamples = 1000
# Number of averaging runs to do:
Navg = 1
#DAQ timeout, in seconds:
DAQtimeout = 10
# Contrast mode
contrastMode ='ratio_SignalOverReference'
# Plotting options--------------------------------------------------------------
# Live plot update option
livePlotUpdate = True
# Plot pulse sequence option  - set to true to plot the pulse sequence
plotPulseSequence = True
# Plot x axis units (Hz, kHz, MHz or GHz)
plotXaxisUnits = Hz
# Plot x axis label
xAxisLabel = 'Frequency (Hz)'
# Save options------------------------------------------------------------------
# Save interval for first scan through all frequency points:
saveSpacing_inScanPts = 2
# Save interval in averaging runs:
saveSpacing_inAverages = 1
# Path to folder where data will be saved:
savePath = os.getcwd()+"\\Saved_Data\\"
# File name for data file
saveFileName = "ESR_"
# Averaging options:------------------------------------------------------------
# Option to do shot by shot contrast normalization:
shotByShotNormalization = False
# Option to randomize order of scan points
randomize = True
#------------------------- END OF USER INPUT ----------------------------------#

scannedParam = np.linspace(startFreq,endFreq, N_scanPts, endpoint=True)
#Sequence string:
sequence = 'ESRseq'
#Scan start Name
scanStartName = 'startFreq'
#Scan end Name
scanEndName = 'endFreq'
#PB channels
PBchannels = {'AOM':AOM,'uW':uW,'DAQ':DAQ,'STARTtrig':STARTtrig}
#Sequence args
sequenceArgs = [t_duration]
#Make save file path
dateTimeStr = strftime("%Y-%m-%d_%Hh%Mm%Ss", localtime())
dataFileName = savePath + saveFileName+ dateTimeStr +".txt"
#Make param file path
paramFileName = savePath + saveFileName+dateTimeStr+'_PARAMS'+".txt"
#Param file save settings
formattingSaveString = "%s\t%d\n%s\t%d\n%s\t%d\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%f\n%s\t%r\n%s\t%r\n%s\t%r\n%s\t%d\n%s\t%d\n%s\t%s\n"
expParamList =  ['N_scanPts:',N_scanPts,'Navg:',Navg,'Nsamples:',Nsamples,'startFreq:',scannedParam[0],'endFreq:',scannedParam[-1],'microwavePower:',microwavePower,'t_duration:',t_duration,'shotByShotNormalization:',shotByShotNormalization,'randomize:',randomize,'plotPulseSequence:',plotPulseSequence,'saveSpacing_inScanPts:',saveSpacing_inScanPts,'saveSpacing_inAverages:',saveSpacing_inAverages,'dataFileName:',dataFileName]

def updateSequenceArgs():
	sequenceArgs = [t_duration]
	return sequenceArgs
	
def updateExpParamList():
	expParamList =  ['N_scanPts:',N_scanPts,'Navg:',Navg,'Nsamples:',Nsamples,'startFreq:',scannedParam[0],'endFreq:',scannedParam[-1],'microwavePower:',microwavePower,'t_duration:',t_duration,'shotByShotNormalization:',shotByShotNormalization,'randomize:',randomize,'plotPulseSequence:',plotPulseSequence,'saveSpacing_inScanPts:',saveSpacing_inScanPts,'saveSpacing_inAverages:',saveSpacing_inAverages,'dataFileName:',dataFileName]
	return expParamList