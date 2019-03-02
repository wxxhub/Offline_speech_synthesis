#coding=utf-8

import sys
from SpeechSynthsis import *

def main():
    synthesis("警报，123号电机过载")
    while isRunning():
        sleep(1)
    print ('finished')
    return

if __name__ == '__main__':
    main()
	
