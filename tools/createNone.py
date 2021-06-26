import wave
import numpy as np
import struct
import matplotlib.pyplot as plt

# sample/every second
framerate = 44100
# bytes needed every sample
sample_width = 2
duration = 5
frequency = 2000
volume = 1000
x = np.linspace(0, duration, num=duration*framerate)
y = np.sin(2 * np.pi * frequency * x) * volume
# 将波形数据转换成数组
sine_wave = y
#save wav file
wf = wave.open("sine.wav", 'wb')
wf.setnchannels(1)
wf.setframerate(framerate)
wf.setsampwidth(sample_width)
for i in sine_wave:
    data = struct.pack('<h', int(0))
    wf.writeframesraw(data)
wf.close()

