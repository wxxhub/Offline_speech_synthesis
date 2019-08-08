#coding=utf-8

import sys
from time import ctime,sleep
from offline_speech.SpeechSynthsis import SpeechSynthsis

def main():
    # SpeechSynthsis.setFile("test", "test")  #change file path
    SpeechSynthsis.append("音频重置重要,上山打老虎老虎打不到打到小松鼠松鼠有几只,一二三四五，五只小松鼠")
    i = 0
    while True:
        i = i + 1
        if i == 6:
            SpeechSynthsis.reset()
            SpeechSynthsis.append("音频重置,这是新的音频")
        sleep(1)

        if i > 10 and SpeechSynthsis.dataEmpty():
            break
        pass
    SpeechSynthsis.close()
    print ('finished')
    return

if __name__ == '__main__':
    main()
