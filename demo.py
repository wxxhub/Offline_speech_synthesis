#coding=utf-8

import sys
from time import ctime,sleep
from offline_speech.SpeechSynthsis import SpeechSynthsis

def main():
    # SpeechSynthsis.setFile("test", "test")  #change file path
    SpeechSynthsis.synthesis("警报，123号电机过载")
    while SpeechSynthsis.isRunning():
        sleep(1)
        pass
    print ('finished')
    return

if __name__ == '__main__':
    main()
