# -*- coding: utf-8 -*-
import datetime

class Circle:
    """
    设计一个Circle类来表示圆，这个类包含圆的半径以及求面积和周长的函数。再使用这个类创建半径为1~10的圆，并计算出相应的面积和周长
    """
    def __init__(self, radius,):
        self.radius = radius

    def perimeter(self):
        return 3.14 * 2 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Account(object):
    def __init__(self, countid, money, year_Rate):
        self.__countid = countid
        self.__money = money
        self.__year_Rate = year_Rate

    def month_Rate(self):
        return self.getyear_Rate() / 1200.0

    def month_Interest(self):
        return self.getmoney() * self.month_Rate()

    def withdraw(self, x):
        self.__money = self.getmoney() - x

    def deposit(self, x):
        self.__money = self.getmoney() + x

    def getcountid(self):
        return self.__countid

    def getmoney(self):
        return self.__money

    def getyear_Rate(self):
        return self.__year_Rate

    def setyear_Rate(self, year_Rate):
        self.__year_Rate = year_Rate




class Timer:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def gethour(self):
        return self.hour

    def getminute(self):
        return self.minute

    def getsecond(self):
        return self.second

    def settime(self, new_hour, new_minute, new_second):
        self.hour = new_hour
        self.minute = new_minute
        self.second = new_second

    def showtime(self):
        print(self.hour, ":", self.minute, ":", self.second)






if __name__ == '__main__':
    for i in range(1, 11):
        circle = Circle(i)
        print "半径为：",i
        print "圆的周长：", format(circle.perimeter(),'.2f')
        print "圆的面积：", float(circle.area())
        print "==========="

    year_Rate = 4.5  # 年利润为4.5%,赋值4.5即可
    countid = "998866"
    money = 2000
    count1 = Account(countid, money, year_Rate)
    count1.deposit(150)
    count1.withdraw(1500)
    print "账号：", count1.getcountid()
    print "余额：", count1.getmoney()
    print "年利率：", str(count1.getyear_Rate()) + "%"
    print "月利率：", str(count1.month_Rate() * 100) + "%"
    print "月息：", count1.month_Interest()
    print "~~~~~~~~~~~~~~~~~~~~~"

    d = datetime.datetime.now()
    timer1 = Timer(d.hour, d.minute, d.second)
    timer1.showtime()



