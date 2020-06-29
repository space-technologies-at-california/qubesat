#sequenceControl.py
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

import matplotlib.pyplot as plt
import math
import numpy as np
import sys
from collections import namedtuple
from spinapi import *
from connectionConfig import *

PBchannel = namedtuple('PBchannel',['channelNumber','startTimes','pulseDurations']) 

# Define t_min, time resolution of the PulseBlaster, given by 1/(clock frequency):
t_min = 1e3/PBclk #in ns 

#Short pulse flags:
ONE_PERIOD = 0x200000
TWO_PERIOD = 0x400000
THREE_PERIOD = 0x600000
FOUR_PERIOD = 0x800000 
FIVE_PERIOD= 0xA00000

def plotSequence(instructions,channelMasks):
	scalingFactor = 0.8
	t_ns = [0,0]
	pulses ={}
	tDone = False
	channelPulses=[]
	for channelMask in channelMasks.values():
		pulses[channelMask]=[0,channelMask&instructions[0][0]]
		for i in range(0, len(instructions)):
			currentPulseLength = instructions[i][3]
			if not tDone:
				previousEdgeTime = t_ns[-1]
				nextEdgeTime = previousEdgeTime + currentPulseLength
				t_ns.append(nextEdgeTime)
				t_ns.append(nextEdgeTime)
				if i == (len(instructions)-1):
					tDone = True
			if i==len(instructions)-1:
				pulses[channelMask].append(channelMask&instructions[i][0])
				pulses[channelMask].append(channelMask&instructions[i][0])
			else:
				pulses[channelMask].append(channelMask&instructions[i][0])
				pulses[channelMask].append(channelMask&instructions[i+1][0])
		t_us = np.divide(t_ns,1e3)
		channelPulses.append(list(np.add(math.log(channelMask,2),np.multiply(list(pulses[channelMask]),scalingFactor/channelMask))))
	yTicks = np.arange(math.log(min(channelMasks.values()),2), 1+math.log(max(channelMasks.values()),2),1)
	return [t_us,channelPulses,yTicks]



def sequenceEventCataloguer(channels):
	#Catalogs sequence events in terms of consecutive rising edges on the channels provided. Returns a dictionary, channelBitMasks, whose keys are event (rising/falling edge) times and values are the channelBitMask which indicate which channels are on at that time.
	eventCatalog ={} #dictionary where the keys are rising/falling edge times and the values are the channel bit masks which turn on/off at that time
	for channel in channels:
		channelMask = channel.channelNumber
		endTimes = [startTime + pulseDuration for startTime, pulseDuration in zip(channel.startTimes,channel.pulseDurations)]
		for eventTime in channel.startTimes+endTimes:
			eventChannelMask = channelMask
			if eventTime in eventCatalog.keys():
				eventChannelMask = eventCatalog[eventTime]^channelMask 
				#I'm XORing instead of ORing here in case someone has a zero-length pulse in the sequence. In that case, the XOR ensures that the channel does not turn on at the pulse start/end time. If we did an OR here, it would turn on and only turn off at the next event (which would have been a rising edge), so this would have given unexpected behaviour.
			eventCatalog[eventTime]=eventChannelMask
	channelBitMasks = {}
	currentBitMask=0
	channelBitMasks[0]=currentBitMask
	for event in sorted(eventCatalog.keys()):
		channelBitMasks[event]=currentBitMask^eventCatalog[event]
		currentBitMask = channelBitMasks[event]
	return channelBitMasks

################--------------------------------------------- PulseBlaster Sequences---------------------------------------------------###################
def makeSequence(sequence, args):
	if sequence == 'ESRseq':
		return makeESRseq(*args)
	elif sequence == 'RabiSeq':
		return makeRabiSeq(*args)
	elif sequence == 'T1seq':
		return makeT1Seq(*args)
	elif sequence == 'T2seq':
		return makeT2Seq(*args)
	elif sequence == 'XY8seq':
		return makeXY8seq(*args)
	elif sequence == 'correlSpecSeq':
		return makecorrelationSpectSeq(*args)
	elif sequence == 'optimReadoutSeq':
		return makeReadoutDelaySweep(*args)
	else:
		print('Error: requested sequence not recognised.')
		sys.exit

