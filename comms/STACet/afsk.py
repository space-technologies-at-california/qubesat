#  STACet AX.25 AFSK Packet Engine
#
#    Copyright (C) 2020  Max Burns
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# --------------------------------------------------------------------------
#   AFSK.py
#       Handles turning going to and from AFSK tones to AX.25 Packets
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
# Imports

import itertools
import math
import audiogen
import var
from var import bitarray

# --------------------------------------------------------------------------
# Variable setup

np = var.np
r_ = var.r_
MARK_HZ = var.MARK
SPACE_HZ = var.SPACE
BAUD_RATE = var.BAUD
RATE = var.RATE
PADDED_ZEROS = var.PADDED_ZEROS
PADDED_FRAMES = var.PADDED_FRAMES

TWO_PI = 2.0 * np.pi


# --------------------------------------------------------------------------

#
#
#
def afsk(bits):
    # TODO: docstring
    # the function will take a bitarray of bits and will output an AFSK1200 modulated signal of them, sampled at 44100Hz
    fc = SPACE_HZ - (SPACE_HZ - MARK_HZ) / 2
    delta_f = (SPACE_HZ - MARK_HZ) / 2
    fs = RATE * 4
    baud = BAUD_RATE
    Ns = fs / baud

    code = {0: [-1.0 for k in range(int(Ns))], 1: [1.0 for k in range(int(Ns))]}
    to_mod = []
    for bit in list(bits):
        to_mod += code[bit]

    t = r_[0:len(to_mod)] / (fs * 1.0)
    afsk = np.cos(2 * np.pi * fc * t + 2 * np.pi * delta_f * np.cumsum(to_mod) / fs)
    afsk = afsk[::4]

    # TODO: plotting code

    return afsk


#
#
#
def encode(binary_data):
    framed_data = frame(binary_data)

    iters = itertools.chain(audiogen.silence(.05), audiogen.multiply(modulate(framed_data), audiogen.constant(0.5)),
                            audiogen.silence(.05))
    for sample in iters:
        yield sample


#
#
#
def modulate(data):
    '''
    Generate Bell 202 AFSK samples for the given symbol generator
    Consumes raw wire symbols and produces the corresponding AFSK samples.
    '''
    seconds_per_sample = 1.0 / RATE
    phase, seconds, bits = 0, 0, 0

    # construct generators
    clock = (x / BAUD_RATE for x in itertools.count(1))
    tones = (MARK_HZ if bit else SPACE_HZ for bit in data)

    for boundary, frequency in zip(clock, tones):
        # frequency of current symbol is determined by how much
        # we advance the signal's phase in each audio frame
        phase_change_per_sample = TWO_PI / (RATE / frequency)

        # produce samples for the current symbol
        # until we reach the next clock boundary
        while seconds < boundary:
            yield math.sin(phase)

            seconds += seconds_per_sample
            phase += phase_change_per_sample

            if phase > TWO_PI:
                phase -= TWO_PI

        bits += 1


#
#
#
def nrzi(data):
    '''
    Packet uses NRZI (non-return to zero inverted) encoding, which means
    that a 0 is encoded as a change in tone, and a 1 is encoded as
    no change in tone.
    '''
    current = True
    for bit in data:
        if not bit:
            current = not current
        yield current


#
#
#
def frame(stuffed_data):
    return nrzi(
        itertools.chain(
            bitarray.bitarray("00000000") * PADDED_ZEROS,
            bitarray.bitarray("01111110") * PADDED_FRAMES,
            stuffed_data,
            bitarray.bitarray("01111110")
        )
    )
