import time
from pydub import AudioSegment
from audiolazy import *
from audiolazy.lazy_stream import Stream
from matplotlib import pyplot as plt # Or /"import pylab as plt"
import pyaudio
# form pyaudio import sHz
import wave
import sys

# voice_file = "../cache/voices0.wav"
# pronounce = AudioSegment.from_wav(voice_file)

# test = Stream(pronounce)
# rate = 44100
# a = Stream(2, -2, 1)
# b = Stream(3, 7, 5, 4)
# c = a + b
# print (c)
# print (a.take(15))
# print (b.take(15))
# print (c.take(15))
# print (test.take(15))
rate = 44100 # Sampling rate, in samples/second
s, Hz = sHz(rate) # Seconds and hertz
ms = 1e-3 * s
note1 = karplus_strong(440 * Hz) # Pluck "digitar" synth
note2 = zeros(300 * ms).append(karplus_strong(880 * Hz))
notes = (note1 + note2) * .5
sound = notes.take(int(2 * s)) # 2 seconds of a Karplus-Strong note
with AudioIO(True) as player: # True means "wait for all sounds to stop"
  player.play(sound, rate=rate)