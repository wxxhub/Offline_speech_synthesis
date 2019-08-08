#coding=utf-8

from ChineseTone import *
import re
import numpy as np
from offline_speech.NumToChinese import numToChinese

from offline_speech.ToAudio import ToAudio
from time import ctime,sleep

class SpeechSynthsis:
    to_audio = ToAudio()
    @classmethod
    def append(self, sentence):
        sentence = numToChinese(str(sentence))
        # pinyins = pinyin(sentence, style=Style.TONE2, heteronym=True)
        pinyins = PinyinHelper.convertToPinyinFromSentence(sentence, pinyinFormat=PinyinFormat.WITH_TONE_NUMBER)

        play_sentence = []
        for pin_yin in pinyins:
            tone = re.sub(u"([^\u0030-\u0039])", "", pin_yin)
            pronounce = re.sub(u"([^\u0061-\u007a])", "", pin_yin)
            if pronounce == '':
                self.to_audio.append(play_sentence)
                play_sentence = []
            else:
                play_sentence.append(pronounce + tone)
        
        self.to_audio.append(play_sentence)
        pass
    
    @classmethod
    def setFile(self, voice_file, cache_file):
        self.to_audio.setFile(voice_file, cache_file)
        pass

    @classmethod
    def dataEmpty(self):
        return self.to_audio.dataEmpty()
    
    @classmethod
    def reset(self):
        self.to_audio.reset()
        pass

    @classmethod
    def close(self):
        self.to_audio.close()