# -*- coding: utf-8 -*-
import time
# from db.db_connect import yunqitong_bank
import pandas as pd
import datetime
import re
import os
# from youke import  df_yk


time_start = time.time() #开始计时

''''时间控制'''
fir_today = datetime.date.today()
# fir_today = datetime.date(day=11,month=5,year=2021)
out_day = (fir_today-datetime.date(day=1,month=1,year=2022)).days
# out_day = (fir_today-datetime.date(day=1,month=5,year=2022)).days
day_list = []
for i in range(out_day):
    last_date = fir_today - datetime.timedelta(days=i)
    date_a = last_date.strftime("%Y%m%d")
    day_list.append(date_a)

'''汇总所有前期输出的手机号，便于后面去重'''
df_pro = pd.DataFrame(data=None,columns=['dest_number'])
file = os.listdir('./导出数据')
for x in file:
    print x
    if x !='.DS_Store':
        file_name = './导出数据/{0}'.format(x)
        df1 = pd.read_excel(file_name)
        df_pro = pd.concat([df_pro,df1],axis=0)
        df_pro['dest_number'] = df_pro['dest_number'].astype(str)
    else:
        continue
# df_yk = df_yk()
# df_pro = pd.concat([df_pro,df_yk],axis=0)


# # 设置数据量
# n = 50000
# df = pd.DataFrame(data=None,columns=['dest_number'])
# for x in day_list:
#     if len(df)<n:
#
#         # 营销通道-- where a.channel_id in (594,239,151,126,125,113,111,91,53,52,29,20,11,9,111,58,51,34,29,10,61,69,40,66,67)
#         # SP验证  where a.channel_id in (594,239,151,126,125,113,111,91,53,52,29,20,11,9,111,58,51,34,29,10,61,69,40,66,67)
#         #593为通知
#         sqla = """
#             select dest_number,a.content
#             from mt_{}  a
#             where a.channel_id in (593)
#             # and a.province not in ('四川','未知')
#             # and city regexp ('成都|温州|杭州|深圳|南京|郑州')
#              and city regexp ('武汉')
#             and a.provider = 'cmcc'
#             # and sign NOT REGEXP '360'
#             # and a.province in ('四川')
#             """.format(x)
#         dfa = yunqitong_bank(sqla)
#         dfa['dest_number'] = dfa['dest_number'].astype(str)
#         dfa['dest_number'].str.strip()  # 清除前后的空格
#         dfa = dfa[~dfa['dest_number'].isin(df_pro['dest_number'])]
#         dfa['res'] = dfa['content'].str.match('.+(本次)?(已)?(还款|扣款|代扣|支付)成功|.+(本次)?(已)?成功(还款|扣款|代扣|划扣|支付)')
#         # dfa['res'] = dfa['content'].str.match('.+(本期)?(应)?(还|还款|扣款|代扣|划扣|支付)(金额)?(：|:)?([1-9][0-9]+([.][0-9]+)?)?|.+账单|.+需(还款|扣款|划扣|支付)(金额)?(：|:)?([1-9][0-9]+([.][0-9]+)?)?')
#         dfa = dfa[dfa['res'] ==True]
#         dfa['res2'] = dfa['content'].str.match('.+(账户)?(自动)?(扣款|还款|扣款|划扣)(：|:)?([0-9]+([.][0-9]+)?(元)?)?失败|.基金|.定投|.购买|.批跑|.跑批|.(已)?(全部)?结清')
#         # dfa['res2'] = dfa['content'].str.match('.+(账户)?(自动)?(还款|代扣|扣款|划扣|支付)(金额)?(：|:)?([1-9][0-9]+([.][0-9]+)?)?(元)?失败|.+未足额还款|.+尚有(金额|余额|未还金额)?(：|:)?[1-9]([0-9]+)?([.][0-9]+)?(未还)?|.+基金|.+定投|.+购买|.+(本次)?(已)?(还款|扣款|代扣|划扣|支付)成功|.+(本次)?(已)?成功(还款|扣款|代扣|划扣|支付)|.(已)?(全部)?结清|.+分期成功|.+成功分期|.+批跑|.+跑批')
#         dfa = dfa[dfa['res2'] == False]
#         dfa = dfa[['dest_number']]
#         df = df.append(dfa)
#         df.drop_duplicates(subset=['dest_number'],
#             keep='first',
#             inplace=True)
#
#
#
#         print(x,len(df))
#         time.sleep(1)
#     else:
#         df = df.head(n)
#         break
# file_name = './导出数据/武汉移动还款成功外部通道{0}-{1}.xlsx'.format(day_list[0],x)
# df.to_excel(file_name,index=False, encoding="utf-8")
# print('执行结束')



time_end = time.time()  # 结束计时
time_c = time_end - time_start  # 运行所花时间
print('time cost', time_c, 's')
