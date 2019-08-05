#coding=utf-8

import sys
from time import ctime,sleep
from offline_speech.SpeechSynthsis import SpeechSynthsis

def main():
    # SpeechSynthsis.setFile("test", "test")  #change file path
    SpeechSynthsis.append("一二三四五,上山打老虎,老虎打不到,打到小松鼠,松鼠有几只,让我数一数,一二三四五，五只小松鼠")
    while not SpeechSynthsis.dataEmpty():
        sleep(1)
        pass
    SpeechSynthsis.close()
    print ('finished')
    return

if __name__ == '__main__':
    main()
