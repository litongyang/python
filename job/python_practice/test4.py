# -*- coding: utf-8 -*-

# n = int(input("请输入一个正整数："))
# list3 = []
# while n != -1:
#     list3.append(n)
#     n = int(input("请输入一个正整数："))
# else:
#     print("输入结束")
# print(list3)
#
# list1 = []
# list2 = []
# for i in list3:
#     if i % 2 != 0 :
#         list1.append(i)
#     else:
#         list2.append(i)
# print "列表1中的奇书和为：",list1,sum(list1)
# print "列表中的偶数和为：",list2,sum(list2)



def sum_num():
    """
    从键盘输入一个正整数列表，以-1结束，分别计算列表中奇数和偶数的和。
    :return:
    """
    n = int(input("请输入一个正整数："))
    list3 = []
    while n != -1:
        list3.append(n)
        n = int(input("请输入一个正整数："))
    else:
        print("输入结束")
    print(list3)

    list1 = []
    list2 = []
    for i in list3:
        if i % 2 != 0 :
            list1.append(i)
        else:
            list2.append(i)
    print "列表1中的奇书和为：",list1, sum(list1)
    print "列表中的偶数和为：",list2, sum(list2)



def student_num():
    """
    已知10个学生的成绩68、75、32、99、78、45、88、72、83、78，请将成绩存放在列表中，请对其进行统计，输出优（100～90）、良（89～80）、中（79～60）、差（59～0）四个等级的人数。
    :return:
    """
    list1 =[68,75,32,99,78,45,88,72,83,78]
    list2 = [x for x in list1 if 90<=x<=100]
    list3 = [x for x in list1 if 80<=x<=89]
    list4 = [x for x in list1 if 60<=x<=79]
    list5 = [x for x in list1 if 0<=x<=59]
    print "成绩优秀人数：", str(len(list2))
    print "成绩良好人数：", str(len(list3))
    print "成绩中人数：", str(len(list4))
    print "成绩差人数：", str(len(list5))


def odd_number_list():
    """
    利用while循环创建一个包含10个奇数的列表，如果输入的不是奇数要给出提示信息并能继续输入，然后计算该列表的和与平均值。
    :return:
    """
    i =0
    list = []
    while i< 10:
        num = input("输入奇数")
        if num%2 ==1:
            list.append(num)
            i += 1
        else:
            print "重新输入奇数"
    print "sum:", sum(list), "avg:", sum(list)/len(list)


def student_dict():
    """
    请用字典编程：已知某班学生的姓名和成绩如下：输出这个班的学生姓名和成绩，并求出全班同学的人数和平均分并显示。
    :return:
    """
    dict = {'张三': '45', '李四': '78', '徐来': '40', '沙思思': '96', '如一': '65', '司音': '90', '赵敏': '78', '张旭宁': '99',
            '柏龙': '60', '思琪': '87'}
    for k,v in dict.items():
        print k,v
    print len(dict)
    print sum((map(int, dict.values()))) / 10

def online_retailers():
    """
    某家商店根据客户消费总额的不同将客户分为不同的类型
    :return:
    """
    list = [2.3, 4.5, 24, 17, 1, 7.8, 39, 21, 0.5, 1.2, 4, 1, 0.3]
    s1, s2, s3, s4 = 0, 0, 0, 0
    dict = {}
    for i in list:
        if i >= 10:
            s1 += 1
        elif i >= 5:
            s2 += 1
        elif i >= 3:
            s3 += 1
        else:
            s4 += 1
    dict['platinum'] = s1
    dict['gold'] = s2
    dict['silver'] = s3
    dict['ordinary'] = s4
    print(dict)


if __name__ == '__main__':
    # sum_num()
    # student_num()
    # odd_number_list()
    # student_dict()
    online_retailers()