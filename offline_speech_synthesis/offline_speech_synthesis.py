import threading
from time import ctime, sleep

import pygame.mixer
from speech_synthesis.SpeechSynthsis import SpeechSynthsis

try:
    from queue import Queue
except:
    from Queue import Queue

class OfflineSpeechSynthesis:
    speech_queue_ = Queue()
    play_thread_ = None
    resetting_ = False
    playing_ = False

    @classmethod
    def __init__(self, goal_frequency, voice_file, cache_file = None):
        self.speech_synthsis = SpeechSynthsis(goal_frequency)

        if  not cache_file:
            cache_file = 'cache'

        self.speech_synthsis.setFile(voice_file, cache_file)
        pygame.mixer.init()

        self.play_thread_ = threading.Thread(target=self.__playThread)
        self.play_thread_.start()
        pass

    @classmethod
    def __del__(self):
        self.play_thread_.join()
        pass

    @classmethod
    def append(self, content):
        ok, file_name = self.speech_synthsis.synthesis(content)
        
        if not ok:
            return ok, ""

        self.speech_queue_.put(file_name)
        return ok, file_name
        pass

    @classmethod
    def reset(self):
        self.resetting_ = True
        self.speech_queue_.queue.clear()
        self.play_num_ = 0
        self.cache_file_num = 0
        while pygame.mixer.music.get_busy():
            pass
        self.resetting_ = False
        pass
        pass

    @classmethod
    def playing(self):
        return self.playing_


    @classmethod
    def __playThread(self):
        while True:
            file_name = self.speech_queue_.get()
            self.__playSpeech(file_name)
        pass

    @classmethod
    def __playSpeech(self, file_name):
        self.playing_ = True
        track = pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()

        while not self.resetting_ and pygame.mixer.music.get_busy():
            sleep(0.1)

        pygame.mixer.music.stop()

        self.playing_ = False
        pass