def makeESRseq(t_duration):
	t_sigAndref = 2*t_duration
	t_startTrig = t_min*round(300*ns/t_min)
	t_readout = t_min*round(300*ns/t_min)
	t_readoutBuffer= t_min*round(2*us/t_min)
	AOMchannel = PBchannel(AOM,[0],[t_sigAndref])
	uWchannel = PBchannel(uW,[0],[t_sigAndref/2])
	DAQchannel = PBchannel(DAQ,[(t_sigAndref/2)-t_readoutBuffer,t_sigAndref-t_readoutBuffer],[t_readout,t_readout])
	STARTtrigchannel = PBchannel(STARTtrig,[0],[t_startTrig])
	channels = [AOMchannel,DAQchannel,uWchannel, STARTtrigchannel]
	return channels

def makeReadoutDelaySweep(t_readoutDelay,t_AOM):
	t_startTrig = t_min*round(300*ns/t_min)
	start_delay = t_min*round(5*us/t_min)-t_startTrig
	t_readout = t_min*round(300*ns/t_min)
	AOMchannel = PBchannel(AOM,[start_delay],[t_AOM])
	DAQchannel = PBchannel(DAQ,[start_delay+t_readoutDelay],[t_readout])
	STARTtrigchannel = PBchannel(STARTtrig,[start_delay+t_AOM],[2*t_min*round(5*us/t_min)+t_startTrig])
	channels=[AOMchannel,DAQchannel, STARTtrigchannel]
	return channels
	
def makeRabiSeq(t_uW,t_AOM,t_readoutDelay):
	start_delay = t_min*round(1*us/t_min) + t_readoutDelay
	t_startTrig = t_min*round(300*ns/t_min)
	t_readout = t_min*round(300*ns/t_min)
	uWtoAOM_delay =t_min*round(1*us/t_min)	
	firstHalfDuration = start_delay + t_uW + uWtoAOM_delay+t_AOM
	if t_uW <=5*t_min and t_uW>0:
		uWchannel = PBchannel(uW,[start_delay],[5*t_min])
		shortpulseFLAG = int((t_uW/2)*ONE_PERIOD)
		shortPulseChannel =PBchannel(shortpulseFLAG, [start_delay],[5*t_min])
		channels = [shortPulseChannel,uWchannel]#Short pulse feature
	else:
		uWchannel = PBchannel(uW,[start_delay],[t_uW])
		channels = [uWchannel]
	AOMchannel = PBchannel(AOM,[firstHalfDuration-t_AOM,2*firstHalfDuration-t_AOM],[t_AOM,t_AOM])
	DAQchannel = PBchannel(DAQ,[firstHalfDuration-t_AOM+t_readoutDelay,2*firstHalfDuration-t_AOM+t_readoutDelay],[t_readout,t_readout])
	STARTtrigchannel = PBchannel(STARTtrig,[0],[t_startTrig])
	channels.extend([AOMchannel,DAQchannel, STARTtrigchannel])
	return channels

def makeT1Seq(t_delay,t_AOM,t_readoutDelay,t_pi):
	t_startTrig = t_min*round(300*ns/t_min)
	t_readout = t_min*round(300*ns/t_min)
	uWtoAOM_delay =t_min*round(1*us/t_min)
	AOMstartTime1 = t_delay
	firstHalfDuration=AOMstartTime1+t_AOM
	AOMstartTime2 =  firstHalfDuration+AOMstartTime1 
	AOMchannel = PBchannel(AOM,[AOMstartTime1,AOMstartTime2],[t_AOM,t_AOM])
	uWchannel = PBchannel(uW,[firstHalfDuration +t_readoutDelay + t_min*round(1*us/t_min)],[t_pi])
	DAQchannel = PBchannel(DAQ,[AOMstartTime1+t_readoutDelay, AOMstartTime2+t_readoutDelay],[t_readout,t_readout])
	STARTtrigchannel = PBchannel(STARTtrig,[0],[t_startTrig])
	channels = [AOMchannel,DAQchannel,uWchannel, STARTtrigchannel]
	return channels
	
