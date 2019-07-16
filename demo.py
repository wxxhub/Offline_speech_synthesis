#coding=utf-8

import sys
from time import ctime,sleep
from offline_speech.SpeechSynthsis import SpeechSynthsis

def main():
    # SpeechSynthsis.setFile("test", "test")  #change file path
    # SpeechSynthsis.synthesis("孔子曰，123号电机过载,真是费劲呀，哈哈哈,3,2,1")
    SpeechSynthsis.synthesis("一二三四五上山打老虎老虎打不到打到小松鼠松鼠有几只让我数一数一二三四五，五只小松鼠")
    # SpeechSynthsis.synthesis("下雨天了怎么办")
    while SpeechSynthsis.isRunning():
        sleep(1)
        pass
    print ('finished')
    return

if __name__ == '__main__':
    main()
