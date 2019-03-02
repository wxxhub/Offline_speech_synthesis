import re
import hanint

def numToChinese(input_str):
    num = re.search(r'([0-9]+)', input_str)
    while num:
        num_str = num.group()
        num_chinese = hanint.encode(int(num_str))
        input_str = input_str.replace(num_str, num_chinese)
        num = re.search(r'([0-9]+)', input_str)
        pass
    return input_str
    pass