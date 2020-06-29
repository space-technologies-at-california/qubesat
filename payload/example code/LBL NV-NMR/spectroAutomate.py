import SRScontrol as SRSctl
from seabreeze.spectrometers import Spectrometer
import time
import csv
import matplotlib.pyplot as p
import datetime

#constants
START_FREQUENCY = 2.5
END_FREQUENCY = 3.2
STEP_FREQUENCY = 0.005
START_WAVELENGTH = 600
END_WAVELENGTH = 850
INTEGRATION_TIME = 10000000 #in microseconds
## 5s (2/24/2020); 10s (2/25)

#take experiment start time for storing files
date_time=str(datetime.datetime.now())

#init 2D array to store intensities and 1D array to store frequencies
intensities = []
frequencies = []

#assuming only one spectrometer, find spectrometer and set integration time
spec = Spectrometer.from_first_available()
spec.integration_time_micros(INTEGRATION_TIME)

#initiate RF generator with channel and model type; set amplitude
my_SRS = SRSctl.initSRS(27, 'SG386')
SRSctl.setSRS_RFAmplitude(my_SRS, .14, units = "Vpp")

#set test frequency and modulation
SRSctl.setSRS_Freq(my_SRS, 1, 'GHz')
SRSctl.setupSRSmodulation(my_SRS, 'ESRseq')

#store all wavelengths that spectrometer would read
wavelengths = spec.wavelengths()

#method to find wavelength index in an array of wavelengths
def findWavelength(wavelength):
	for i in range(0, len(wavelengths)):
		if (wavelengths[i] > wavelength):
			return i

#finding indexes of START and END frequency
start_index = findWavelength(START_WAVELENGTH)
end_index = findWavelength(END_WAVELENGTH) - 1

#delete extraneous wavelengths in array
wavelengths = wavelengths[start_index:end_index]

#initiate counter for iterating through frequencies
f = START_FREQUENCY

while f <= END_FREQUENCY:
	#store frequency to create array of all frequencies for data analysis
	frequencies+= [f]

	#init RF generator with each frequency
	SRSctl.setSRS_Freq(my_SRS, f, 'GHz')

	#turn on the microwave excitation - changed the sequence here, zhao, 02/24/2020
	SRSctl.enableSRS_RFOutput(my_SRS)
	time.sleep(.1)

	#read spectrum
	intensities.append(spec.intensities()[start_index:end_index])

	#turn off the microwave excitation
	SRSctl.disableSRS_RFOutput(my_SRS)
	time.sleep(.1)

	#read spectrum
	intensities.append(spec.intensities()[start_index:end_index])

	f += STEP_FREQUENCY

#simple file writer - make sure to close csv file before running
def write(x, name):
	with open(name, 'w', newline = '') as csv_file:
		writer = csv.writer(csv_file)
		f = START_FREQUENCY
		i = 0

		#Writing first row with all wavelengths
		w = ['Frequencies\\ wavelengths']
		w.extend(wavelengths)
		writer.writerow(w)

		#writing each row with frequency then pre-microwave excitation and post-microwave excitation
		while f <= END_FREQUENCY:
			freq = [f,]
			freq.extend(x[i])
			post = [f,]
			post.extend(x[i+1])

			writer.writerow(freq)
			writer.writerow(post)
			f += STEP_FREQUENCY
			i += 2

#writing the intensities file
write(intensities, "intensities" + "_" + date_time[0:4] + date_time[5:7] + date_time[8:10] + '_' + date_time[11:13] + date_time[14:16] + date_time[17:19] + ".csv") 

#method to find average amplitude of each run of amplitudes
def average_amplitude(intensities):
	avg = []
	for i in range(0, len(intensities)):
		avg += [sum(intensities[i])/(end_index - start_index + 1)]
	return avg

#generic plotter
def plot(name, x, y):
	p.figure(1)
	p.plot(x, y, '-')
	p.savefig(name)
	p.close()

#plotting frequency vs amplitudeg
avg_amplitude = average_amplitude(intensities[::2])
plot("plot" + "_" + date_time[0:4] + date_time[5:7] + date_time[8:10] + '_' + date_time[11:13] + date_time[14:16] + date_time[17:19] + ".png", frequencies, avg_amplitude)   
