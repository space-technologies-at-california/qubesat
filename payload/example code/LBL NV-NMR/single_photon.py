import nidaqmx
import nidaqmx.system
from  nidaqmx.constants import *
from connectionConfig import *
import numpy as np
import sys

#system = nidaqmx.system.System.local()
DAQ_APDInput = "DEV1/ctr0"   ## the signal from single photon counter.

def configureDAQ(Nsamples):
	try:
		NsampsPerDAQread=2*Nsamples
		readTask = nidaqmx.Task()
		channel = readTask.ci_channels.add_ci_count_edges_chan(DAQ_APDInput,"", initial_count=0, edge=Edge.RISING, count_direction=CountDirection.COUNT_UP)  
		#Configure sample clock
		readTask.timing.cfg_samp_clk_timing(DAQ_MaxSamplingRate,DAQ_SampleClk,Edge.RISING,AcquisitionType.FINITE, NsampsPerDAQread)
		channel.ci_count_edges_term = 'PFI0'
		#Configure start trigger
		readArmTrig = readTask.triggers.arm_start_trigger
		readArmTrig.trig_type = TriggerType.DIGITAL_EDGE
		readArmTrig.dig_edge_src = DAQ_StartTrig

		#Configure start trigger
		# readStartTrig = readTask.triggers.start_trigger
		# readStartTrig.cfg_dig_edge_start_trig(DAQ_StartTrig,Edge.RISING)
		
	except Exception as excpt:
		print('Error configuring DAQ. Please check your DAQ is connected and powered. Exception details:', type(excpt).__name__,'.',excpt)
		closeDAQTask(task)
		sys.exit()
	return readTask, channel
def readDAQ(task, channel, N,timeout):
	try:
		counts = task.read(N, timeout)
	except Exception as excpt:
		print('Error: could not read DAQ. Please check your DAQ\'s connections. Exception details:', type(excpt).__name__,'.',excpt)
		sys.exit()
	return counts
	
def closeDAQTask(task):
	task.close()
