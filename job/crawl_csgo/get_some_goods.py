# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime
from openpyxl import *
from get_json_test import GetData
import os
import sys
reload(sys)
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


class GetSomeGoods:
    """
    获取指定商品信息
    """
    def __init__(self):
        self.some_goods_file = 'C:\\Users\\Administrator\\Desktop\\goods.xlsx'
        self.some_goods_excel = 'some_goods' + str(datetime.now().strftime('%Y%m%d%H')) +'.xlsx'
        self.all_excel_name = str(datetime.now().strftime('%Y%m%d%H')) + '.xlsx'


    def get_goods_info(self):
        if not os.path.exists(self.all_excel_name):
            getData = GetData()
            getData.get_data()
            getData.save_data_excel()
            print getData.attribute_all_list
            logging.info("一共有数据：" + str(len(getData.attribute_all_list)))

        columns = ['名称', '军级', '属性', '在租数量', '在售数量', '短租最低价', '长租最低价', '在售最低价', '短租最低价/在售最低价', '长租最低价/在售最低价',
                   '短租最低价/在售最低价*160', '长租最低价/在售最低价*240']
        df = pd.DataFrame(columns=columns)  # 构造一个空df
        name_df = pd.read_excel(self.some_goods_file,  encoding='utf-8')['名称']
        all_df = pd.read_excel(self.all_excel_name,  encoding='utf-8')
        for i in range(0, len(name_df.values)):
            data_df = all_df.loc[all_df['名称'] == name_df.values[i]]
            del data_df['Unnamed: 0']
            data_df = data_df.drop_duplicates()
            df = df.append(data_df)
        writer = pd.ExcelWriter(self.some_goods_excel)
        df.to_excel(writer, index=False, encoding='utf_8')
        writer.save()



if __name__ == '__main__':
    get_some_goods = GetSomeGoods()
    get_some_goods.get_goods_info()
