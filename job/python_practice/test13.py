# -*- coding: utf-8 -*-

import math


class Circle:
    """
    仿照例8-14 定义一个Circle类。
    """

    def __init__(self):
        pass

    def SetCenter(self, x, y):
        self.x = x
        self.y = y

    def SetRadius(self, r):
        self.r = r

    def GetArea(self):
        return math.pi * r ** 2


class Person:
    __age = 0
    name = 'nick'
    gender = 'male'

    def __init__(self, name='nick', age=0, gender='male'):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Person):
    number = ''

    def __init__(self, number=2):
        # super().__init__(name, age, gender)
        Person.name = 'nick'
        Person.age = 0
        Person.gender = 'male'
        self.number = number

    def show_info(self):
        print(self.name, 'is an Employee')


class Exeutive(Employee):
    def show_info(self):
        print(self.name, 'is Executive')


def a_b():
    """
    用户输入一个数字，存入变量a   （a为浮点数）
    用户输入第二个数字，存入变量b  （b为浮点数）
    计算 a+b、a-b、a*b、以及a/b的值 （注意除数不能为0）
    给以上的程序加上异常处理，处理用户输入非数字，以及除数为0的情况。
    :return:
    """
    try:
        a = input("输入第一个数：")
        b = input("输入第二个数：")
        print "a+b:", a+b
        print "a-b:", a-b
        print "a*b:", a*b
        print "a/b:", a/b
    except Exception, e:
        print Exception, e


if __name__ == '__main__':
    # x = input("输入圆心的x坐标:")
    # y = input("输入圆心的y坐标:")
    # r = input("输入半径:")  # 输入半径
    # c = Circle()  # 创建Cirle对象
    # c.SetCenter(x, y)  # 设置圆心
    # c.SetRadius(r)  # 设置半径
    # print 'center:(%.2f,%.2f),radius:%.2f' % (c.x, c.y, c.r)  # 输出圆心和半径
    # print 'area:%.2f' % c.GetArea()  # 输出面积
    # print "~~~~~~~~~~~~~~~~~~~"

    # person_list = [Exeutive(), Exeutive(), Exeutive(), Employee(), Employee()]
    # for e in person_list:
    #     e.show_info()

    a_b()
