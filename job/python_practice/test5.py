# -*- coding: utf-8 -*-

def fund_company():
    """
    某企业为职工发放奖金：如果入职超过5年，且销售业绩超过15000元的员工，奖金比例为0.2.....
    :return:
    """
    list = []
    n = int(input("请输入入职年限："))
    while n != -1:
        sales = float(input("请输入销售业绩："))
        if n > 5:
            if sales > 15000:
                ratio = 0.2
            elif sales > 10000:
                ratio = 0.15
            elif sales > 5000:
                ratio = 0.1
            else:
                ratio = 0.05
        else:
            if sales > 4000:
                ratio = 0.045
            else:
                ratio = 0.01
        bonus = sales * ratio
        print "您的奖金比例：", ratio, "您的奖金：", bonus
        list.append(bonus)
        n = int(input("请输入入职年限："))
    print "奖金列表为：", list


def five_int():
    """
    输入5个整数放到列表list1中，输出下标及值，然后将列表list1中大于平均值的元素组成一个新列表list2，输出平均值和列表list2。请利用列表推导式解决该问题。
    :return:
    """
    print("请输入五个整数")
    list1 = []
    for i in range(5):
        n = int(input("请输入第" + str(i + 1) + "个:"))
        list1.append(n)
    avg = sum(list1) / len(list1)
    list2 = [i for i in list1 if i > avg]
    print "平均值为:", avg, " list2为:", list2


def three_num():
    """
    编写程序，将由1、2、3、4这四个数字组成的每位数都不相同的所有三位数存入一个列表中并输出该列表。请利用列表推导式解决该问题。
    :return:
    """
    a = [1, 2, 3, 4]
    b = [i * 100 + j * 10 + x for i in a for j in a for x in a if i != j and i != x and j != x]
    print(b)


def del_list():
    """
    编写程序，给定列表[1,9,8,7,6,5,13,3,2,1]，先输出原列表，删除其中所有奇数后再输出。请利用列表推导式解决该问题。
    :return:
    """
    a = [1, 9, 8, 7, 6, 5, 13, 3, 2, 1]
    b = [i for i in a if i % 2 == 0]
    print '原列表:', a
    print b

def chicken():
    """
    百钱买百鸡：一只公鸡5块钱，一只母鸡3块钱，三只小鸡1块钱，现在要用一百块钱买一百只鸡，问公鸡、母鸡、小鸡各多少只？请利用列表推导式解决该问题。
    :return:
    """
    list1 = [(a, b, c) for a in range(0, 101) for b in range(0, 101) for c in range(0, 101) if
             5 * a + 3 * b + c / 3 == 100 and a + b + c == 100]
    print list1


if __name__ == '__main__':
    # fund_company()
    # five_int()
    # three_num()
    # del_list()
    chicken()