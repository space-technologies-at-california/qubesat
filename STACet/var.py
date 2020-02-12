#imports
import numpy as np
from numpy import r_
from numpy import fft
from numpy import random
from scipy import signal
import bitarray

#vars
BAUD = 1200.0
RATE = 48000
MARK = 1200
SPACE = 2200

PADDED_ZEROS = 20
PADDED_FRAMES = 100