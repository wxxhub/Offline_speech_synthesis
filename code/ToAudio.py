#coding=utf-8

import pygame
import time
from pydub import AudioSegment
from time import ctime,sleep
import threading
import os

pygame.mixer.init()

class ToAudio:
    running_thread_num = 0
    thread_num = 0

    def __init__(self):
        # create cache file
        if not os.path.exists('../cache'):
            os.mkdir('../cache')

    @classmethod
    def speechSynthesis(self, sentence, num):
        # print ('test')
        while True:
            if self.running_thread_num - num < 2:
                t = threading.Thread(target=self.speechSynthesisThread, args=(sentence,num))
                t.setDaemon(False)
                t.start()
                self.thread_num = self.thread_num + 1 # sum of thread
                sleep(0.1)
                break
            sleep(1)

    @classmethod
    def speechSynthesisThread(self, sentence, num):
        # print ('start synthesis...')
        # print (sentence)
        size = len(sentence)
        voices = False
        # print ('test1',num)
        file_name = '../cache/voices'+str(num)+'.wav'
        for word in sentence:
            pronounce = AudioSegment.from_mp3('../voice/'+word+'.mp3')
            if voices == False:
                voices = pronounce
            else:
                voices = voices + pronounce 
        voices.export(file_name, format="wav")
        # print ('test2',num)
        self.playSpeech(file_name, num)
    
    @classmethod
    def playSpeech(self, file_name, num):
        # print ("playing...")
        while True:
            if num == self.running_thread_num:
                track = pygame.mixer.music.load(file_name)
                pygame.mixer.music.play()
                # time.sleep(size)
                while pygame.mixer.music.get_busy():
                    sleep(0.1)
                self.running_thread_num = self.running_thread_num + 1
                break
            else:
                sleep(0.5)

    @classmethod
    def isRunning(self):
        if (self.running_thread_num == self.thread_num):
            return False
        else:
            running_thread_num = 0
            thread_num = 0
            return True