# -*- coding: utf-8 -*-

import re
import string
import random


def s_first():
    """
    给定字符串"site sea suede sweet see kase sse ssee loses"，匹配出所有s开头，e结尾的单词
    :return:
    """
    str = "site sea suede sweet see kase sse ssee loses"
    r = r"\bs\S*e\b"
    a = re.findall(r, str)
    print "匹配出所有s开头，e结尾的单词", a


def special_characters():
    """
    生成15个包括10个字符的随机密码，密码中的字符只能是大小写字母、数字和特殊字符“@”、“$”、“#”、“&”、“_”、“~”构成。
    :return:
    """
    x = string.ascii_letters + string.digits + "@$#&_~"
    for i in range(15):
        print"随机密码" + str(i + 1) + ":"
        y = "".join([random.choice(x) for i in range(10)])
        print y


def phone():
    """
    给定列表x=["13915556234", "13025621456", "15325645124", "15202362459"]，检查列表中的元素是否为移动手机号码，这里移动手机号码的规则是：手机号码共11位数字；以13开头，后面跟4、5、6、7、8、9中的某一个；或者以15开头，后面跟0、1、2、8、9中的某一个。
    :return:
    """
    import re
    x = ["13915556234", "13025621456", "15325645124", "15202362459"]
    r = r'^(13[4-9]\d{8})|(15[01289]\d{8})$'
    print "符合这里移动手机号码规则的是："
    for i in x:
        if re.findall(r, i):
            print i


def single(t):
    """
    按单利计算
    :param t:
    :return:
    """
    sum=t*0.06*3
    print sum


def complex(t):
    """
    按复利计算
    :param t:
    :return:
    """
    sum=t*(1+0.06)**3-t
    print sum


def prime_number():
    """
    判断一个数是否为素数。调用该函数，判断从键盘输入的一个数是否为素数
    :return:
    """
    n = int(input("请输入一个数"))
    i = 2
    flag = True
    while i <= n - 1:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        print("%d是素数" % n)
    else:
        print("%d不是素数" % n)


if __name__ == '__main__':
    # s_first()
    # special_characters()
    # phone()
    # single(0.054)
    # complex(0.07)
    prime_number()