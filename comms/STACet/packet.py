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
#   packet.py
#       builds packets from data, and detects packets from audio input
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
# Imports

import var
from var import bitarray
import ax25
import afsk

# --------------------------------------------------------------------------
# Variable setup

np = var.np
r_ = var.r_
fft = var.fft
random = var.random
signal = var.signal

BAUD = var.BAUD
RATE = var.RATE


# --------------------------------------------------------------------------

#
# This takes in SRC DEST DIGI and INFO and returns the AX.25 PACKET
#
def gen_packet(src, dest, digi, info):
    packet = ax25.UI(
        destination=dest,
        source=src,
        info=info,
        digipeaters=digi.split(b','),
    )
    return packet


#
# This builds the Frame Check Sequence FCS
# FCS is used to see if received packet is corrupted in transit
#
def genfcs(bits):
    # Generates a checksum from packet bits
    fcs = ax25.FCS()
    for bit in bits:
        fcs.update_bit(bit)

    digest = bitarray.bitarray(endian="little")
    digest.frombytes(fcs.digest())

    return digest


#
# This takes in NRZI data (from receive.nc_afskDemod)
# and returns a list of packets dectected between flags (01111110)
# It also returns the position of the last flag
#
def detectFrames(NRZI):
    # function looks for packets in an NRZI sequence and validates their checksum

    # compute finite differences of the digital NRZI to detect zero-crossings
    dNRZI = NRZI[1:] - NRZI[:-1]
    # find the position of the non-zero components. These are the indexes of the zero-crossings.
    transit = np.nonzero(dNRZI)[0]
    # Transition time is the difference between zero-crossings
    transTime = transit[1:] - transit[:-1]

    # loop over transitions, convert to bit streams and extract packets
    dict = {1: bitarray.bitarray([0]), 2: bitarray.bitarray([1, 0]), 3: bitarray.bitarray([1, 1, 0]),
            4: bitarray.bitarray([1, 1, 1, 0]), 5: bitarray.bitarray([1, 1, 1, 1, 0]),
            6: bitarray.bitarray([1, 1, 1, 1, 1, 0])
        , 7: bitarray.bitarray([1, 1, 1, 1, 1, 1, 0])}

    state = 0;  # no flag detected yet

    packets = []
    tmppkt = bitarray.bitarray([0])
    lastFlag = 0  # position of the last flag found.

    for n in range(0, len(transTime)):
        Nb = round(transTime[n] / (RATE / BAUD))  # maps intervals to bits. Assume 44100Hz and 1200baud
        if (Nb == 7 and state == 0):
            # detected flag frame, start collecting a packet
            tmppkt = tmppkt + dict[7]
            state = 1  # packet detected
            lastFlag = transit[n - 1]
            continue
        if (Nb == 7 and state == 1):
            # detected end frame successfully
            tmppkt = tmppkt + dict[7]
            # validate checksum
            bitsu = ax25.bit_unstuff(tmppkt[8:-8])  # unstuff bits
            # print(genfcs(bitsu[:-16]).tobytes(),"  ", bitsu[-16:].tobytes())
            if (genfcs(bitsu[:-16]).tobytes() == bitsu[-16:].tobytes()):
                # valid packet
                packets.append(tmppkt)
            tmppkt = bitarray.bitarray([0])
            state = 0
            continue

        if (state == 1 and Nb < 7 and Nb > 0):
            # valid bits
            tmppkt = tmppkt + dict[Nb]
            continue
        else:
            # not valid bits reset
            state = 0
            tmppkt = bitarray.bitarray([0])
            continue

    if state == 0:
        lastFlag = -1

    # if the state is 1, which means that we detected a packet, but the buffer ended, then
    # we return the position of the beginning of the flag within the buffer to let the caller
    # know that there's a packet that overlapps between two buffer frames.

    return packets, lastFlag


#
# Takes in the AX.25 data and turns it into usable information
#
def decodeAX25(bits):
    ax = ax25.AX25()
    ax.info = "bad packet"

    bitsu = ax25.bit_unstuff(bits[8:-8])

    if (genfcs(bitsu[:-16]).tobytes() == bitsu[-16:].tobytes()) == False:
        # print("failed fcs")
        return ax

    byte = bitsu.tobytes()
    destination = ax.callsign_decode(bitsu[:56])
    if isinstance(destination[-1], int) and destination[-1] != "0":
        ax.destination = b"".join((destination[:-1], b'-', str(destination[-1]).encode("utf-8")))
    else:
        ax.destination = destination[:-1].strip()

    source = ax.callsign_decode(bitsu[56:112])

    if isinstance(source[-1], int) and source[-1] != "0":
        ax.source = b"".join((source[:-1], b'-', str(source[-1]).encode("utf-8")))
    else:
        ax.source = source[:-1]

    digilen = 0

    if byte[14] == '\x03' and byte[15] == '\xf0':
        digilen = 0
    else:
        for n in range(14, len(byte) - 1):
            if byte[n] & 1:
                digilen = (n - 14) + 1
                break

    ax.digipeaters = ax.callsign_decode(bitsu[112:112 + digilen * 8])
    ax.info = str(bitsu[112 + digilen * 8 + 16:-16].tobytes())[2:-1]

    return ax
