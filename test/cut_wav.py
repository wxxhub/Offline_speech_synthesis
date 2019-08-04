#coding:utf-8
import os
import wave

import numpy as np

wave_path = "wav/"
cut_wave_path = "cut_wav/"

def change(wave_data):

    max_data = 0
    for data in wave_data:
        if data > max_data:
            max_data = data

    wave_data = wave_data * 40000 // max_data

def cutWav(origion_wav, cut_wav):
    params = origion_wav.getparams()
    channels, samp_width, fps, frames = params[:4]
    str_data = origion_wav.readframes(frames)
    wave_data = np.fromstring(str_data, dtype = np.short)

    change(wave_data)

    i = 0
    for data in wave_data:
        if data <= 500 and data >= -500:
            i = i + 1
        else:
            break
    # print (wave_data)
    cut_data = wave_data[i:]

    size = 0

    for data in cut_data:
        if data >= 500 or data <= -500:
            size = size + 1

    t = 0
    
    for data in cut_data:
        t = t + 1
        if t // 1.5 == 0:
            size = size + 1
    # print (cut_data)

    cut_data = cut_data[0:size]

    cut_wav.setnchannels(channels)
    cut_wav.setsampwidth(samp_width)
    cut_wav.setframerate(fps)
    cut_wav.writeframes(cut_data.tostring())

    # print (cut_data)
    print (len(cut_data))
    origion_wav.close()
    cut_wav.close()
    pass

def main():
    files = os.listdir(wave_path)
    for file_name in files:
        origion_wav = wave.open(wave_path+file_name, "rb")
        cut_wav = wave.open(cut_wave_path+file_name, "wb")
        
        cutWav(origion_wav, cut_wav)
        print (file_name)
        # break
    pass

if __name__ == "__main__":
    main()
