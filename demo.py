#coding=utf-8

import sys
from time import ctime, sleep

from offline_speech.SpeechSynthsis import SpeechSynthsis

def main():
    synthsis = SpeechSynthsis(15500)

    ##### reset test
    # SpeechSynthsis.append("音频重置重要,123.78.88, 上山打老虎老虎打不到打到小松鼠松鼠有几只,一二三四五，五只小松鼠")
    # i = 0
    # while True:
    #     i = i + 1
    #     if i == 10:
    #         SpeechSynthsis.reset()
    #         SpeechSynthsis.append("音频重置,这是新的音频")
    #     sleep(1)

    #     if i > 20 and SpeechSynthsis.dataEmpty():
    #         break
    #     pass

    #### performance test

    # SpeechSynthsis.append("这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, ")
    # i = 0
    # while True:
    #     if i < 100:
    #         i += 1
    #         SpeechSynthsis.append("这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试, 这是性能测试,")
    #     sleep(1)
    # SpeechSynthsis.close()
    # print ('finished')

    SpeechSynthsis.append("性能测试")
    while not SpeechSynthsis.dataEmpty():
        sleep(1)
    SpeechSynthsis.close()
    print ('finished')
    return

if __name__ == '__main__':
    main()
