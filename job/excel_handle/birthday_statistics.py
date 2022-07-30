# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import sys

reload(sys)
sys.setdefaultencoding('utf8')
"""
获取生日计数画柱状图
"""

birth_day = pd.read_excel(u'学生生日.xlsx', sheet_name="Sheet1", encoding='utf-8')['生日']
birth_mon_list = []
# #  获取生日
for birth in birth_day:
    mon_str = str(birth)[4:6]
    birth_mon_list.append(mon_str)
# 构造姓氏计数字典
birthMon_cnt_dict = Counter(birth_mon_list)
# # 获取x、y轴的值
birthMon_x = []
birthMon_y = []
for k, v in birthMon_cnt_dict.items():
    birthMon_x.append(k)
    birthMon_y.append(v)
# 画柱状图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'
plt.pie(birthMon_y, labels=birthMon_x, autopct='%3.1f%%')
plt.title(u"班级同学生日月份分布饼状图")
plt.show()
