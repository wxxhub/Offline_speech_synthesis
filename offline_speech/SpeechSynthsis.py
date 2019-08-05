#coding=utf-8

from pypinyin import pinyin, Style
from pypinyin.style import register
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
        pinyins = pinyin(sentence, style=Style.TONE2)

        play_sentence = []
        for pin_yin in pinyins:
            tone = re.sub(u"([^\u0030-\u0039])", "", pin_yin[0])
            pronounce = re.sub(u"([^\u0061-\u007a])", "", pin_yin[0])
            if pronounce == '':
                self.to_audio.append(play_sentence)
                play_sentence = []
            else:
                play_sentence.append(pronounce + tone)
        pass
    
    @classmethod
    def setFile(self, voice_file, cache_file):
        self.to_audio.setFile(voice_file, cache_file)
        pass

    @classmethod
    def dataEmpty(self):
        return self.to_audio.dataEmpty()

    @classmethod
    def close(self):
        self.to_audio.close()