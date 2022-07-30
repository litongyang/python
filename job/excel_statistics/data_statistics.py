# -*- coding: utf-8 -*-
"""pip install xlrd==1.2.0"""
import pandas as pd
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
txt_name = str(datetime.now().strftime('%Y%m%d')) + '.txt'
file_handle = open("../%s"%txt_name, mode='w')


class GetStatisticsData:
    def __init__(self):
        self.out_day_excel_name = u'设备外联每日统计.xlsx'
        self.out_week_excel_name = u'设备外联每周统计.xlsx'
        self.out_month_excel_name = u'设备外联每月统计.xlsx'

        self.attack_day_excel_name = u'设备攻击每日统计.xlsx'
        self.attack_week_excel_name = u'设备攻击每周统计.xlsx'
        self.attack_month_excel_name = u'设备攻击每月统计.xlsx'

        self.company_dict_excel_name = u'对应名称.xlsx'
        self.remove_excel_name = u'对跳过.xlsx'

        self.remove_name = []  # 跳过公司list
        self.company_dict = {}  # 公司和省份对应的字典
        self.result_excel_name = 'result' + str(datetime.now().strftime('%Y%m%d%H')) + '.xlsx'

    def get_data(self, data_excel_name):
        remove_name_pd = pd.read_excel(self.remove_excel_name, sheet_name="Sheet1", encoding='utf-8')
        self.remove_name.append(remove_name_pd.columns.values[0])
        company_dict_pd = pd.read_excel(self.company_dict_excel_name, encoding='utf-8')
        self.company_dict = dict(zip(company_dict_pd[u'原名称'].values, company_dict_pd[u'输出名称'].values))
        company_dict_pd.rename(columns={'原名称': '所属服务站'}, inplace=True)
        out_day_pd = pd.read_excel(data_excel_name, encoding='utf-8')
        # 删除 跳过公司的数据
        for remove_name_one in self.remove_name:
            for name in out_day_pd['所属服务站'].values:
                if name == remove_name_one:
                    out_day_pd.drop(columns=[name])
        # 数据和公司字典关联
        data_pa = pd.merge(out_day_pd, company_dict_pd, on='所属服务站')
        # 按输出名称聚合求和
        data_group = data_pa.groupby("输出名称").sum()
        # 结果
        re = data_group['已研判数量'] / data_group['数量']
        re_sort = re.sort_values(ascending=False, inplace=False)  # 排序后的结果数据
        file_handle.write(' 排名 ' + '\t' + '服务站' + '\t' + '    研判完成率' + '\n')
        for i in range(0, len(re_sort)):
            index = '第' + str(i + 1) + '名'
            if len(re_sort.index[i]) == 3:  # 服务站名字为3个字的加一个空格
                file_handle.write(index + '\t' + re_sort.index[i] + ' ' + '\t\t' + str(format(re_sort.values[i], '.2%'))
                                  + '\n')
            elif len(re_sort.index[i]) == 2:  # 服务站名字为2个字的加一个空格
                file_handle.write(
                    index + '\t' + re_sort.index[i] + '  ' + '\t\t' + str(format(re_sort.values[i], '.2%')) + '\n')
            else:  # 服务站名字为4个字的不加空格
                file_handle.write(
                    index + '\t' + re_sort.index[i] + '\t' + str(format(re_sort.values[i], '.2%')) + '\n')


if __name__ == '__main__':
    get_data = GetStatisticsData()
    file_handle.write('各服务中心：' + '\n' + '昨日、本周及本月研判完成度具体情况如下：' + '\n')
    file_handle.write('【昨日(29日)研判成绩排名】：' + '\n')
    file_handle.write('正面攻击研判完成度：' + '\n')
    get_data.get_data(get_data.attack_day_excel_name)
    file_handle.write('外联研判完成度：' + '\n')
    get_data.get_data(get_data.out_day_excel_name)
    file_handle.write('其他未发生' + '\n')
    file_handle.write('【本周(5.23-5.29)研判成绩排名】	：' + '\n')
    file_handle.write('正面攻击研判完成度：' + '\n')
    get_data.get_data(get_data.attack_week_excel_name)
    file_handle.write('外联研判完成度：' + '\n')
    get_data.get_data(get_data.out_week_excel_name)
    file_handle.write('其他未发生' + '\n')
    file_handle.write('【本月(5.1-5.29)研判成绩排名】	：' + '\n')
    file_handle.write('正面攻击研判完成度：' + '\n')
    get_data.get_data(get_data.out_month_excel_name)
    file_handle.write('外联研判完成度：' + '\n')
    get_data.get_data(get_data.attack_month_excel_name)
    file_handle.write('其他未发生' + '\n')
    file_handle.write('注：统计时间为%s点，计算数据为1日 0:00 - 29日24:00数据'%datetime.now().strftime('%H'))