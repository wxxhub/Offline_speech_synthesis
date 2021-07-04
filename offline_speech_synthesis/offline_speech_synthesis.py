import threading
from time import sleep
import os
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
    enable_ = True

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

        self.speech_queue_.put(os.path.join(self.speech_synthsis.getCacheFile(), file_name))
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
        self.speech_synthsis.reset()
        pass

    @classmethod
    def playing(self):
        return self.playing_

    @classmethod
    def close(self):
        self.enable_ = False
        self.speech_queue_.put("")
        pass


    @classmethod
    def __playThread(self):
        while self.enable_:
            file_name = self.speech_queue_.get()
            if file_name:
                self.__playSpeech(file_name)
        pass

    @classmethod
    def __playSpeech(self, file_name):
        self.playing_ = True
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()

        while not self.resetting_ and pygame.mixer.music.get_busy():
            sleep(0.1)

        pygame.mixer.music.stop()

        self.playing_ = False
        pass
