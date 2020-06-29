#PBcontrol.py
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
from ctypes import *
from spinapi import *
import numpy as np
import sequenceControl as seqCtl
from connectionConfig import *
import sys
def errorCatcher(statusVar):
	if statusVar<0:
		print ('Error: ', pb_get_error())
		sys.exit()
		
def configurePB():
	pb_set_debug(1)
	status = pb_init()
	errorCatcher(status)
	pb_core_clock(PBclk)
	return 0

def pb_inst_pbonly(flags,inst,inst_data,length):
	flags = c_uint(flags)
	inst = c_int(inst)
	inst_data = c_int(inst_data)
	length = c_double(length)
	return spinapi.pb_inst_pbonly(flags, inst, inst_data, length)
	
def programPB(sequence,sequenceArgs):
	channels=seqCtl.makeSequence(sequence, sequenceArgs)
	channelBitMasks = seqCtl.sequenceEventCataloguer(channels)
	#instructionArray=programSequence(channelBitMasks)
	instructionArray = produceSequence(channelBitMasks)
	return instructionArray
	
def programSequence(channelBitMasks):
	eventTimes = list(channelBitMasks.keys())
	numEvents = len(eventTimes)
	eventDurations =list(np.zeros(numEvents-1))
	numInstructions = numEvents-1
	for i in range(0,numInstructions):
		if i == numInstructions-1:
			eventDurations[i] = eventTimes[i+1]-eventTimes[i]
		else:
			eventDurations[i] = eventTimes[i+1]-eventTimes[i]
	instructionArray = []
	bitMasks = list(channelBitMasks.values())
	start = [0]
	for i in range(0,numEvents-1):
		if i==(numEvents-2):
			instructionArray.extend([[bitMasks[i], Inst.BRANCH, start[0], eventDurations[i]]])
		else:
			instructionArray.extend([[bitMasks[i], Inst.CONTINUE, 0, eventDurations[i]]])
	
	#Program Pulseblaster
	configurePB()
	status = pb_start_programming(PULSE_PROGRAM)
	errorCatcher(status)
	startDone = False
	for i in range(0, len(instructionArray)):
		if startDone:
			status = pb_inst_pbonly(instructionArray[i][0],instructionArray[i][1],instructionArray[i][2],instructionArray[i][3])
			errorCatcher(status)
		else:
			start[0]= pb_inst_pbonly(instructionArray[0][0],instructionArray[0][1],instructionArray[0][2],instructionArray[0][3])
			errorCatcher(start[0])
			startDone = True
	status = pb_stop_programming()
	errorCatcher(status)
	status = pb_start()
	print("Continuing will stop program execution\n");
	input("Please press a key to continue.")
	errorCatcher(status)
	status = pb_close()
	errorCatcher(status)
	return instructionArray
	
	
def produceSequence(channelBitMasks):
	eventTimes = list(channelBitMasks.keys())
	numEvents = len(eventTimes)
	eventDurations =list(np.zeros(numEvents-1))
	numInstructions = numEvents-1
	for i in range(0,numInstructions):
		if i == numInstructions-1:
			eventDurations[i] = eventTimes[i+1]-eventTimes[i]
		else:
			eventDurations[i] = eventTimes[i+1]-eventTimes[i]
	instructionArray = []
	bitMasks = list(channelBitMasks.values())
	start = [0]
	for i in range(0,numEvents-1):
		if i==(numEvents-2):
			instructionArray.extend([[bitMasks[i], Inst.BRANCH, start[0], eventDurations[i]]])
		else:
			instructionArray.extend([[bitMasks[i], Inst.CONTINUE, 0, eventDurations[i]]])
	return instructionArray