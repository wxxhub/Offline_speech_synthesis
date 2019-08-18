#coding=utf-8

import pygame.mixer
import time
import wave
from time import sleep
import threading
import os

try:
    from queue import Queue
except:
    from Queue import Queue

lock = threading.Lock()
thread_num_lock = threading.Lock()

class ToAudio:
    play_num_ = 0
    cache_file_num = 0
    cache_file_ = "cache"
    voice_file_ = "wav"
    sentence_queue_ = Queue()
    play_thread_ = None
    enable_ = False
    playing_ = False
    resetting = False
    max_frequency = 22050
    min_frequency = 10000

    @classmethod
    def __init__(self, goal_frequency = 16000):
        if goal_frequency < self.min_frequency:
            goal_frequency = self.min_frequency
        elif goal_frequency > self.max_frequency:
            goal_frequency = self.max_frequency
            
        pygame.mixer.init(frequency=goal_frequency, channels=1) 

        # create cache file
        self.enable_ = True
        if not os.path.exists(self.cache_file_):
            os.mkdir(self.cache_file_)

        self.play_thread_ = threading.Thread(target=self.__playThread)
        self.play_thread_.start()
        pass

    @classmethod
    def __del__(self):
        self.play_thread_.join()
        pass
    
    @classmethod
    def reset(self):
        self.resetting = True
        self.sentence_queue_.queue.clear()
        self.play_num_ = 0
        self.cache_file_num = 0
        while pygame.mixer.music.get_busy():
            pass
        self.resetting = False
        pass

    @classmethod
    def setFile(self, voice_file, cache_file):
        self.cache_file_ = cache_file
        self.voice_file_ = voice_file
        pass

    @classmethod
    def printFile(self):
        print ("cache_file: "+self.cache_file_)
        print ("voice_file: "+self.voice_file_)
        pass
    
    @classmethod
    def append(self, sentence):
        self.sentence_queue_.put(sentence)
        # print (sentence)
        pass

    @classmethod
    def dataEmpty(self):
        if self.play_num_ > 0:
            return False

        return self.sentence_queue_.empty()

    @classmethod
    def playing(self):
        return self.playing_

    @classmethod
    def close(self):
        self.enable_ = False
    
    @classmethod
    def __playThread(self):
        while self.enable_:
            # resetting and not enable break
            while not self.resetting and self.enable_:
                if not self.sentence_queue_.empty():
                    sentence = self.sentence_queue_.get()
                    result, file_name = self.__synthesis(sentence)
                    if result:
                        # 如果等待播放的数量大于一,等待
                        while self.play_num_ > 1 and not self.resetting and self.enable_:
                            sleep(0.1)
                        
                        self.__playSpeech(file_name)
                sleep(0.1)
            sleep(0.1)
        pass

    @classmethod
    def __synthesis(self, sentence):
        datas = []
        success = False
        for word in sentence:
            wav_file = self.voice_file_+'/'+word+'.wav'
            # print (wav_file)
            if not os.path.exists(wav_file):
                print (wav_file + " not exists, please add")
                continue

            read_wave = wave.open(wav_file, 'r')

            if not success:
                params = read_wave.getparams()

            data = read_wave.readframes(read_wave.getnframes())

            datas.append(data)
            read_wave.close()
            success = True
            

        if success:
            file_name = self.cache_file_+'/voices'+str(self.cache_file_num)+'.wav'
            self.cache_file_num = self.cache_file_num + 1
            out_put_wave = wave.open(file_name,  'w')
            out_put_wave.setparams(params)
            for data in datas:
                out_put_wave.writeframes(data)
            out_put_wave.close()
            return True, file_name
        
        return False, ''
            

    @classmethod
    def __playSpeech(self, file_name):
        self.playing_ = True
        self.play_num_ = self.play_num_ + 1
        track = pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()

        while not self.resetting and pygame.mixer.music.get_busy():
            sleep(0.1)

        pygame.mixer.music.stop()
        if self.play_num_ != 0:
            self.play_num_ = self.play_num_ - 1

        self.playing_ = False
        pass