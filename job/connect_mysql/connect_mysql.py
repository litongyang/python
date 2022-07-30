# -*- coding: utf-8 -*-

import MySQLdb
import time
import random


class CreateTable:
    """
    1、连接 mysql数据库
    2、创建mysql数据表
    3、在mysql表插入数据
    4、在mysql表删除数据
    """
    def __init__(self):
        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '1234'  # 密码
        self.table_name = 'test1'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port, use_unicode=True, charset="utf8", autocommit=True)
        self.cur = self.conn.cursor()

    def create_table_test(self):
        """
        创建数据表
        :return:
        """
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "time varchar(100) comment '时间',"
                "distance varchar(100) comment '距离',"
                "temperature varchar(100) comment '温度',"
                "PRIMARY KEY (`time`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_name)
        except Exception, e:
            print Exception, e

    def insert_data(self, table_name, insert_sql):
        """
        插入数据
        :param table_name:
        :param insert_sql:
        :return:
        """
        try:
            print "插入数据：", "insert into %s values(%s)" % (table_name, insert_sql)
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("insert into %s values(%s)" % (table_name, insert_sql))

        except Exception, e:
            print Exception, e

    def delete_data(self, table_name):
        """
        删除数据
        :param table_name:
        :param delete_sql:
        :return:
        """
        try:
            print "删除数据：", "delete from %s" % table_name
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("delete from %s" % table_name)

        except Exception, e:
            print Exception, e



def time_factory(start_time=(2022, 1, 1, 0, 0, 0, 0, 0, 0), end_time=(2022, 4, 30, 23, 59, 59, 0, 0, 0)):
    start = time.mktime(start_time)  # 生成开始时间戳
    end = time.mktime(end_time)  # 生成结束时间戳
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串
    return date


if __name__ == '__main__':
    # data_insert_test = [['张强', '13:12', '20cm', ' 36°C'], [ '王梅',  '17:11', '10cm', ' 32°C'],
    #                     ['荀晓峰', '08:20', '70cm', ' 28°C'], [ '李磊',  '23:25', '27cm', ' 26°C'], [ '韩宇',  '19:37', '35cm', ' 27°C']]

    test = CreateTable()
    print time_factory(start_time=(2022, 1, 1, 0, 0, 0, 0, 0, 0), end_time=(2022, 4, 30, 23, 59, 59, 0, 0, 0))
    # test.create_table_test()
    # """插入数据 """
    for i in range(0,100):
        insert_sql = ''
        insert_sql += '\'' + str(time_factory(start_time=(2022, 1, 1, 0, 0, 0, 0, 0, 0), end_time=(2022, 4, 30, 23, 59, 59, 0, 0, 0))) + '\'' + ','
        insert_sql += '\'' + str(random.randint(0, 1000)) + '\'' + ','
        insert_sql += '\'' + str(random.randint(0, 50)) + '\'' + ','
        insert_sql = insert_sql[0:-1]
        test.insert_data(test.table_name, insert_sql)
    # for i in range(0,100):
    #     insert_sql = ''
    #     insert_sql += '\'' + str(insert[0]) + '\'' + ','
    #     insert_sql += '\'' + str(insert[1]) + '\'' + ','
    #     insert_sql += '\'' + str(insert[2]) + '\'' + ','
    #     insert_sql += '\'' + str(insert[3]) + '\'' + ','
    #     insert_sql = insert_sql[0:-1]
    #     test.insert_data(test.table_name, insert_sql)
    """删除语句"""
    # test.delete_data(test.table_name)

