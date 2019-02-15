#coding=utf-8

from pypinyin import pinyin, Style
from pypinyin.style import register
import re
import numpy as np

from ToAudio import ToAudio
from time import ctime,sleep

def depart(pinyins):
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

def synthesis(sentence):
    pinyins = pinyin(sentence, style=Style.TONE2)
    print (pinyins)
    depart(pinyins)

def isRunning():
    return ToAudio.isRunning()
