#coding=utf-8

import re
from time import ctime, sleep

import numpy as np
from ChineseTone import *
from offline_speech.NumToChinese import numToChinese
from offline_speech.ToAudio import ToAudio


class SpeechSynthsis:
    punctuation = " ,！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
    @classmethod
    def __init__(self, goal_frequency):
        self.to_audio = ToAudio(goal_frequency)

    @classmethod
    def append(self, sentence):
        split_sentences = re.split(u"[%s]+"%self.punctuation, sentence)
  
        for split_sentence in split_sentences:
            split_sentence = numToChinese(str(split_sentence))
            pinyins = PinyinHelper.convertToPinyinFromSentence(split_sentence, pinyinFormat=PinyinFormat.WITH_TONE_NUMBER)

            play_sentence = []
            
            for pin_yin in pinyins:
                tone = re.sub(u"([^\u0030-\u0039])", "", pin_yin)
                pronounce = re.sub(u"([^\u0061-\u007a])", "", pin_yin)
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
    def playing(self):
        return self.to_audio.playing_

    @classmethod
    def close(self):
        self.to_audio.close()