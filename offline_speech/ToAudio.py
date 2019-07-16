#coding=utf-8

import pygame.mixer
import time
import wave
from time import sleep
import threading
import os

lock = threading.Lock()
thread_num_lock = threading.Lock()
pygame.mixer.init(16000) 
class ToAudio:
    running_thread_num_ = 0
    thread_num_ = 0
    cache_file_ = "cache"
    voice_file_ = "woman_wav"

    def __init__(self):
        # create cache file
        if not os.path.exists(self.cache_file_):
            os.mkdir(self.cache_file_)
        pass

    @classmethod
    def speechSynthesis(self, sentence, num):
        # print ('test')
        while True:
            if self.running_thread_num_ - num < 2:
                t = threading.Thread(target=self.__speechSynthesisThread, args=(sentence,num))
                t.start()
                thread_num_lock.acquire()
                self.thread_num_ = self.thread_num_ + 1 # sum of thread
                thread_num_lock.release()
                sleep(0.1)
                break
            sleep(1)
        pass

    @classmethod
    def setFile(self, voice_file, cache_file):
        self.cache_file_ = cache_file
        self.voice_file_ = voice_file
        pass

    @classmethod
    def __speechSynthesisThread(self, sentence, num):
        size = len(sentence)
        datas = []
        success = False
        for word in sentence:
            wav_file = self.voice_file_+'/'+word+'.wav'
            print (wav_file)
            if not os.path.exists(wav_file):
                print (wav_file + " not exists, please add")
                continue

            read_wave = wave.open(wav_file, 'r')
            datas.append([read_wave.getparams(), read_wave.readframes(read_wave.getnframes())] )
            read_wave.close()
            success = True

        if success:
            file_name = self.cache_file_+'/voices'+str(num)+'.wav'
            out_put_wave = wave.open(file_name,  'w')
            out_put_wave.setparams(datas[1][0])
            print (datas[0][0])
            for data in datas:
                out_put_wave.writeframes(data[1])
            
            out_put_wave.close()
            self.__playSpeech(file_name, num)
        else:
            thread_num_lock.acquire()
            self.thread_num_ = self.thread_num_-1
            thread_num_lock.release()
    
    @classmethod
    def __pushData(out_put_wave, data):
        pass

    @classmethod
    def __playSpeech(self, file_name, num):
        # print ("playing...")
        while True:
            if num == self.running_thread_num_:
                track = pygame.mixer.music.load(file_name)
                pygame.mixer.music.play()
                # time.sleep(size)
                while pygame.mixer.music.get_busy():
                    sleep(0.1)
                self.running_thread_num_ = self.running_thread_num_ + 1
                break
            else:
                sleep(0.5)
        pass

    @classmethod
    def isRunning(self):
        if (self.running_thread_num_ >= self.thread_num_):
            return False
        else:
            running_thread_num = 0
            thread_num = 0
            return True
        pass

    @classmethod
    def printFile(self):
        print ("cache_file: "+self.cache_file_)
        print ("voice_file: "+self.voice_file_)
        pass