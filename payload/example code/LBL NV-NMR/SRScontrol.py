# SRS control
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
import visa
import sys
# Frequency unit multiplier definitions
Hz =1
kHz =1e3
MHz=1e6
GHz=1e9


unicode = lambda s: str(s)

##-------------------- Function definitions--------------------
def initSRS(GPIBaddr,modelName):
	#initSRS: opens a GPIB communication channel with the SRS.
	#		   arguments: - GPIBaddr: int describing GPIB address of SRS. For model SG384, the factory default is 27.
	#					  - modelName: string describing SRS model. e.g.'SG384'
	
	#Check model name is recognised:
	if modelName not in ('SG382','SG384','SG386','SG392','SG394','SG396'):
		print('Error: SRS model name ',modelName,' not recognized. This code has only been tested with SRS models SG384 and SG386, but also recognises models SG382, SG392, SG394, SG396. If you are using a different SRS model, and you think it is compatible with the functions in SRScontrol.py, please edit the initSRS function in SRScontrol.py to include your model.\n')
		sys.exit()
	elif modelName not in ['SG384', 'SG386']:
		print('Warning: This code has only been tested with SRS models SG384 and SG386, but will likely also support other SG models. Please refer to your SRS\'s manual and check that the functions used in SRScontrol.py are compatible with your model\'s GPIB interface.') 
	#Construct instrument identifier from GPIB address:
	SRSaddr = unicode('GPIB0::'+str(GPIBaddr)+'::INSTR')
	#Instantiate a resource manager
	rm = visa.ResourceManager()
	# Try quering SRS identity:
	SRS = rm.open_resource(SRSaddr)
	try:
		deviceID = SRS.query('*IDN?')
	except Exception as excpt:
		print('Error: could not query SRS. Please check GPIB address is correct and SRS GPIB communication is enabled. Exception details:', type(excpt).__name__,'.',excpt)
		sys.exit()
	if 'Stanford Research Systems,'+modelName not in deviceID:
		print('Error: Instrument at this GPIB address, (',GPIBaddr,') is not an SRS '+modelName+'. When sent an identity query, \'*IDN?\', it returned ',deviceID,'. Please check the your SRS signal generator\'s GPIB address and/or model name.\n') 
		sys.exit() 
	# Clear the ESR (Standard Event Status Register), INSR (Instrument Status Register) and LERR (Last Error Buffer):
	SRS.write('*CLS')
	return SRS

def SRSerrCheck(SRS):
	err = SRS.query('LERR?')
	if int(err) is not 0:
		print('SRS error: error code', int(err),'. Please refer to SRS manual for a description of error codes.')
		sys.exit()
			
def enableSRS_RFOutput(SRS):
	SRS.write('ENBR 1')
	SRSerrCheck(SRS)

def disableSRS_RFOutput(SRS):
	SRS.write('ENBR 0')
	SRSerrCheck(SRS)
	
def setSRS_RFAmplitude(SRS,RFamplitude, units='dBm'):
	SRS.write('AMPR '+str(RFamplitude)+' '+units)
	SRSerrCheck(SRS)
	
def setSRS_Freq(SRS,freq, units='Hz'):
	#setSRSFreq: Sets frequency of the SRS output. You can call this function with one argument only (the first argument, freq),
	#			 in which case the argument freq must be in Hertz. This function can also be called with both arguments, the first
	#			 specifying the frequency and the second one specifying the units, as detailed below.
	#			 arguments: - freq: float setting frequency of SRS. This must either be in Hz if the units argument is not passed.
	#					    - units: string describing units (e.g. 'MHz'). For SRS384, minimum unit is 'Hz', max 'GHz'
	SRS.write('FREQ '+str(freq)+' '+units)
	SRSerrCheck(SRS)

def setupSRSmodulation(SRS,sequence):
	#Enables IQ modulation with an external source for T2, XY8 and correlation spectroscopy sequences
	#and disables modulation for ESR, Rabi and T1 sequences.
	if sequence in ['ESRseq', 'RabiSeq', 'T1seq']:
		disableModulation(SRS)
	elif sequence in ['T2seq','XY8seq','correlSpecSeq']:
		enableIQmodulation(SRS)
	else:
		print('Error in SRScontrol.py: unrecognised sequence name passed to setupSRSmodulation.')
		sys.exit()
	
def enableIQmodulation(SRS):
	SRSerrCheck(SRS)
	#Enable modulation
	SRS.write('MODL 1')
	SRSerrCheck(SRS)
	#Set modulation type to IQ
	SRS.write('TYPE 6')
	SRSerrCheck(SRS)
	#Set IQ modulation function to external
	SRS.write('QFNC 5')	

def disableModulation(SRS):
	SRS.write('MODL 0')
	SRSerrCheck(SRS)
	
def queryModulationStatus(SRS):
	status = SRS.query('MODL?')
	SRSerrCheck(SRS)
	if status=='1\r\n':
		print('SRS modulation is on...')
		IQstatus = SRS.query('TYPE?')
		SRSerrCheck(SRS)
		if IQstatus=='6\r\n':
			print('...and is set to IQ')
		else:
			print('...but is not set to IQ.')
	else:
		print('SRS modulation is off.')
	return status