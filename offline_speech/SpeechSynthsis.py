#coding=utf-8

from pypinyin import pinyin, Style
from pypinyin.style import register
import re
import numpy as np
from offline_speech.NumToChinese import numToChinese

from offline_speech.ToAudio import ToAudio
from time import ctime,sleep

class SpeechSynthsis:

    @classmethod
    def synthesis(self, sentence):
        print (sentence)
        sentence = numToChinese(str(sentence))
        pinyins = pinyin(sentence, style=Style.TONE2)
        print (pinyins)
        self.__depart(pinyins)
        pass
    
    @classmethod
    def setFile(self, voice_file, cache_file):
        ToAudio.setFile(voice_file, cache_file)
        pass

    @classmethod
    def __depart(self, pinyins):
        num = 0
        sentence = []
        for pinyin in pinyins:
            tone = re.sub(u"([^\u0030-\u0039])", "", pinyin[0])
            pronounce = re.sub(u"([^\u0061-\u007a])", "", pinyin[0])
            if pronounce == '':
                # sentence.append('null')
                ToAudio.speechSynthesis(sentence, num)
                num = num + 1
                sentence = []
            else:
                sentence.append(pronounce + tone)

        ToAudio.speechSynthesis(sentence, num)
        pass

    @classmethod
    def isRunning(self):
        return ToAudio.isRunning()
        pass
