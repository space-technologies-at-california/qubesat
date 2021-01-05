import numpy as np
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
def decode_fsk_zc(fsk_sig, sig_thresh = 0.3, zc_thresh = 0.1, width = 5):
	#sequecne of 1s and 0s that we will return
	msg = []

	#Iterate through signal until it begins
	ind = 0
	while abs(fsk_sig[ind]) < sig_thresh:
		ind += 1

	#Move to halfway of the bit pulse
	ind += float(SAMP_RATE / BAUD_RATE) / 2

	#Start zero crossing technique
	mx = float('inf')
	while mx > sig_thresh:
		mx = 0
		zcs = 0
		is_pos = fsk_sig[int(ind) - width//2] > 0
		for k in range(-width // 2, width // 2):
			wind_ind = k + int(ind)
			#First, we calculate max of the window with width = 'width'
			if abs(fsk_sig[wind_ind]) > mx:
				mx = abs(fsk_sig[wind_ind])
			#Next, we determine the amount of zero crossings
			if is_pos and fsk_sig[wind_ind] < 0:
				is_pos = False
				zcs += 1
			elif not is_pos and fsk_sig[wind_ind] > 0:
				is_pos = True
				zcs += 1

		#Percentage of zero crossings in the window
		z_pcnt = zcs / width

		#Append new bit
		msg.append(int(z_pcnt > zc_thresh))

		#increment by 1 bit
		ind += float(SAMP_RATE / BAUD_RATE)

	#Remove last element, I know bad loop structure whatever
	return np.array(msg[:-1])


"""
Decodes an FSK signal into its binary sequence/message. We will be using the
correlation method. We multiply the signal by sine waves at different phase shifts
to convert the fsk signal into a square wave.
Inputs:
	fsk_sig - the FSK signal to decode, as an np array
Outputs:
	np array - the sequence of 1s and 0s that the FSK signal encodes
"""
def decode_fsk_cor(fsk_sig):
	#Generate sine for low and high signals
	t = np.arange(len(fsk_sig)) / SAMP_RATE
	phi_low, phi_high = 0, 0
	s_low  = np.sin(FREQ_LOW * 2 * np.pi * t)
	s_high = np.sin(FREQ_HIGH * 2 * np.pi * t)
	c_l = np.correlate(fsk_sig, s_low, 'same')
	c_h = np.correlate(fsk_sig, s_high, 'same')
	i_l = np.argmax(c_l)
	i_h = np.argmax(c_h)

	print(i_l, i_h)
	
	s_low  = np.roll(np.sin(FREQ_LOW * 2 * np.pi * t), 27)
	s_high = np.roll(np.sin(FREQ_HIGH * 2 * np.pi * t), 7)
	#plt.plot(fsk_sig)

	def moving_average(s, n):
		return np.convolve(s, np.ones(n), 'valid') / n

	dig = fsk_sig * (s_high - s_low)
	plt.subplot(3,1,1)
	plt.plot(fsk_sig)
	plt.subplot(3,1,2)
	plt.plot(s_high)
	plt.subplot(3,1,3)
	plt.plot(moving_average(dig, 100))
	plt.show()



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
		msg2 = np.append(msg2, np.zeros(l1 - l2))
	elif l2 > l1:
		msg1 = np.append(msg1, np.zeros(l2 - l1))
	return sum(abs(msg1 - msg2)) / len(msg1)


#Start fuck around	
msg =  np.array([0, 0, 1])#np.random.randint(2, size=3)
print(msg)
meas_sig = gen_fsk(msg, pre = 0.1, post = 0.1, noise = 0)
decode_fsk_cor(meas_sig)
