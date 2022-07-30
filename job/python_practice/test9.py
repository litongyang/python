# -*- coding: utf-8 -*-
import random
import string
import re


def letter_cnt():
    s = "sw7JD$29VKLV$%GE[P,.H/?"
    b, l, n, x = 0, 0, 0, 0  # b大写字母数目 l小写字母数目 n数字数目 其他
    for i in s:
        if i.islower():
            l += 1
        elif i.isupper():
            b += 1
        elif i.isdigit():
            n += 1
        else:
            x += 1
    print "小写字母个数", b
    print "小写字母个数", l
    print "小写字母个数", n
    print "其他个数", x




def encrypt():
    """
    使用以下规则，将这段文字转为密文。密码规则：将英文字母替换为字母表顺序后的第7个字母，若超出字母表范围则从头开始。
    :return:
    """
    str1 = "In the flood of darkness, hope is the light. It brings comfort, faith, and confidence. It gives us guidance when we are lost, and gives support when we are afraid. And the moment we give up hope, we give up our lives. The world we live in is disintegrating into a place of malice and hatred, where we need hope and find it harder. In this world of fear, hope to find better, but easier said than done, the more meaningful life of faith will make life meaningfu"
    list_2, list_3 = [], []
    list_1 = re.findall(r'[^\W\d_]+|\d+', str1)
    for i in list_1:
        try:
            list_2.append(5 * int(i))
        except ValueError:
            list_2.append(i)
    for i in list_2:
        list_3.append(str(i))  # 这个步骤是因为字符串和整数是无法进行join()操作的,所以是整数进行字符串化的操作
    del list_2[:]
    str1 = ''.join(list_3)
    del list_3[:]
    for i in str1:
        list_3.append(i)
    for i in list_3:
        if 65 <= ord(i) <= 90:
            s = ord(i) + 7
            if s <= 90:
                list_2.append(chr(s))
            else:
                s = s - 90 + 65 - 1
                list_2.append(chr(s))
        elif 97 <= ord(i) <= 122:
            s = ord(i) + 7
            if s <= 122:
                list_2.append(chr(s))
            else:
                s = s - 122 + 97 - 1
                list_2.append(chr(s))
        else:
            list_2.append(i)
    str2 = ''.join(list_2)
    print  str2



def firt_letter():
    """
    用户输入一个英文句子，将英文的单词首字母大写，其它位置上的字母小写后输出。并统计该句子中共包含多少个单词
    :return:
    """
    str = "my python is world!"
    str1 = str.split(' ')
    str_val = str.title()
    print "首字母大写：", str_val
    print "单词数：", len(str1)


def random_letter():
    """
    随机生成100个小写字母组成的列表
    :return:
    """
    list = []
    for i in range(0, 100):
        list.append(random.choice(string.ascii_lowercase))
    print "随机生成100个小写字母组成的列表:", list


if __name__ == '__main__':
    # letter_cnt()
    # encrypt()
    # firt_letter()
    random_letter()