def makeT2Seq(t_delay,t_AOM,t_readoutDelay,t_pi,IQpadding, numberOfPiPulses):
	t_piby2=t_pi/2
	t_startTrig = t_min*round(300*ns/t_min)
	t_readout = t_min*round(300*ns/t_min)
	uWtoAOM_delay =t_min*round(1*us/t_min)
	start_delay = (t_min*round(1*us/t_min) + t_readoutDelay) 
	#Make pulses for signal half of the sequence:
	[uWstartTimes1,uWdurations,IstartTimes1,Idurations,QstartTimes1,Qdurations]= makeCPMGpulses(start_delay,numberOfPiPulses,t_delay,t_pi, t_piby2,IQpadding)
	CPMGduration = uWstartTimes1[-1]+t_piby2-start_delay
	AOMstartTime1 = start_delay+CPMGduration +uWtoAOM_delay
	DAQstartTime1 = AOMstartTime1+t_readoutDelay
	firstHalfDuration = AOMstartTime1+t_AOM 
	#Make pulses for background half of the sequence:
	uWstartTimes2 =[x+firstHalfDuration for x in uWstartTimes1]
	#IstartTimes2 = [x+firstHalfDuration for x in IstartTimes1]
	QstartTimes2nd = QstartTimes1[:-1]
	QstartTimes2 = [x+firstHalfDuration for x in QstartTimes2nd]
	AOMstartTime2 = firstHalfDuration + AOMstartTime1
	DAQstartTime2 = firstHalfDuration + DAQstartTime1
	#Make full uW, I and Q pulse lists
	uWstartTimes=uWstartTimes1 +uWstartTimes2
	#Make channels:
	AOMchannel 		 = PBchannel(AOM,[AOMstartTime1,AOMstartTime2],[t_AOM,t_AOM])
	DAQchannel 		 = PBchannel(DAQ,[DAQstartTime1,DAQstartTime2],[t_readout,t_readout])
	uWchannel  		 = PBchannel(uW,uWstartTimes1 +uWstartTimes2,uWdurations+uWdurations)
	Ichannel   		 = PBchannel(I,IstartTimes1,Idurations)
	Qchannel   		 = PBchannel(Q,QstartTimes1+QstartTimes2,Qdurations+Qdurations[:-1])
	STARTtrigchannel = PBchannel(STARTtrig,[0],[t_startTrig])
	channels=[AOMchannel,DAQchannel, uWchannel, Ichannel, Qchannel, STARTtrigchannel]
	return channels
	
def makeXY8seq(t_delay,t_AOM,t_readoutDelay,t_pi,IQpadding, numberOfRepeats):
	t_piby2=t_pi/2
	t_startTrig = t_min*round(300*ns/t_min)
	t_readout = t_min*round(300*ns/t_min)
	uWtoAOM_delay =t_min*round(1*us/t_min)
	start_delay = (t_min*round(1*us/t_min) + t_readoutDelay) 
	#Make pulses for signal half of the sequence:
	[uWstartTimes1,uWdurations,IstartTimes1,Idurations,QstartTimes1,Qdurations]= makeXY8pulses(start_delay,numberOfRepeats,t_delay,t_pi, t_piby2,IQpadding)
	XY8duration = uWstartTimes1[-1]+t_pi/2-start_delay
	AOMstartTime1 = start_delay+XY8duration +uWtoAOM_delay
	DAQstartTime1 = AOMstartTime1+t_readoutDelay
	firstHalfDuration = AOMstartTime1+t_AOM 
	#Make pulses for background half of the sequence:
	uWstartTimes2 =[x+firstHalfDuration for x in uWstartTimes1]
	QstartTimes2nd = QstartTimes1[:-1]
	QstartTimes2 = [x+firstHalfDuration for x in QstartTimes2nd]
	AOMstartTime2 = firstHalfDuration + AOMstartTime1
	DAQstartTime2 = firstHalfDuration + DAQstartTime1
	#Make channels:
	AOMchannel 		 = PBchannel(AOM,[AOMstartTime1,AOMstartTime2],[t_AOM,t_AOM])
	DAQchannel 		 = PBchannel(DAQ,[DAQstartTime1,DAQstartTime2],[t_readout,t_readout])
	uWchannel  		 = PBchannel(uW,uWstartTimes1 +uWstartTimes2,uWdurations+uWdurations)
	Ichannel   		 = PBchannel(I,IstartTimes1,Idurations)
	Qchannel   		 = PBchannel(Q,QstartTimes1+QstartTimes2,Qdurations+Qdurations[:-1])
	STARTtrigchannel = PBchannel(STARTtrig,[0],[t_startTrig])
	channels=[AOMchannel,DAQchannel, uWchannel, Ichannel, Qchannel, STARTtrigchannel]
	return channels
	
	
