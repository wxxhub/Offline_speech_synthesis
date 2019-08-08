from ChineseTone import *
import re
import hanint

print (PinyinHelper.convertToPinyinFromSentence('了解了', pinyinFormat=PinyinFormat.WITH_TONE_NUMBER))

def numToChinese(input_str):
    num = re.search(r'\d+.\d+', input_str)
    while num:
        num_str = num.group()
        num_chinese = hanint.encode(int(num_str))
        input_str = input_str.replace(num_str, num_chinese)
        num = re.search(r'([0-9]+)', input_str)
        pass
    return input_str

print (numToChinese('123.46'))