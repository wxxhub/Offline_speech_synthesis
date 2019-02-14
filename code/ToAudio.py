#coding=utf-8

import pygame
import time
from pydub import AudioSegment
from time import ctime,sleep
import threading
import os

pygame.mixer.init()

class ToAudio:
    thread_num = 0

    def __init__(self):
        # create cache file
        if not os.path.exists('../cache'):
            os.mkdir('../cache')

    @classmethod
    def speechSynthesis(self, sentence, num):
        # print ('test')
        t = threading.Thread(target=self.speechSynthesisThread, args=(sentence,num))
        t.setDaemon(False)
        t.start()
        sleep(1)

    @classmethod
    def speechSynthesisThread(self, sentence, num):
        # print ('start synthesis...')
        print (sentence)
        size = len(sentence)
        voices = False
        file_name = '../cache/voices'+str(num)+'.wav'
        for word in sentence:
            pronounce = AudioSegment.from_mp3('../voice/'+word+'.mp3')
            if voices == False:
                voices = pronounce
            else:
                voices = voices + pronounce 
        
        voices.export(file_name, format="wav")
        # print ("playing...")
        while True:
            if num == self.thread_num:
                track = pygame.mixer.music.load(file_name)
                pygame.mixer.music.play()
                # time.sleep(size)
                while pygame.mixer.music.get_busy():
                    sleep(1)
                self.thread_num = self.thread_num + 1
                break