def makecorrelationSpectSeq(t_delay_betweenXY8seqs,t_delay, t_AOM,t_readoutDelay,t_pi,IQpadding,numberOfRepeats):
	t_piby2=t_pi/2
	t_startTrig = t_min*round(300*ns/t_min)
	t_readout = t_min*round(300*ns/t_min)
	uWtoAOM_delay =t_min*round(1*us/t_min)
	start_delay = t_min*round(2*us/t_min)
	#Make pulses for first XY8 in the first half of the sequence (I only pulses in second XY8 of second half, so we will take the I times here and shift them in time):
	[uWstartTimes1a,uWdurations1a,IstartTimes,Idurations,QstartTimes1a,Qdurations1a]= makeXY8pulses(start_delay,numberOfRepeats,t_delay,t_pi, t_piby2,IQpadding)
	#Make pulses for second XY8 in the first half of the sequence:
	firstXY8duration = uWstartTimes1a[-1]+t_piby2
	uWstartTimes1b = [x+firstXY8duration + t_delay_betweenXY8seqs for x in uWstartTimes1a]
	QstartTimes1b = [x +firstXY8duration + t_delay_betweenXY8seqs for x in QstartTimes1a]
	Qdurations1b = Qdurations1a
	#Make AOM pulse and DAQ pulse for signal half
	XY8duration = uWstartTimes1b[-1]+t_pi/2-start_delay
	AOMstartTime1 = start_delay+XY8duration +uWtoAOM_delay
	DAQstartTime1 = AOMstartTime1+t_readoutDelay
	firstHalfDuration = AOMstartTime1+t_AOM 
		
	#Make pulses for first XY8 in the second half of the sequence (no I's on this half):
	uWstartTimes2 = [x+firstHalfDuration for x in uWstartTimes1a+uWstartTimes1b]
	QstartTimes2 = [x+firstHalfDuration for x in QstartTimes1a+QstartTimes1b[:-1]]
	AOMstartTime2 = firstHalfDuration + AOMstartTime1
	DAQstartTime2 = firstHalfDuration + DAQstartTime1
	IstartTimes = [x +firstHalfDuration+firstXY8duration+t_delay_betweenXY8seqs for x in IstartTimes]
	
	#concatenate pulse times:
	uWstartTimes = uWstartTimes1a+uWstartTimes1b+uWstartTimes2
	uWdurations = uWdurations1a*4
	QstartTimes = QstartTimes1a+QstartTimes1b+QstartTimes2
	Qdurations = Qdurations1a+Qdurations1b+Qdurations1a+Qdurations1b[:-1]
	
	#Make channels:
	AOMchannel 		 = PBchannel(AOM,[AOMstartTime1,AOMstartTime2],[t_AOM,t_AOM])
	DAQchannel 		 = PBchannel(DAQ,[DAQstartTime1,DAQstartTime2],[t_readout,t_readout])
	uWchannel  		 = PBchannel(uW,uWstartTimes,uWdurations)
	Ichannel   		 = PBchannel(I,IstartTimes,Idurations)
	Qchannel   		 = PBchannel(Q,QstartTimes,Qdurations)
	STARTtrigchannel = PBchannel(STARTtrig,[0],[t_startTrig])
	channels=[AOMchannel,DAQchannel, uWchannel, Ichannel, Qchannel, STARTtrigchannel]
	return channels
		
