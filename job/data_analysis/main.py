import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.linear_model as lm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

class AnalysisAssigned:
    """

    """

    def __init__(self):
        self.data_path = path = 'Invistico_Airline.csv'
        self.data_df = pd.DataFrame()  # 构造一个空df
        self.train_data = pd.DataFrame()  # 构造一个空df,用于模型训练
        self.train_x = []
        self.train_y = []

    def get_data(self):
        """
        获取数据
        :return:
        """
        self.data_df = pd.read_csv(self.data_path)
        """查看数据情况"""
        # print(self.data_df.columns)
        # print(self.data_df.info)

    def data_cleaning(self):
        """
        数据清晰
        :return:
        """
        self.data_df = self.data_df.dropna(axis=0, subset=["satisfaction","Customer Type"])
        self.train_data = self.data_df
        self.train_data[self.train_data['satisfaction'] == 'satisfied'] = 1
        self.train_data[self.train_data['satisfaction'] == 'dissatisfied'] = 0
        self.train_data[self.train_data['Gender'] == 'Female'] = 0
        self.train_data[self.train_data['Gender'] == 'male'] = 1
        final_columns = self.train_data.drop(columns=['Customer Type', 'Type of Travel','Class'], axis=1).columns
        train_data = self.train_data[final_columns]
        final_columns_x = train_data.drop(columns=['satisfaction'], axis=1).columns
        self.train_x = train_data[final_columns_x]
        self.train_y = train_data['satisfaction']
        print(self.train_x.columns)
        print(self.train_y)

    def model_train(self):
        X_train, X_test, Y_train, Y_test = train_test_split(self.train_x, self.train_y, test_size=0.3, random_state=0)
        rf = RandomForestClassifier()
        rf.fit(X_train, Y_train.astype('int'))
        y_pre = rf.predict(X_test)
        print(Y_test.values)
        report = classification_report(list(Y_test.values), y_pre)
        print(y_pre)
        print("Features sorted by their score:")
        print(sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_))), self.train_x.columns)
        print(report)

    def data_analysis(self):
        """
        数据分析
        :return:
        """
        plt.figure(figsize=(10, 4))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        """客户性别分析"""
        gender_counts = self.data_df['Gender'].value_counts()
        print(gender_counts)
        sns.barplot(x=gender_counts.index, y=gender_counts.values)
        plt.title("男女总数对照")
        plt.show()

        """客户年龄数据分析"""
        age_df = pd.DataFrame()
        bins = [0, 13, 20, 35, 55, 100]
        labels = ['Kid', 'Teen', 'Adult', 'mid-life', 'old-age']
        age_df['AgeGroup'] = pd.cut(self.data_df['Age'], bins=bins, labels=labels, right=False)
        age_counts = age_df['AgeGroup'].value_counts()
        sns.barplot(y=age_counts.index, x=age_counts.values)
        plt.title("乘客年龄划分的数据展示")
        plt.show()

        """客户乘坐的位置类别的数据分析"""
        class_counts = self.data_df['Class'].value_counts()
        plt.pie(class_counts.values,labels=class_counts.index)
        plt.title("客户乘坐的位置类别的数据分析")
        plt.show()

        """乘客乘乘坐总航程的数据分析"""
        distance_mean = self.data_df['Flight Distance'].mean()
        print("distance_mean:", distance_mean)
        distance_df = pd.DataFrame()
        bins = [0, 500, 1000, 1500, 2000, 100000]
        labels = ['0-500', '500-1000', '1000-1500', '1500-2000','2000+']
        distance_df['DistanceGroup'] = pd.cut(self.data_df['Flight Distance'], bins=bins, labels=labels, right=False)
        distance_counts = distance_df['DistanceGroup'].value_counts()
        print(distance_counts)
        sns.barplot(y=distance_counts.index, x=distance_counts.values)
        plt.title("乘客乘乘坐总航程的数据分析")
        plt.show()

        """乘客被飞机延误时长的数据分析"""
        delay_mean = self.data_df['Departure Delay in Minutes'].std()
        print("delay_mean:", delay_mean)
        delay_df = pd.DataFrame()
        bins = [0, 5, 14, 20, 40, 60, 100000]
        labels = ['0-5', '0-14', '14-20', '20-40', '40-60', '60+']
        delay_df['DelayeGroup'] = pd.cut(self.data_df['Departure Delay in Minutes'], bins=bins, labels=labels, right=False)
        delay_counts = delay_df['DelayeGroup'].value_counts()
        print(delay_counts)
        sns.barplot(y=delay_counts.index, x=delay_counts.values)
        plt.title("乘客被飞机延误时长的数据分析")
        plt.show()

        """乘客乘坐航班出发/到达时间方便程度分析"""
        convenient_counts = self.data_df['Departure/Arrival time convenient'].value_counts()
        print("1111111111111", convenient_counts.values)
        plt.pie(convenient_counts.values,labels=convenient_counts.index)
        plt.title("乘客乘坐航班出发/到达时间方便程度分析")
        plt.show()

        """是否满意的人数数据分析"""
        satisfaction_counts = self.data_df['satisfaction'].value_counts()
        print(satisfaction_counts)
        sns.barplot(x=satisfaction_counts.index, y=satisfaction_counts.values)
        plt.title("是否满意的人数数据分析")
        plt.show()

        """乘客是否满意乘坐总公里对比分析"""
        fig, ax1 = plt.subplots()
        satisfied_distance = self.data_df[self.data_df['satisfaction']=='satisfied']['Flight Distance'].sort_values(ascending=True, inplace=False)
        dissatisfied_distance = self.data_df[self.data_df['satisfaction']=='dissatisfied']['Flight Distance'].sort_values(ascending=True, inplace=False)
        ax1.plot(range(0, len(satisfied_distance.values)), satisfied_distance.values, label='满意乘客的乘坐距离')
        ax1.plot(range(0, len(dissatisfied_distance.values)), dissatisfied_distance.values, label='不满意乘客的乘坐距离')
        ax1.legend()
        plt.title("乘客是否满意乘坐总公里对比分析")
        plt.show()

        """乘客是否满意年龄对比分析"""
        fig, ax1 = plt.subplots()
        satisfied_age = self.data_df[self.data_df['satisfaction'] == 'satisfied']['Age'].sort_values(
            ascending=True, inplace=False)
        dissatisfied_age = self.data_df[self.data_df['satisfaction'] == 'dissatisfied'][
            'Age'].sort_values(ascending=True, inplace=False)

        ax1.plot(range(0, len(satisfied_age.values)), satisfied_age.values, label='满意乘客的年龄')
        ax1.plot(range(0, len(dissatisfied_age.values)), dissatisfied_age.values, label='不满意乘客的年龄')
        ax1.legend()
        plt.title("乘客是否满意年龄对比分析")
        plt.show()

        """乘客是否满意飞机延误时长的对比分析"""
        fig, ax1 = plt.subplots()
        satisfied_delay = self.data_df[self.data_df['satisfaction'] == 'satisfied']['Departure Delay in Minutes'].sort_values(
            ascending=True, inplace=False)
        dissatisfied_delay = self.data_df[self.data_df['satisfaction'] == 'dissatisfied'][
            'Departure Delay in Minutes'].sort_values(ascending=True, inplace=False)
        ax1.plot(range(0, len(satisfied_delay.values)), satisfied_delay.values, label='满意乘客的飞机延误时长')
        ax1.plot(range(0, len(dissatisfied_delay.values)), dissatisfied_delay.values, label='不满意乘客的飞机延误时长')
        ax1.legend()
        plt.title("乘客是否满意飞机延误时长的对比分析")
        plt.show()


