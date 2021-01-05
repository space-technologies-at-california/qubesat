import utils
import numpy as np
import matplotlib.pyplot as plt

#Define constants for utils
utils.BAUD_RATE = 960
utils.SAMP_RATE = 96000
utils.FREQ_LOW  = 1e3
utils.FREQ_HIGH = 1e5

#randomly generate a true binary message
sig_len = 0
true_msg = np.concatenate((np.array(10 * [0, 1]), np.random.randint(2, size=sig_len)))

#use utils to generate an FSK signal (with/wo noise) 
meas_sig = utils.gen_fsk(true_msg, pre = 1, post = 1, noise = 0.01)

#use utils to decode the measured FSK signal
meas_msg = utils.decode_fsk_zc(meas_sig, sig_thresh = 0.5, zc_thresh = 0.05, width = int(0.80 * utils.SAMP_RATE / utils.BAUD_RATE))

#Find the percent error between the two bit sequences
bit_err = utils.loss(meas_msg, true_msg)
print(str(bit_err * 100) + "% error")

plt.plot(meas_sig)
plt.show()
