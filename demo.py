#coding=utf-8

from time import sleep
from offline_speech_synthesis.offline_speech_synthesis import OfflineSpeechSynthesis
import _locale

_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])
goal_frequency = 20000
def main():
    synthsis = OfflineSpeechSynthesis(goal_frequency, 'wav', 'cache')

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
        
        if i == 15:
            print ("add")
            synthsis.append("这是新加的音频")

        if i > 20 and not synthsis.playing():
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