def makeCPMGpulses(start_delay,numberOfPiPulses,t_delay,t_pi, t_piby2,IQpadding):
	t_piby4 = t_piby2/2;
	if numberOfPiPulses == 1:
		uWstartTimes = [start_delay, start_delay +t_delay-t_piby4, start_delay +2*t_delay] 
		uWdurations =  [t_piby2, t_pi, t_piby2]
	else:
		half_t_delay = t_delay/2
		#Start off the sequence by adding the initial pi/2 and first pi pulse
		uWstartTimes =[start_delay, start_delay +half_t_delay-t_piby4] 
		uWdurations =[t_piby2, t_pi]
		#Add remaining pi pulses:
		for i in range(1,numberOfPiPulses):
			currentEdgeTime = uWstartTimes[-1]+t_delay
			uWstartTimes.append(currentEdgeTime)
			uWdurations.append(t_pi)
		#Append the final pi/2 pulse:
		uWstartTimes.append(uWstartTimes[-1]+half_t_delay+t_piby4)
		uWdurations.append(t_piby2)
	#Make the I and Q channel pulses:
	#Q is ON during pi(y) pulses and the final pi/2(-x), but not the first pi/2(x) pulse
	QstartTimes = [x-IQpadding for x in uWstartTimes[1:]]
	Qdurations=[x +2*IQpadding for x in uWdurations[1:]]
	#I is only on during the final pi/2(-x) pulse:
	IstartTimes =[x-IQpadding for x in [uWstartTimes[-1]]]
	Idurations =[x +2*IQpadding for x in [uWdurations[-1]]]
	return [uWstartTimes,uWdurations,IstartTimes,Idurations,QstartTimes,Qdurations]
	
def makeXY8pulses(start_delay,numberOfRepeats,t_delay,t_pi, t_piby2,IQpadding):
	t_piby4=t_piby2/2
	#Start off the sequence by adding the initial pi/2:
	half_t_delay = t_delay/2
	uWstartTimes =[start_delay] 
	uWdurations =[t_piby2]
	QstartTimes=[]
	Qdurations =[]
	#Add remaining pi pulses:
	firstPiPulseDone = False
	for i in range(0,numberOfRepeats):
		#Make next 8 pi pulses:
		next8piPulseStartTimes =[]
		next8piPulseDurations=[]
		#Add the first pulse in the set of 8
		currentEdgeTime=0
		if not firstPiPulseDone:
			currentEdgeTime = uWstartTimes[-1]+half_t_delay-t_piby4
			firstPiPulseDone=True
		else:
			currentEdgeTime = uWstartTimes[-1]+t_delay
		next8piPulseStartTimes.append(currentEdgeTime)
		next8piPulseDurations.append(t_pi)
		for j in range (1,8):
			newEdgeTime = next8piPulseStartTimes[-1]+t_delay
			next8piPulseStartTimes.append(newEdgeTime)
			next8piPulseDurations.append(t_pi)
		# Make next 8 Q start times (Q is only on for pulses 1,3,4,6 of the xy8 pi pulses, for a 0-indexed sequence):
		next8QstartTimes = list(next8piPulseStartTimes[i] for i in [1,3,4,6])
		next8Qdurations = list(next8piPulseDurations[i] for i in [1,3,4,6])
		# Append next 8 pi pulses and Q pulses to start times lists:
		uWstartTimes.extend(next8piPulseStartTimes)
		uWdurations.extend(next8piPulseDurations)
		QstartTimes.extend(next8QstartTimes)
		Qdurations.extend(next8Qdurations)
		
	#Append the final pi/2 pulse:
	uWstartTimes.append(uWstartTimes[-1]+half_t_delay+t_piby4)
	uWdurations.append(t_piby2)
	#Append the final pi/2 pulse to Q channel since (in the signal bin) Q is on for this pulse as it is a -x pulse.
	QstartTimes.append(uWstartTimes[-1])
	Qdurations.append(uWdurations[-1])
	#Pad the Q channel pulses:
	QstartTimes = [x-IQpadding for x in QstartTimes]
	Qdurations=[x +2*IQpadding for x in Qdurations]
	#Make I channel pulses. I is only on during the final pi/2(-x) pulse:
	IstartTimes =[x-IQpadding for x in [uWstartTimes[-1]]]
	Idurations =[x +2*IQpadding for x in [uWdurations[-1]]]
	return [uWstartTimes,uWdurations,IstartTimes,Idurations,QstartTimes,Qdurations]
	
