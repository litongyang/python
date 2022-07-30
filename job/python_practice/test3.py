# -*- coding: utf-8 -*-
from random import randint


def random_num(num):
    """
    猜随机数
    :param num:
    :return:
    """
    random_num = randint(0,100)
    if num >random_num:
        print "太大"
    elif num < random_num:
        print "太小"
    else:
        print "恭喜，你猜中了!"


def prime_number():
    """
    1000以内素数之和
    :return:
    """
    num = []
    i = 2
    for i in range(2, 1000):
        j = 2
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num.append(i)
    sum = 0
    for v in num:
        sum += v
    print "素数之和：",sum


def sum():
    """
    按公式 s=1^2+2^2+3^2+4^2+……+n^2  求累加数s不超过1000的最大项数n
    :return:
    """
    s, n = 0, 1
    print('n    s')
    while True:
        s += n * n
        if s > 1000:
            break
        print(n, '  ', s)
        n += 1
        print('*' * 30)
    print('累积和不超过1000的最大项数是%d' % n)


if __name__ == '__main__':
    # random_num(50)
    # prime_number()
    sum()