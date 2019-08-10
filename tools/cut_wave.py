#coding:utf-8
import os
import wave

wave_path = "../t/"
cut_wave_path = "../tt/"

import numpy as np


def cutWav(origion_wav, cut_wav):
    params = origion_wav.getparams()
    channels, samp_width, fps, frames = params[:4]
    str_data = origion_wav.readframes(frames)
    wave_datas = np.fromstring(str_data, dtype = np.short)

    find_start = False
    start = 0
    end = 0
    for data in wave_datas:
        if data != 0:
            end = end + 1
            find_start = True

        if not find_start:
            start = start + 1    

    if start - 10 > 0:
        start = start - 10
    else:
        start = 0
    
    if end + 10 < len(wave_datas):
        end = end + 10
    else:
        end = len(wave_datas)

    cut_data = wave_datas[start:end]
    cut_wav.setnchannels(channels)
    cut_wav.setsampwidth(samp_width)
    cut_wav.setframerate(fps)
    cut_wav.writeframes(cut_data.tostring())

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