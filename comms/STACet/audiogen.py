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
#   audiogen.py
#       Deal with playing audio and things related to that.
#       This is a cut-down, modified, and updated version of the package
#       Audiogen, https://github.com/casebeer/audiogen
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
# Imports
import var

from functools import reduce
import itertools
import struct

try:
    import pyaudio
    pyaudio_loaded = True
except ImportError:
    pyaudio_loaded = False

# --------------------------------------------------------------------------
# Variable setup

SAMPLE_WIDTH = 2
RATE = var.RATE
FRAME_RATE = RATE
BUFFER_SIZE = 100000

# --------------------------------------------------------------------------

#
# audiogen play: Plays a waveform
#
def play(channels, blocking=True, raw_samples=False):
    if not pyaudio_loaded:
        raise Exception("Soundcard playback requires PyAudio. Install with `pip install pyaudio`.")
    channel_count = 1
    wavgen = wav_samples(channels, raw_samples=raw_samples)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(SAMPLE_WIDTH),
        channels=channel_count,
        rate=FRAME_RATE,
        output=True,
        stream_callback=_pyaudio_callback(wavgen) if not blocking else None
    )
    if blocking:
        try:
            for chunk in buffer(wavgen, 1024):
                if chunk == b"":
                    break
                stream.write(chunk)
        except StopIteration:
            pass
        except Exception:
            raise
        finally:
            if not stream.is_stopped():
                stream.stop_stream()
            try:
                stream.close()
            except Exception:
                pass
    else:
        return stream


#
# audiogen wav samples: provide the wav samples
#
def wav_samples(channels, sample_width=SAMPLE_WIDTH, raw_samples=False):
    channels = (channels,)
    if not raw_samples:
        # we have audio waveforms, so sample/pack them first
        channels = sample_all(channels, width=sample_width)
    return interleave(channels)


#
# audiogen sample:
#
def sample(generator, min=-1, max=1, width=SAMPLE_WIDTH):
    '''Convert audio waveform generator into packed sample generator.'''
    # select signed char, short, or in based on sample width
    fmt = { 1: '<B', 2: '<h', 4: '<i' }[width]
    return (struct.pack(fmt, int(sample)) for sample in \
            normalize(hard_clip(generator, min, max), \
                      min, max, -2**(width * 8 - 1), 2**(width * 8 - 1) - 1))

#
# audiogen sample all:
#
def sample_all(generators, *args, **kwargs):
    '''Convert list of audio waveform generators into list of packed sample generators.'''
    return [sample(gen, *args, **kwargs) for gen in  generators]


#
# audiogen interleave:
#
def interleave(channels):
    while True:
        try:
            yield b"".join([next(channel) for channel in channels])
        except StopIteration:
            yield b""
            break


#
# adudiogen _pyaudio_callback:
#
def _pyaudio_callback(wavgen):
    def cb(a, frame_count, b, c):
        data = bytearray()
        try:
            for i in range(frame_count):
                data.extend(next(wavgen))
        except StopIteration:
            if len(data) == 0:
                return "", pyaudio.paComplete
        return str(data), pyaudio.paContinue
    return cb


#
#
#
def buffer(stream, buffer_size=BUFFER_SIZE):
    '''
    Buffer the generator into byte strings of buffer_size samples

    Return a generator that outputs reasonably sized byte strings
    containing buffer_size samples from the generator stream.

    This allows us to outputing big chunks of the audio stream to
    disk at once for faster writes.
    '''
    i = iter(stream)

    return iter(lambda: b"".join(itertools.islice(i, buffer_size)), "")


#
# audiogen util hard_clip
#
def hard_clip(generator, min=-1, max=1):
    while True:
        try:
            sample = next(generator)
        except StopIteration:
            break
        if sample > max:
            yield max
        elif sample < min:
            yield min
        else:
            yield sample


#
# audiogen util normalize
#
def normalize(generator, min_in=0, max_in=256, min_out=-1, max_out=1):
    scale = float(max_out - min_out) / (max_in - min_in)
    return ((sample - min_in) * scale + min_out for sample in generator)


#
# audiogen util constant
#
def constant(value):
    while True:
        yield value


#
# audiogen util vector reduce
#
def vector_reduce(op, generators):
    while True:
        yield reduce(op, [next(g) for g in generators])


#
# audiogen util vector reduce 1
#
def vector_reduce1(op, generators):
    while True:
        try:
            yield reduce(op, [next(g) for g in generators])
        except StopIteration:
            break


#
# audiogen util multiply
#
def multiply(*generators):
    return vector_reduce1(lambda a, b: a * b, generators)


#
# provide a way to produce a silent audio waveform
#
def silence(seconds=None):
    if seconds != None:
        for i in range(int(FRAME_RATE * seconds)):
            yield 0
    else:
        while True:
            yield 0
