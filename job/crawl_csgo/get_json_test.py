# -*- coding: utf-8 -*-
from os import times
import requests
from selenium import webdriver
import get_category_url as get_category_url_class
import pandas as pd
import time
import sys
reload(sys)
import os
sys.setdefaultencoding('utf8')
""" log日志文件设置 """
import logging
from datetime import datetime
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 设置打印级别
formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')

# 设置屏幕打印的格式
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)
log_name =str(datetime.now().strftime('%Y%m%d%H')) +'.log'
# 设置log保存
fh = logging.FileHandler(log_name, encoding='utf8')
fh.setFormatter(formatter)
logger.addHandler(fh)


class GetData:
    def __init__(self):
        # self.mysql = create_table.CreateTable()
        self.goods_query_list = get_category_url_class.GetGoodsCategoryUrl().get_goods_category_url()
        self.category_url_list_test = ['https://www.youpin898.com/market/csgo?gameId=730&weapon=weapon_knife_survival_bowie',
                                       'https://www.youpin898.com/market/csgo?gameId=730&weapon=Broken Fang Glovesn']
        self.options = webdriver.ChromeOptions()
        self.chrome_dir = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Chrome驱动安装本地地址
        self.items_url_list = []  # 商品内容url
        self.id_url_dict = {}  # id和url对应的字典
        self.attribute_all_list = []  # 所有商品数据
        self.header = {
                            'authority': 'api.youpin898.com',
                            'accept': 'application/json, text/plain, */*',
                            'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
                            'apptype': '1',
                            'cache-control': 'no-cache',
                            'content-type': 'application/json;charset=UTF-8',
                            'origin': 'https://www.youpin898.com',
                            'pragma': 'no-cache',
                            'referer': 'https://www.youpin898.com/',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-site',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
                        }
        self.json_url_head = 'https://api.youpin898.com/api/homepage/es/template/GetCsGoPagedList'


    def get_data(self):

        """
        测试
        :return:
        """
        goods_query_list_test = ['weapon_knife_falchion', 'Sport Gloves', 'weapon_mac10']
        # for goods_query in self.goods_query_list:
        for goods_query in self.goods_query_list:
            time.sleep(1)
            logging.info("goods_query：" + str(goods_query))
            max_page = 10
            for page in range(max_page):
                payload = '{"listType":"30","gameId":"730","weapon":' +"\"" + str(goods_query) + "\"" + ',"pageIndex":' + str(
                    page) + ',"pageSize":100,"sortType":"0","listSortType":"2"}'
                response = requests.post(self.json_url_head, headers=self.header, data=payload).json()

                if response['Data'] == None:
                    break
                else:
                    for data in response['Data']:
                        print data['CommodityName']  # 名称
                        print data['Quality']  # 军级
                        print data['Exterior']  # 属性
                        print data['OnLeaseCount']  # 在租数量
                        print data['OnSaleCount']  # 在售数量
                        print data['LeaseUnitPrice']  # 短租最低价
                        print data['LongLeaseUnitPrice']  # 长租最低价
                        print data['Price']  # 在售最低价
                        if data['Price'] == '0' or data['Price']== None or data['LeaseUnitPrice'] ==None:
                            lease_s_price = None
<<<<<<< HEAD
                            lease_s_price_160 = None
                            print 'None'
                        else:
                            lease_s_price = float(data['LeaseUnitPrice']) / float(data['Price']) # 短租最低价/在售最低价
                            lease_s_price_160 = lease_s_price*160 # 短租最低价/在售最低价/160
                        if data['Price'] == '0' or data['Price'] is None or data['LeaseUnitPrice'] is None:
                            lease_l_price = None
                            lease_l_price_240 = None
                            print 'None'
                        else:
                            lease_l_price = float(data['LongLeaseUnitPrice']) / float(data['Price'])
                            lease_l_price_240 = lease_l_price*240
                            print lease_l_price  # 长租最低价/在售最低价
                        attribute_one_list = [data['CommodityName'], data['Quality'], data['Exterior'], data['OnLeaseCount'],
                                              data['OnSaleCount'], data['LeaseUnitPrice'], data['LongLeaseUnitPrice'],
                                              data['Price'], lease_s_price, lease_l_price, lease_s_price_160, lease_l_price_240]  # 一个商品所有数据
=======
                            print 'None'
                        else:
                            lease_s_price = float(data['LeaseUnitPrice']) / float(data['Price']) # 短租最低价/在售最低价
                        if data['Price'] == '0' or data['Price'] is None or data['LeaseUnitPrice'] is None:
                            lease_l_price = None
                            print 'None'
                        else:
                            lease_l_price = float(data['LongLeaseUnitPrice']) / float(data['Price'])
                            print lease_l_price  # 长租最低价/在售最低价
                        attribute_one_list = [data['CommodityName'], data['Quality'], data['Exterior'], data['OnLeaseCount'],
                                              data['OnSaleCount'], data['LeaseUnitPrice'], data['LongLeaseUnitPrice'],
                                              data['Price'], lease_s_price, lease_l_price]  # 一个商品所有数据
>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780
                        # print attribute_one_list
                        self.attribute_all_list.append(attribute_one_list)
                        # print self.attribute_all_list

    def save_data_excel(self):
        """
        将数据存入Excel
        :return: None
        """
        excel_name = str(datetime.now().strftime('%Y%m%d%H')) +'.xlsx'
        df = pd.DataFrame(self.attribute_all_list)
<<<<<<< HEAD
        df.columns =['名称', '军级', '属性', '在租数量', '在售数量', '短租最低价', '长租最低价', '在售最低价', '短租最低价/在售最低价', '长租最低价/在售最低价', '短租最低价/在售最低价*160','长租最低价/在售最低价*240']
=======
        df.columns =['名称', '军级', '属性', '在租数量', '在售数量', '短租最低价', '长租最低价', '在售最低价', '短租最低价/在售最低价', '长租最低价/在售最低价']
>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780
        writer = pd.ExcelWriter(excel_name)
        df.to_excel(writer, encoding='utf_8')
        writer.save()


if __name__ == '__main__':
    getData = GetData()
    getData.get_data()
    getData.save_data_excel()
    print getData.attribute_all_list
    logging.info("一共有数据："+ str(len(getData.attribute_all_list)))
