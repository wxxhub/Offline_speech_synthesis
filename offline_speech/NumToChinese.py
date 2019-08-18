#coding:utf-8
import re

NUM_DICT = {'1':'一', '2':'二', '3':'三', '4':'四', '5':'五', '6':'六', '7':'七', '8':'八', '9':'九', '0':'零', }
INDEX_DICT = {1:'', 2:'十', 3:'百', 4:'千', 5:'万', 6:'十', 7:'百', 8:'千', 9:'亿'}

def __encode(num):
    nums = list(num)
    nums_index = [x for x in range(1, len(nums)+1)][-1::-1]

    chinese = ''
    for index, item in enumerate(nums):
        chinese = "".join((chinese, NUM_DICT[item], INDEX_DICT[nums_index[index]]))

    chinese = re.sub("零[十百千零]*", "零", chinese)
    chinese = re.sub("零万", "万", chinese)
    chinese = re.sub("亿万", "亿零", chinese)
    chinese = re.sub("零零", "零", chinese)
    chinese = re.sub("零\\b" , "", chinese)

    return chinese

def numToChinese(input_str):
    num = re.search(r'([0-9]+)', input_str)
    while num:
        num_str = num.group()
        num_chinese = __encode(num_str)
        input_str = input_str.replace(num_str, num_chinese)
        num = re.search(r'([0-9]+)', input_str)
        pass
    return input_str
    pass