# -*- coding: utf-8 -*-
import math


def area_compute(long, wide):
    """
    计算矩形面积
    :param long:
    :param wide:
    :return:
    """
    area = long * wide
    print "矩形面积：", area


def mean_sore(s1, s2, s3):
    """
    计算三个学生的均值
    :param s1:
    :param s2:
    :param s3:
    :return:
    """
    soreMean = (s1 + s2 + s3) / 3
    print "成绩均值：", soreMean

def invest_amount(rate):
    """
    计算投资金额
    :param rate:
    :return:
    """
    amount = 50000/math.pow((1+rate),120)
    print amount

# def if_pass(v1, v2, v3):
#     """
#     及格判断
#     :param v1:
#     :param v2:
#     :param v3:
#     :return:
#     """
#     if v1 >= 60 and v2 >= 60 and v3 >= 60:
#         print "三门课都及格"
#     if v1 >= 60 or v2 >= 60 or v3 >= 60:
#         print "至少一门课程及格"
#     if v1 >= 60 and (v2>=90 or v3>=90):
#         print "语文及格且数学或者英语优秀"


if __name__ == '__main__':
    # area_compute(2, 10)
    # mean_sore(99, 57, 67)
    invest_amount(0.035)
