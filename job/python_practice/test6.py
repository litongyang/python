# -*- coding: utf-8 -*-
import random
import string


def input_str():
    """
    输入一个字符串，将该字符串中下标为偶数的字符组成新串并通过字符串格式化方式显示
    :return:
    """
    x = raw_input("请输入一个字符串：")
    y = x[::2]
    print "下标为偶数的字符组成的新串为：{}".format(y)


def letter_15():
    """
    生成一个15个不重复的大小写字母组成的列表。
    :return:
    """
    list1 = []
    while len(list1) <= 15:
        x = random.choice(string.ascii_letters)
        if x not in list1:
            list1.append(x)
    print "15个不重复的大小写字母组成的列表为：", list1


def english_word(word):
    """
    用户输入一个英文句子（不包含标点符号），统计该句子中包含多少个单词，并将每一个单词拆分放入列表，并输出列表。
    :param word:
    :return:
    """

    count = len(word.split())
    print "单词个数：", count


def mean_10():
    """
    从键盘输入10个数字，用“，”分隔。计算它们的平均值并输出（保留2位小数）
    :return:
    """
    x = eval(raw_input('请输入10个数，以‘,’隔开：'))
    s = sum(x)
    l = len(x)
    avg = s / l
    print(round(avg, 2))


def letter_cnt():
    """
    统计这段文字中每个英文字母出现的次数，不区分大小写。
    :return:
    """
    a = "Unfortunately, as a society we have bought into these misguided messagesand have come to believe that spendingmoney on certain items will bring us fame,fortune, happiness, beauty, or popularity.We end up using money as a crutch toprovide us with something we ultimatelymust find within ourselves. As we becomecaught up in this charade, we trade precious hours of our lives trying to earnthe money we have been taught to covetSO much."
    b = list(a.lower())  # 将输入的字符全部转换为小写字母
    c = {}  # 建立一个空字典
    for i in b:  # for循环遍历出结果
        c[i] = b.count(i)
    print c


if __name__ == '__main__':
    # input_str()
    # letter_15()
    # english_word("hello world  weqw")
    # mean_10()
    letter_cnt()