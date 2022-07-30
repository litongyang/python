# -*- coding: utf-8 -*-



def roster():
    """
    一个基于列表的建议花名册管理系统
    :return:
    """
    print("="*50)
    print("学生管理系统V1.1")
    print("功能选择如下：")
    print("1.增添学生")
    print("2.删除学生")
    print("3.修改信息")
    print("4.查找信息")
    print("5.退出")
    print("="*50)

    names = []  # 定义一个列表

    while True:
        num=int(input("请输入你需要操作的功能序号："))
        if num==1:
            new_name=raw_input("请输入你要增添的姓名：")
            if new_name in names:
                print "您需要增添的名字已经存在"
            else:
                names.append(new_name)
                print names
        elif num==2:
            del_name = raw_input("请输入你要删除的姓名：")
            if del_name in names:
                names.remove(del_name)
                print names
            else:
                print "您需要删除的名字不存在..."

        elif num==3:
            mod_name = raw_input("请输入你要修改的姓名：")
            if mod_name in names:
                print "您需要修改的名字存在"
            else:
                print "您需要修改的名字不存在..."
        elif num==4:
            find_name = raw_input("请输入你要查找的姓名：")
            if find_name in names:
                print "存在此人..."
            else:
                print "抱歉，查无此人..."
        elif num==5:
            break
        else:
            print "您输入的信息有误，请重新输入"


if __name__ == '__main__':
    roster()
