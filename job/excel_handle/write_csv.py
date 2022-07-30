# coding=utf-8
"""
将指定咧写入csv
"""
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')
student_num = 2110412209  # 同寝室学号
excel_name = 'writer_csv.csv'
data_pd = pd.read_excel(u'21电气6班花名册.xls',sheet_name="Sheet1", encoding='utf-8')[['序号','姓名','学号']]
print data_pd.index
print data_pd.loc[data_pd['学号'] == 2110412317]
print data_pd.loc[data_pd['学号'] == 2110412317]['序号']
data_pd.loc[data_pd['学号'] == student_num,'序号']= -1
res_data = data_pd.sort_values(by='序号', ascending=True, inplace=False)  # 排序结果
res_data.to_csv(excel_name, index=False)

