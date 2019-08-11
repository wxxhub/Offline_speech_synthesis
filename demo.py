#coding=utf-8

import sys
from time import ctime, sleep

from offline_speech.SpeechSynthsis import SpeechSynthsis

def main():
    synthsis = SpeechSynthsis(15500)

    ##### reset test
    synthsis.append("音频重置重要,123.78.88,上山打老虎老虎打不到打到小松鼠松鼠有几只,一二三四五，五只小松鼠")
    i = 0 
    while True:
        i = i + 1
        if i == 11:
            synthsis.reset()
            print ("reset")
            synthsis.append("音频重置,这是新的音频")
        sleep(1)
        
        if synthsis.playing():
            print ('playing...')

        if i > 15 and synthsis.dataEmpty():
            break
        pass

    #### performance test

    # synthsis.append("这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, ")
    # i = 0
    # while True:
    #     if i < 100:
    #         i += 1
    #         synthsis.append("这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试,")
    #     sleep(1)

    synthsis.close()
    print ('finished')

    return

if __name__ == '__main__':
    main()
