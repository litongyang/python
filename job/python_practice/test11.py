# -*- coding: utf-8 -*-

def factor(num):
    """
    求出一个数除了1和它自身以外的所有因子。从键盘输入一个数，调用该函数，输出其所有因子。
    :param num:
    :return:
    """
    for i in range(2, num):
        if num % i == 0:
            print i


def narcissistic_number():
    """
    判断一个数是否为水仙花数
    :return:
    """
    num = int(input("请输入一个三位数子:"))

    gw = num % 10  # 取个位数
    sw = num % 100 // 10  # 取百位数
    bw = num // 100  # 取百位数

    total = gw ** 3 + sw ** 3 + bw ** 3

    if num == total:
        print "该数字是一个水仙花数"
    else:
        print "该数字不是水仙花数"


if __name__ == '__main__':
    # factor(30)
    narcissistic_number()