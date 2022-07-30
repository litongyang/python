# -*- coding: utf-8 -*-

"""
提示用户输入字符串。将所输入的字符串，以及对应字符串的长度写入到exercise7_2.txt中
"""

with open('exercise7_2.txt','w') as f:
    s=raw_input("请输入一个字符串")
    f.write("输入的字符串是：" + str(s) +"\n"+ "字符串的长度是：" + str(len(s)))
    f.close()


