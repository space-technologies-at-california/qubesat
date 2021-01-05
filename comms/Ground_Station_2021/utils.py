import numpy as np
import itertools
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

#Important constants needed for encoding and decoding signals
BAUD_RATE = 960
SAMP_RATE = 96000
FREQ_LOW  = 1e3
FREQ_HIGH = 1e5

"""
Generates a Frequency Shift Keyed signal, or FSK signal, given a bit array.
Inputs:
	bit_arr - an array of 1s and 0s
	pre - the percentage of time that there is no signal (just noise) before transmission
	post - the percentage of time that there is no signal (just noise) after transmission
Outputs:
	np array - an np array representing the FSK signal
"""
def gen_fsk(bit_arr, pre = 0, post = 0, noise = 0):
	#Generate low and high sig
	samp_per_bit = SAMP_RATE // BAUD_RATE
	t = np.arange(len(bit_arr) * samp_per_bit) / SAMP_RATE
	s_low  = np.sin(FREQ_LOW * 2 * np.pi * t)
	s_high = np.sin(FREQ_HIGH * 2 * np.pi * t)

	#Generate mask
	mask = np.empty(0)
	one = np.ones(samp_per_bit)
	zero = np.zeros(samp_per_bit)
	for bit in bit_arr:
		if bit:
			mask = np.append(mask, one)
		else:
			mask = np.append(mask, zero)

	#Pre and Post signals
	s_pre  = np.random.normal(0, noise, int(len(mask) * pre))
	s_post = np.random.normal(0, noise, int(len(mask) * post))

	#FSK Signal masking + noise if needed
	return np.concatenate((s_pre, mask * s_high + (1 - mask) * s_low + np.random.normal(0, noise, len(mask)), s_post))

"""
Decodes an FSK signal into its binary sequence/message. We will be using the
zero crossing methods, which simply counts how many times the signal has 
changed from negative to positive (or vise versa) in order to detect low from
high frequencies.
Inputs:
	fsk_sig - the FSK signal to decode, as an np array
	sig_thresh - the value where we accept a signal, not noise
	zc_thresh - hyperparemeter for percent of zero crossings in window
	width - the width of the window for zero crossing calculation
Outputs:
	np array - the sequence of 1s and 0s that the FSK signal encodes
"""
def decode_fsk_zc(fsk_sig, sig_thresh = 0.3, zc_thresh = 0.1, raw_perc = False):
	#sequecne of 1s and 0s that we will return
	msg = []

	#Iterate through signal until it begins
	ind = 0
	while abs(fsk_sig[ind]) < sig_thresh:
		ind += 1

	#Move to halfway of the bit pulse
	ind += float(SAMP_RATE / (2 * BAUD_RATE))

	#Start zero crossing technique
	mx = float('inf')
	width = width = int(0.90 * SAMP_RATE / BAUD_RATE)
	while mx > sig_thresh:
		#Max and zero crossings in the window
		window = fsk_sig[int(ind - width//2):int(ind + width//2)]
		mx = max(abs(min(window)), max(window))
		zcs = len(list(itertools.groupby(window, lambda x: x > 0)))

		#Percentage of zero crossings in the window
		z_pcnt = zcs / width

		#Append new bit
		if not raw_perc:
			msg.append(int(z_pcnt > zc_thresh))
		else:
			msg.append(z_pcnt)


		#increment by 1 bit
		ind += float(SAMP_RATE / BAUD_RATE)


	#Remove last element, I know bad loop structure whatever
	return np.array(msg[:-1])


"""
Decodes an FSK signal into its binary sequence/message. We will use
a phase allignment method
	fsk_sig - the FSK signal to decode, as an np array
Outputs:
	np array - the sequence of 1s and 0s that the FSK signal encodes
"""
def decode_fsk_PA(fsk_sig, sig_thresh = 0.5):
	#sequence of 1s and 0s that we will return
	msg = []

	#Iterate through signal until it begins
	ind = 0
	while abs(fsk_sig[ind]) < sig_thresh:
		ind += 1

	#Generate low and high sine waves
	t = np.arange(len(fsk_sig)) / SAMP_RATE
	s_low  = np.sin(FREQ_LOW * 2 * np.pi * t)
	s_high = np.sin(FREQ_HIGH * 2 * np.pi * t)

	#Now that we are at the start of the signal, (we leverage preamble)
	#We can sample a LOW wave and find the phase:
	indl = ind
	low_sine = fsk_sig[int(indl):int(indl + (SAMP_RATE / BAUD_RATE))]
	t0 = (indl + np.argmax(low_sine)) / SAMP_RATE
	s_low  = np.sin(FREQ_LOW * 2 * np.pi * (t - t0) + np.pi / 2)
	#Same for High
	indh = ind + SAMP_RATE / BAUD_RATE
	high_sine = fsk_sig[int(indh):int(indh + (SAMP_RATE / BAUD_RATE))]
	t0 = (indh + np.argmax(high_sine)) / SAMP_RATE
	s_high = np.sin(FREQ_HIGH * 2 * np.pi * (t - t0) + np.pi / 2)

	#Now we convert our signal into highs and lows
	diff_sig = fsk_sig * (s_high - s_low)
	samp_per_bit = SAMP_RATE / BAUD_RATE
	width = int(samp_per_bit * 0.5)
	mx = float('inf')
	ind += samp_per_bit / 2
	while mx > sig_thresh:
		#In a window, find the max value to see if signal or noise
		window = diff_sig[int(ind - width//2):int(ind + width//2)]
		mx = max(abs(min(window)), max(window))

		#Now we can take the mean over the window and append it to the message
		msg.append(int(np.mean(window) > 0))

		#increment by 1 bit
		ind += float(SAMP_RATE / BAUD_RATE)
	
	return np.array(msg[:-1])


"""
Computes the percent of different bits between msg1 and msg2. If the lengths are not
equal, every extra bit counts as incorrect.
Inputs:
	msg1 - first sequence of 1s and 0s as an array
	msg2 - second sequence of 1s and 0s as an array
Outputs:
	float - the percentage of bits that differ
"""
def loss(msg1, msg2):
	l1, l2 = len(msg1), len(msg2)
	if l1 > l2:
		msg2 = np.append(msg2, 1 - msg1[l2:])
	elif l2 > l1:
		msg1 = np.append(msg1, 1 - msg2[l1:])
	return sum(abs(msg1 - msg2)) / len(msg1)
