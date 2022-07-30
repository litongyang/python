# -*- coding: utf-8 -*-

import MySQLdb


class CreateTable:
    def __init__(self):
        """
        self.db_name = 'spider'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = '10.10.202.16'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '1234abcd'  # 密码
        """
        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '1234'  # 密码
        self.table_name = 'csgo_info'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port, use_unicode=True, charset="utf8", autocommit=True)
        self.cur = self.conn.cursor()

    # 利率和成交量的每日数据
    def create_table_csgo_info(self):
        try:
            self.cur.execute('set names \'utf8\'')
            # self.cur.execute("drop table if exists %s" % self.table_name)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "name varchar(100) comment '产品m名称',"
                "level varchar(100) comment '产品级别名称',"
                "attribute varchar(100) comment '产品属性',"
                "lease_cnt double comment '租赁数量',"
                "sale_cnt double comment '出卖数量',"
                "PRIMARY KEY (`name`,`level`,`attribute`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_name)
        except Exception, e:
            print Exception, e

    def insert_data(self, table_name, insert_sql):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("insert into %s values(%s)" % (table_name, insert_sql))
            print "insert into %s values(%s)" % (table_name, insert_sql)
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_csgo_info()