class AnalysisFree:
    """
    数据分析
    """

    def __init__(self):
        self.data_path = path = 'usagov_bitly_data2012-03-16-1331923249.txt'
        self.records = {}

    def get_data(self):
        """
        获取数据
        :return:
        """
        self.records = [json.loads(line) for line in open(self.data_path)]

    def data_analysis(self):
        """
        数据分析
        :return:
        """
        frame = pd.DataFrame(self.records)
        frame.info()
        print(frame.head())
        """可视化示例数据中排名前十的时区"""
        plt.figure(figsize=(10, 4))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        tz_counts = frame['tz'].value_counts()
        print(tz_counts[:10])
        subset = tz_counts[:10]  # 将前十数据进行可视化
        sns.barplot(y=subset.index, x=subset.values)
        plt.title('排名前十的时区可视化')
        plt.show()

        """统计Windows和非Windows平台用户行为数据"""
        cframe = frame[frame.a.notnull()]
        cframe['os'] = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')
        by_tz_os = cframe.groupby(['tz', 'os'])
        agg_counts = by_tz_os.size().unstack().fillna(0)
        indexer = agg_counts.sum(1).argsort()
        count_subset = agg_counts.take(indexer[-10:])
        count_subset = count_subset.stack()
        count_subset.name = 'total'
        count_subset = count_subset.reset_index()
        plt.figure()
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        sns.barplot(x='total', y='tz', hue='os', data=count_subset)
        plt.title('排名前十的时区Windows和非Windows的统计数据')
        plt.show()

        """统计Windows和非Windows平台用户行为占比数据"""

        def norm_total(group):
            group['normed_total'] = group.total / group.total.sum()
            return group
        results = count_subset.groupby('tz').apply(norm_total)
        plt.figure()
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        sns.barplot(x='normed_total', y='tz', hue='os', data=results)
        plt.title('排名前十的时区Windows和非Windows的占比数据')
        plt.show()


if __name__ == '__main__':
    analysis_assigned = AnalysisAssigned()
    analysis_assigned.get_data()
    analysis_assigned.data_cleaning()
    # analysis_assigned.model_train()
    analysis_assigned.data_analysis()

    # analysis_free = AnalysisFree()
    # analysis_free.get_data()
    # analysis_free.data_analysis()
