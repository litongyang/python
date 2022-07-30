import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class DataProcess:
    def __init__(self):
        # self.zzsfp_file = 'D:\zzsfp'  # 文件位置自定义
        self.zzsfp_file = 'zzsfp.txt'  # 测试用的数据样本
        self.nsrxx_file = 'nsrxx'
        self.train_pd = pd.DataFrame()
        self.train_x = []
        self.train_y = []

    def get_data(self):
        """
        获取训练集
        Returns:

        """
        zzsfp_pd = pd.read_csv('zzsfp.txt', sep=",",
                               names=['fp_nid', 'xf_id', 'gf_id', 'je', 'se', 'jshj', 'kpyf', 'kprq', 'zfbz'])
        nsrxx_gf_pd = pd.read_csv('nsrxx', sep=",",
                                  names=['hydm', 'gf_id', 'djzclx_dm', 'kydjrq', 'xgrq', 'label'])  # 与 gf_id merge
        nsrxx_xf_pd = pd.read_csv('nsrxx', sep=",",
                                  names=['hydm', 'xf_id', 'djzclx_dm', 'kydjrq', 'xgrq', 'label'])  # 与 xf_id merge
        nsrxx_xf_pd['hydm'] = nsrxx_xf_pd['hydm'].str.strip("(")  # 数据清洗
        nsrxx_xf_pd['label'] = nsrxx_xf_pd['label'].str.strip(")")  # 数据清洗

        data1_pd = pd.merge(zzsfp_pd, nsrxx_xf_pd, on='xf_id')
        data1_pd.insert(loc=3, column='count', value=1)  # 计数列
        data1_pd.loc[data1_pd['zfbz'] == 'Y)', 'zfbz'] = 0  # Y变0
        data1_pd.loc[data1_pd['zfbz'] == 'N)', 'zfbz'] = 1
        # print(data1_pd.columns)
        je_group = data1_pd.groupby("xf_id")['je'].sum()  # 销售总金额
        se_group = data1_pd.groupby("xf_id")['se'].sum()  # 总税收
        yxfp_group = data1_pd.groupby("xf_id")['zfbz'].sum()  # 有效发票总量
        fpcnt_group = data1_pd.groupby("xf_id")['zfbz'].count()  # 发票总量
        fpcnt_group = pd.DataFrame(fpcnt_group, columns=['zfbz'])
        fpcnt_group.columns = ['fpcnt']  # 列更名
        # print(fpcnt_group)
        # print(data_group[data_group['zfbz']>1])
        # print(data1_pd.columns)
        # print(data_group.columns)
        # print(yxfp_group[yxfp_group.values>1])
        print("===========")
        """zzsfp_pd merge nsrxx_gf_pd:求购量总金额"""
        data2_pd = pd.merge(zzsfp_pd, nsrxx_gf_pd, on='gf_id')
        gl_group = data2_pd.groupby("gf_id").sum()  # 购量总金额
        gl_group = pd.DataFrame(gl_group, columns=['xf_id', 'je'])
        gl_group.columns = ['xf_id', 'gl']  # 列更名

        """合并数据"""
        merge1_pd = pd.merge(je_group, se_group, on='xf_id')
        merge2_pd = pd.merge(merge1_pd, yxfp_group, on='xf_id')
        merge3_pd = pd.merge(merge2_pd, fpcnt_group, on='xf_id')
        merge4_pd = pd.merge(merge3_pd, gl_group, on='xf_id')
        merge4_pd['zzbl'] = merge4_pd['je'] / merge4_pd['gl']  # 增值比率
        merge4_pd['yxfpl'] = merge4_pd['zfbz'] / merge4_pd['fpcnt']  # 有效发票率
        merge4_pd['ssl'] = merge4_pd['se'] / merge4_pd['je']  # 税收率
        info_pd = pd.DataFrame(nsrxx_xf_pd, columns=['xf_id', 'hydm', 'kydjrq', 'label'])
        info_pd['Time'] = pd.to_datetime(info_pd['kydjrq'])
        info_pd['year'] = info_pd['Time'].dt.strftime('%Y')
        train_pd = pd.merge(merge4_pd, info_pd, on='xf_id')
        train_pd = pd.DataFrame(train_pd, columns=['hydm', 'year', 'zzbl', 'ssl', 'yxfpl', 'label'])
        train_pd[['hydm']] = train_pd[['hydm']].astype(int)
        train_pd[['year']] = train_pd[['year']].astype(int)
        train_pd[['label']] = train_pd[['label']].astype(int)
        train_x_pd = pd.DataFrame(train_pd, columns=['hydm', 'year', 'zzbl', 'ssl', 'yxfpl']).values
        train_y_pd = pd.DataFrame(train_pd, columns=['label']).values
        self.train_x = np.array(train_x_pd)
        self.train_y = np.array(train_y_pd)
        print(train_pd)
        print(self.train_x)
        print(self.train_y)
        """
        # 选取指定的列
        # col_n = ['fp_nid', 'nsr_id', 'label']
        # a = pd.DataFrame(data_pd, columns=col_n)

        # 删除指定列的特殊符号
        # data_pd['fp_nid'] = data_pd['fp_nid'].str.strip("(")
        # data_pd['label'] = data_pd['label'].str.strip(")")
        # print(data_pd['label'])
        """

    def mmodel(self):
        clf = RandomForestClassifier(bootstrap=True, oob_score=True, criterion='gini', n_estimators=90)
        model = clf.fit(self.train_x, self.train_y)  # 训练
        print(model)


if __name__ == '__main__':
    data_process = DataProcess()
    data_process.get_data()
    data_process.mmodel()
