# -*- coding: utf-8 -*-

def inputStr():
    """
    输入名字
    :return:
    """
    str1 = raw_input("请输入一个字符串：")
    str = str1 + "，欢迎你进入python程序世界"
    print str


if __name__ == '__main__':
    inputStr()
