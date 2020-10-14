from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, data = wavfile.read('packet.wav')

MAX_INT = 2147483647

data = list(map(lambda x : x / (MAX_INT * 1.0), data))

data_size = len(data)

f = open('../Raw_Input/raw_audio.txt', 'w')
f.write("%d\n" %data_size)

for i in range(data_size):
	f.write("%f\n" %data[i])

f.close()