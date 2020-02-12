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
#   receive.py
#       handles the audio input, and build packets from it
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
# Imports

import pyaudio
import var
import packet
from multiprocessing import Process, Pipe
import time
import socket
import console

# --------------------------------------------------------------------------
# Variable setup

np = var.np
r_ = var.r_
fft = var.fft
random = var.random
signal = var.signal

BAUD = var.BAUD
MARK = var.MARK
SPACE = var.SPACE

RATE = var.RATE
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RECORD_SECONDS = 5

SENSITIVITY = 1000
# --------------------------------------------------------------------------


# Set up socket for nc (net cat) on mac or putty on windows
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8001))


#
# for printing to the socket
#
def sock_print(string):
    string = string + '\n'
    sock.send(string.encode("utf-8"))


#
# This takes a audio signal and finds the MARK and SPACE audio in it
# returns the NRZI data in the waveform between MARK and SPACE
#
def nc_afskDemod(sig, tbw=2.0, fs=RATE):
    baud = BAUD
    M = int(2 / (baud / fs))
    h = signal.firwin(M, 600, nyq=fs / 2)
    t = r_[0:len(h)] / fs

    bp_mark = h * np.exp(t * 1j * MARK * 2.0 * np.pi)
    bp_space = h * np.exp(t * 1j * SPACE * 2.0 * np.pi)

    filt_mark = abs(signal.fftconvolve(bp_mark, sig))
    filt_space = abs(signal.fftconvolve(bp_space, sig))
    NRZI = filt_space - filt_mark

    return NRZI


#
# This takes a signal and gets the data inside. This is setup for testing right not
#
def get_data(sig):
    #    sock_print("* demoding *")

    NRZIa = nc_afskDemod(sig)
    NRZI = np.sign(NRZIa)

    packets, lastflag = packet.detectFrames(NRZI)
    # print(len(packets))
    for pack in packets:
        ax = packet.decodeAX25(pack)
        sock_print("Dest: %s | Source: %s | Digis: %s | %s |"
                   % (ax.destination, ax.source, ax.digipeaters, ax.info))


#
#   Take in frames from build_frames, and then combine them into one
#   audio signal, then send them to get_data
#
def build_sig(FRAMES):
    sig = b''.join(FRAMES)
    sig = np.frombuffer(sig, dtype="int16")
    get_data(sig)


#
#   Takes raw audio data from audio_decode
#
#   If the level is above "SENSITIVITY" (we are receiving something)
#   then wait for the transmission to stop, and try to detect something in it
#
def build_frames(conn, pipe):
    FRAMES = []
    receiving = False
    while True:
        if conn.poll():
            frame = conn.recv()
            blame = np.frombuffer(frame, dtype="int16")
            if max(blame) > SENSITIVITY:
                receiving = True
                FRAMES.append(frame)
            else:
                receiving = False
        if not receiving and len(FRAMES) > 0:
            build_sig(FRAMES)
            FRAMES = []

    conn.close()


#
#   This takes audio input from the computer's default sound input
#   and sends it to a pipe for build_frames to run on.
#   Runs on it's own thread so it can constantly take in input.
#
def audio_decode(conn):
    py_aud = pyaudio.PyAudio()

    stream = py_aud.open(format=FORMAT,
                         channels=CHANNELS,
                         rate=RATE,
                         input=True,
                         frames_per_buffer=CHUNK)
    while True:
        conn.send(stream.read(CHUNK, False))

    conn.close()
    stream.stop_stream()
    stream.close()
    py_aud.terminate()


#
#   This starts the audio input handling and builds the different threads
#
if __name__ == '__main__':
    aud_receive, aud_send = Pipe(False)
    cmd_pipe, frame_pipe = Pipe()

    audio = Process(target=audio_decode, args=(aud_send,))
    frames = Process(target=build_frames, args=(aud_receive, frame_pipe,))
    audio.start()
    frames.start()

    console.STACetShell(cmd_pipe).cmdloop()

    sock.close()

    aud_receive.close()
    aud_send.close()
    audio.terminate()
    frames.terminate()
    time.sleep(.3)
    audio.close()
    frames.close()
