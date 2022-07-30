"""读取数据"""
import pandas as pd

# 数据路径
file_path = 'data(1).xlsx'
# 需要解析日期的列
parse_dates = ['Inspection_Date', 'Date_Keel', 'Date_Inspection', 'date of last initial inspection']
# 读取数据并解析日期
data = pd.read_excel(file_path, parse_dates=parse_dates)
print(data.columns)
# 重命名RO为RO_Performance
data.rename(columns={'RO': 'RO_Performance'}, inplace=True)
# 本次实验只需要使用Inspection_Type==initial inspection的数据
data = data[data['Inspection_Type'] == 'initial inspection']
# data.loc[data['SRP'] == 'N.A.', 'SRP'] = 'Standard Risk Ship'
data['SRP'][data['SRP'] == 'N.A.'] = 'Standard Risk Ship'


def print_with_prefix(desc: str) -> None:
    prefix = '-' * 20
    print('\n%s%s%s\n' % (prefix, desc, prefix))


"""查看数据"""
print_with_prefix('1、预览数据的前3行')
print(data.head(3))

print_with_prefix('2、查看数据的列名')
print(list(data.columns))

print_with_prefix('3、查看样本数和特征数')
print(data.shape)

print_with_prefix('4、数据的描述性统计')
print(data.describe())

print_with_prefix('5、查看数据缺失情况')
data.info()

"""删除无用特征 & 提取新特征"""
##  1、业务不相关的特征
irrelevant_columns = ['Call_Sign', 'Inspection_Type', 'Flag', 'IMO number', 'MMSI', 'No', 'Draft']
##  2、缺失过多，意义不大的特征
missing_too_much_columns = ['Liquid']
## 3、高度相关的特征
# Tonnage和deadweight高度相关，只保存deadweight
redundant_columns = ['Tonnage']

drop_columns = []
drop_columns.extend(irrelevant_columns)
drop_columns.extend(missing_too_much_columns)
drop_columns.extend(redundant_columns)

data = data.drop(columns=drop_columns, axis=1)
print('删除无用特征后还剩以下字段：')
list(data.columns)
print(list(data.columns))

"""提取新特征"""


# 1、计算过去3年检测出来的平均缺陷数last_36_months_avg_def_no
def f(x):
    if x is None or x == '' or x == 'none':
        return x
    xs = str(x).strip().split(' ')
    return sum(list(map(int, xs))) / len(xs)


data['last_36_months_avg_def_no'] = data['last_36_months_def_no'].map(f)


# 2、计算过去3年被扣留的总次数last_36_months_all_det_no
def g(x):
    xs: list = x.split(' ')
    return xs.count('yes')


data['last_36_months_all_det_no'] = data['last_36_months_det'].map(g)

print('提取新特征后还有以下特征：')
list(data.columns)

"""划分数据集"""
# train 60% valid 20% test 20%
from sklearn.model_selection import train_test_split

# 用于聚类的数据需要用data_for_cluster(删除Code和Detainable_Code字段)，之后计算每个类对应的code数量时再用data
data_copy = data.copy()
# data = data.drop(columns=['Code', 'Detainable_Code'], axis=1)
train_valid, test = train_test_split(data, test_size=0.2, random_state=1)
train, valid = train_test_split(train_valid, test_size=0.25, random_state=2)
print('划分后的训练集: %s, 验证集:%s, 测试集:%s' % (train.shape, valid.shape, test.shape))

"""数据处理：缺失值填充 & 编码转换"""
zipped = zip(['RO_Performance', 'flag performance', 'company performance'], ['Undefined', 'Undefined', 'Unknown'])
for column, to_filled in zipped:
    # 使用训练集出现次数最多的value作为填充值
    mode = train[column].mode()[0]
    for df in [train, test, valid]:
        df[column][df[column] == to_filled] = mode


"""将deficiency分列开并进行统计"""
def deficiency_statistics():
    initial_data = data
    initial_data = initial_data.drop(initial_data[initial_data['deficiency_no'] == 0].index)
    initial_data = initial_data.reset_index(drop=True)
    # 初始化列名和列index
    # deficiency list列名
    columns_def = ['def_01', 'def_02', 'def_03', 'def_04', 'def_05', 'def_06', 'def_07', 'def_08',
                   'def_09', 'def_10', 'def_11', 'def_12', 'def_13', 'def_14', 'def_15', 'def_18']
    # detainable deficiency list 列名
    columns_det_def = ['det_def_01', 'det_def_02', 'det_def_03', 'det_def_04', 'det_def_05', 'det_def_06', 'det_def_07',
                       'det_def_08',
                       'det_def_09', 'det_def_10', 'det_def_11', 'det_def_12', 'det_def_13', 'det_def_14', 'det_def_15',
                       'det_def_18']
    # deficiency code名字
    def_code_no = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '18']
    def_code = pd.DataFrame(columns=columns_def, index=range(0, len(initial_data), 1), data=0)  # 初始化空的DF保存def出现次数
    for index, row in initial_data.iterrows():
        code = row['Code']
        if '/' in code:  # 包含多个deficiency code
            code_split = code.split('/')
            # print(code_split)
            for code_item in code_split:
                code_no = code_item[0:2]  # 只看前2位deficiency的大类
                if code_no == '99':  # 忽略99-other相关的deficiency
                    initial_data.loc[index, 'deficiency_no'] -= 1
                    continue
                code_index = def_code_no.index(code_no)
                def_code.loc[index, columns_def[code_index]] += 1
        else:  # 只包含一个deficiency

            code_no = code[0:2]
            if code_no == '99':
                initial_data.loc[index, 'deficiency_no'] -= 1
                continue
            code_index = def_code_no.index(code_no)
            def_code.loc[index, columns_def[code_index]] += 1
    def_code["total_def"] = def_code.apply(lambda x: x.sum(), axis=1)  # 按行求和，便于与本身给出的deficiency no对比
    return def_code["total_def"]
data["deficiency_stat"] = deficiency_statistics()


# 处理[ 'last-inspection-state', 'last-deficiency-no', 'Code', 'last_36_months_avg_def_no'], 并把他们对应起来，
# 因为他们三个是相联系和对应的。具体而言，将所有的字段包含到feature里面，
# 并将没有上次检查的船的record（即有缺失的部分）用training set上的相关统计量信息进行填充
median = train['last-deficiency-no'][train['last-deficiency-no'] != 'none'].median()
median_last_36 = train['last_36_months_avg_def_no'][train['last_36_months_avg_def_no'] != 'none'].median()
mode_last_inspection_state = train['last-inspection-state'].mode()[0]
mode_detention = train['detention'].mode()[0]

for df in [train, test, valid]:
    df['last-deficiency-no'][df['last-deficiency-no'] == 'none'] = median
    df['last-inspection-state'][(df['last-inspection-state'] == 'none') | (df['last-inspection-state'].isna())] = mode_last_inspection_state
    df['last_36_months_avg_def_no'][(df['last_36_months_avg_def_no'] == 'none') | (df['last_36_months_avg_def_no'].isna())] = median_last_36
    df['detention'] = df['detention'].fillna(mode_detention)
    # 将上次检查缺陷数=0的那些记录的Code设为0
    df['Code'][df['Code'].isna()] = 0
    df['Detainable_Code'][df['Detainable_Code'].isna()] = 0

median = pd.to_datetime(
    data['date of last initial inspection'][data['date of last initial inspection'] != 'none']).median()
for df in [train, test, valid]:
    df['date of last initial inspection'] = data['date of last initial inspection'].str.replace(
        'none', str(median))
    df['date of last initial inspection'] = pd.to_datetime(df['date of last initial inspection'])
    df['last inspection time'] = (df['Inspection_Date'] - df['date of last initial inspection']).map(
        lambda x: int(x.days / 30))
    df['ship age'] = (df['Date_Inspection'] - df['Date_Keel']).map(lambda x: int(x.days / 365))

# 处理['Ship Type_PSC]
ship_type_psc_group = pd.DataFrame(train.groupby("Ship Type_PSC")['Ship Type_PSC'].count().sort_values(ascending=False))
ship_type_psc_top = ship_type_psc_group[0:3].index.tolist()
ship_type_psc_top1 = ship_type_psc_top[0]
ship_type_psc_top2 = ship_type_psc_top[1]
ship_type_psc_top3 = ship_type_psc_top[2]
keep_ships = ['Oil tanker', 'Chemical tanker', 'Oil tanker/Chemical tanker (OILCHEM)']
passenger_ships = ['Passenger ship', 'Ro-Ro passenger ship']


def change_ship(x):
    if x in keep_ships:
        return "tanker ship"
    elif x in passenger_ships:
        return "passenger ship"
    elif x == ship_type_psc_top1:
        return str(ship_type_psc_top1)
    elif x == ship_type_psc_top2:
        return str(ship_type_psc_top2)
    elif x == ship_type_psc_top3:
        return str(ship_type_psc_top3)
    else:
        return "other"


for df in [train, test, valid]:
    df['Ship Type_PSC'] = df['Ship Type_PSC'].apply(change_ship)

# 对变量[ 'company performance', 'RO_Performance', 'flag performance']进行缺失值填充
columns_to_filled = ['company performance', 'RO_Performance', 'flag performance']
for df in [train, test, valid]:
    for column in columns_to_filled:
        mode = train[column][~train[column].isna()].mode()[0]
        df[column] = df[column].fillna(mode)

"""
对变量[ 'flag performance', 'RO_Performance', 'company performance', 'detention', 'last-inspection-state']进行Label编码
不是直接用的label encoder，而是直接规定某一个值编码为什么，例如flag_performance_white = 1, flag_performance_gray = 2, flag_performance_black = 3。
如果直接用label encoder而什么都不规定，应该是按照变量名称的字母表顺序进行编码？
如何保证编码出来的值是按照我们预想的顺序呢？
要按照这三个字段的取值顺序事先规定好几代表几，然后进行编码
"""
label_encode_columns = ['flag performance', 'RO_Performance',
                        'company performance', 'detention', 'last-inspection-state']

# 自定义编码的值
label_dic = {
    'flag performance': {'Black': 3, 'Grey': 2, 'White': 1},
    'RO_Performance': {'High': 1, 'Medium': 2},
    'company performance': {'High': 1, 'Low': 3, 'Medium': 2, 'Very Low': 4},
    'detention': {'no': 0, 'yes': 1},
    'last-inspection-state': {'no': 0, 'none': 3, 'yes': 1}
}


def label_encode_func(x, dic):
    return dic.get(x)


for df in [train, test, valid]:
    for column in label_encode_columns:
        df[column] = df[column].map(lambda x: label_encode_func(x, label_dic[column]))

# 对变量['Ship Type_PSC']进行onehot编码
from sklearn.preprocessing import OneHotEncoder

onehot_encode_columns = ['Ship Type_PSC']

ohe = OneHotEncoder()


def onehot_encode(df: pd.DataFrame) -> pd.DataFrame:
    ohe_matrix = ohe.fit_transform(df[onehot_encode_columns])
    new_columns = ohe.get_feature_names_out()
    df_ohe = pd.DataFrame(ohe_matrix.toarray(),
                          columns=new_columns,
                          index=df.index)
    print("新的编码名称:", new_columns)
    # 再删除原有编码前的字段
    df = df.drop(columns=onehot_encode_columns, axis=1)
    df = pd.concat([df, df_ohe], axis=1)
    return df


train = onehot_encode(train)
test = onehot_encode(test)
valid = onehot_encode(valid)

# 填充变量['Length', 'Beam', 'Depth', 'Speed', 'DeadWeight']的缺失值
# 处理DeadWeight字段
import numpy as np

data['DeadWeight'][data['DeadWeight'] == 'N.A.'] = np.nan
data['DeadWeight'] = data['DeadWeight'].astype(np.float64)

# 按均值填充Length、Beam、Depth、Speed、DeadWeight的缺失记录
for column in ['Length', 'Beam', 'Depth', 'Speed', 'DeadWeight']:
    for df in [train, valid, test]:
        df['DeadWeight'][df['DeadWeight'] == 'N.A.'] = np.nan
        df['DeadWeight'] = df['DeadWeight'].astype(np.float64)
        df[column] = df[column].fillna(train[column].mean())

"""建立模型 & 模型效果评估"""
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

model = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=3))])
# 最终用于训练的columns
final_columns = train.drop(
    columns=['Code', 'Detainable_Code', 'Inspection_Date', 'Classification_Society', 'Date_Keel', 'Date_Inspection',
             'date of last initial inspection', 'last_36_months_def_no', 'last_36_months_det', 'SRP',
             'deficiency_no', 'detention'],
    axis=1).columns
train_data = train[final_columns]
print("训练集的数组结构：", train_data.shape)
print("训练集的特征有:", train_data.columns)
model.fit(train_data.astype(float))
# 训练数据的label
train_label = model.predict(train_data.astype(float))
train['y_pred'] = train_label.tolist()
train['SRP'] = data['SRP'].loc[train.index]
train_data['y_pred'] = train_label.tolist()
print(train_label)
for i in range(0, len(model[1].cluster_centers_)):
    print("中心点坐标:", model[1].cluster_centers_[i])

"""显著性检验"""
import scipy.stats as stats

"""将每个cluter数据划分出来"""
train_data_0 = train_data[train_data['y_pred'] == 0][final_columns]
train_data_1 = train_data[train_data['y_pred'] == 1][final_columns]
train_data_2 = train_data[train_data['y_pred'] == 2][final_columns]

arr_0 = sum(train_data_0.values.tolist(), [])
arr_1 = sum(train_data_1.values.tolist(), [])
arr_2 = sum(train_data_2.values.tolist(), [])

t01, p01 = stats.ttest_ind(arr_0, arr_1)
t02, p02 = stats.ttest_ind(arr_0, arr_2)
t12, p12 = stats.ttest_ind(arr_1, arr_2)
print("cluter0和cluter1的显著T,P值：", t01, p01)
print("cluter0和cluter2的显著T,P值：", t02, p02)
print("cluter1和cluter2的显著T,P值：", t12, p12)

"""计算训练集的SRP的众数"""
# 先计算train里的三种SRP对应的数量
frequence = data.loc[train.index, 'SRP'].value_counts()
# 再计算每个cluster的众数
modes = {}
for label in range(3):
    value_counts = data['SRP'].loc[train[train['y_pred'] == label].index].value_counts()
    print('\n------频数（label == %s）------\n' % label)
    print(value_counts)
    print('\n------频率（label == %s）------\n' % label)
    print(value_counts / value_counts.sum())
    # 按占比来计算其属于哪一类
    result = value_counts / frequence
    mode = result.index[result.argmax()]
    modes[label] = mode
print("modes", modes)
"""计算每个cluster里面船舶的总的deficiency number的平均数（总deficiency number除以船的数量"""
avg_deficiency_no = {}
for label in range(3):
    avg = train['deficiency_no'][train['y_pred'] == label].mean()
    avg_deficiency_no[label] = avg
print("avg_deficiency_no:", avg_deficiency_no)

"""统计每个船舶检查记录里面每个deficiency code下面分别有多少deficiency number"""
def compute_code_cnt_top2(col, label):
    """
    统计每个cluter中每个code(前2位)出现的次数
    Args:
        col: 列名

    Returns:
    每个cluter每个code(前2位)出现的次数的字典
    """
    from collections import Counter
    code_noe = []
    for code in train[col][train['y_pred'] == label]:
        if code == 0:
            continue
        else:
            x = code.split('/')
            for i in range(0, len(x)):
                code_noe.append(x[i][0] + x[i][1])  # 取每个code前2位数字
    return dict(Counter(code_noe))


for label in range(3):
    code_cnt_top2_dict = compute_code_cnt_top2('Code', label)
    print("cluter%s的code下的deficiency numbe统计结果：" % label)
    print(code_cnt_top2_dict)
    print("==================================")

"""统计每个cluster中所包含船舶对于每个detainable deficiency code下的平均deficiency number"""
for label in range(3):
    cluter_deficiency_no_cnt = train['deficiency_no'][train['y_pred'] == label].sum()
    detainable_code_cnt_top2_dict = compute_code_cnt_top2('Detainable_Code', label)
    for key in detainable_code_cnt_top2_dict:
        detainable_code_cnt_top2_dict[key] = cluter_deficiency_no_cnt / detainable_code_cnt_top2_dict[key]
    print("cluter%s的deficiency code下的平均deficiency number统计结果：" % label)
    print(detainable_code_cnt_top2_dict)
    print("++++++++++++++++++++++++++++++++++++")

"""计算每个cluster里面船舶的总的detention number的平均数（总deficiency number除以船的数量"""
avg_detention = {}
median_detention = {}
print(train['detention'])
for label in range(3):
    avg = train['detention'][train['y_pred'] == label].mean()
    median = train['detention'][train['y_pred'] == label].median()
    avg_detention[label] = avg
    median_detention[label] = median
print("avg_detention:", avg_detention)
print("median_detention:", median_detention)

"""计算Detainable_Code均值"""
from collections import Counter

detainable_code_label = {}
code_label = {}


def compute_code_label(col, map):
    """
    计算detainable_code、code的cluterlabel
    Args:
        col: 列名
        map: 返回的map

    Returns:

    """
    for label in range(3):
        code_list = []
        cluter_data = train[col][train['y_pred'] == label]
        for i in cluter_data:
            if i != 0:
                x = i.split('/')
                for j in x:
                    code_list.append(j)
        code_avg_dict = {}
        code_cnt_dict = dict(Counter(code_list))
        for k, v in code_cnt_dict.items():
            code_avg_dict[k] = v / len(train)
        # 排序后的数字组
        code_sort_list = sorted(code_avg_dict.items(), key=lambda item: item[1], reverse=True)
        # 判断最大值和第二大值相差多少，如果相差0.5倍以下，将最大值、第二大值的key都加入labl，如果大于0.5倍，只加入最大值的key
        list_temp = []
        if code_sort_list[0][1] * 0.5 < code_sort_list[1][1]:
            list_temp.append(code_sort_list[0][0])
            list_temp.append(code_sort_list[1][0])
        else:
            list_temp.append(code_sort_list[0][0])
        map[label] = list_temp


compute_code_label('Detainable_Code', detainable_code_label)
compute_code_label('Code', code_label)
print("detainable_code_label", detainable_code_label)
print("code_label", code_label)

#  1、SRP：带加权的众数作为label，label和原来的特征一致则为准确
correct_number = [len(train[(train['y_pred'] == i) & (train['SRP'] == modes[i])]) for i in range(3)]
accuracy_srp = sum(correct_number) / len(train)
print("accuracy_srp:", accuracy_srp)


from sklearn.metrics import mean_squared_error
detention_no_mse = 0
for label in range(3):
    lengh = len(train['deficiency_no'][train['y_pred'] == label])
    y = []
    for i in range(0, lengh):
        y.append(avg_deficiency_no[label])
    print("cluter%s mean_squared_error:" % label, mean_squared_error(train['deficiency_no'][train['y_pred'] == label], y))
    detention_no_mse += mean_squared_error(train['deficiency_no'][train['y_pred'] == label], y)
print("detention_no_mse", detention_no_mse)
# 2、deficiency_no: 真实的船的deficiency_no值在该类平均值的上下80%范围内则可视为准确
# count = 0
# for i in train.index:
#     y_pred = train.loc[i, 'y_pred']
#     range_ = avg_deficiency_no[y_pred] * 0.8, avg_deficiency_no[y_pred] * 1.8
#     if range_[0] <= train.loc[i, 'deficiency_no'] <= range_[1]:
#         count += 1
# accuracy_deficiency_no = count / len(train)
# print("accuracy_deficiency_no:", accuracy_deficiency_no)

# 3、detention_mse
from sklearn.metrics import mean_squared_error
detention_mse = 0
for label in range(3):
    lengh = len(train['detention'][train['y_pred'] == label])
    y = []
    for i in range(0, lengh):
        y.append(avg_deficiency_no[label])
    print("cluter%s mean_squared_error:" %label, mean_squared_error(train['detention'][train['y_pred'] == label], y))
    detention_mse += mean_squared_error(train['detention'][train['y_pred'] == label], y)
print("detention_mse", detention_mse)
# 3、由于avg_detention可知cluter0的均值是其他簇的十倍，又由于detention中位数是0，所以在cluter0中的值为1为正确，在cluter1、2为0为正确
# for i in train.index:
#     y_pred = train.loc[i, 'y_pred']
#     if (y_pred == 0 and train.loc[i, 'detention'] == 1) or (y_pred != 1 and train.loc[i, 'detention'] == 0):
#         count += 1
# accuracy_detention = count / len(train)
# print("accuracy_detention:", accuracy_detention)

# 4、通过 detainable_code_label来判断准确率
count = 0
for i in train.index:
    y_pred = train.loc[i, 'y_pred']
    if train.loc[i, 'Detainable_Code'] != 0:
        # 取交集
        res = [v for v in detainable_code_label[y_pred] if v in train.loc[i, 'Detainable_Code'].split('/')]
        if len(res) > 0:
            count += 1
accuracy_detainable_code = count / len(train)
print("accuracy_detainable_code:", accuracy_detainable_code)

# 5、通过code_label来判断准确率
count = 0
for i in train.index:
    y_pred = train.loc[i, 'y_pred']
    if train.loc[i, 'Code'] != 0:
        # 取交集
        res = [v for v in code_label[y_pred] if v in train.loc[i, 'Code'].split('/')]
        if len(res) > 0:
            count += 1
accuracy_code = count / len(train)
print("accuracy_code:", accuracy_code)

"""test数据预测"""
final_columns_test = test.drop(
    columns=['Code', 'Detainable_Code', 'Inspection_Date', 'Classification_Society', 'Date_Keel', 'Date_Inspection',
             'date of last initial inspection', 'last_36_months_def_no', 'last_36_months_det', 'SRP',
             'deficiency_no', 'detention'],
    axis=1).columns
test_data = test[final_columns_test]
test_data['Ship Type_PSC_passenger ship'] = train_data['Ship Type_PSC_passenger ship'][:len(test_data)].values
print("预测集的数组结构：", test_data.shape)
print("预测集的特征有:", test_data.columns)
test_label = model.predict(test_data.astype(float))
test['y_pred'] = test_label.tolist()
test['SRP'] = data['SRP'].loc[test.index]

"""用test数据算5个label的准确率"""
"""计算test集的SRP的众数"""
# 先计算train里的三种SRP对应的数量
frequence = data.loc[train.index, 'SRP'].value_counts()
# 再计算每个cluster的众数
modes_test = {}
for label in range(3):
    value_counts = data['SRP'].loc[test[test['y_pred'] == label].index].value_counts()
    print('\n------频数（label == %s）------\n' % label)
    print(value_counts)
    print('\n------频率（label == %s）------\n' % label)
    print(value_counts / value_counts.sum())
    # 按占比来计算其属于哪一类
    result = value_counts / frequence
    mode = result.index[result.argmax()]
    modes_test[label] = mode
print("modes_test", modes_test)
"""计算每个cluster里面船舶的总的deficiency number的平均数（总deficiency number除以船的数量"""
avg_deficiency_no_test = {}
for label in range(3):
    avg = test['deficiency_no'][test['y_pred'] == label].mean()
    avg_deficiency_no_test[label] = avg
print("avg_deficiency_no_test:", avg_deficiency_no_test)

"""计算每个cluster里面船舶的总的detention number的平均数（总deficiency number除以船的数量"""
avg_detention_test = {}
median_detention_test = {}
for label in range(3):
    avg = test['detention'][test['y_pred'] == label].mean()
    median = test['detention'][test['y_pred'] == label].median()
    avg_detention_test[label] = avg
    median_detention_test[label] = median
print("avg_detention_test:", avg_detention_test)
print("median_detention_test:", median_detention_test)

"""计算Detainable_Code均值"""
from collections import Counter

detainable_code_label_test = {}
code_label_test = {}


def compute_code_label_test(col, map):
    """
    计算detainable_code、code的cluterlabel
    Args:
        col: 列名
        map: 返回的map

    Returns:

    """
    for label in range(3):
        code_list = []
        cluter_data = test[col][test['y_pred'] == label]
        for i in cluter_data:
            if i != 0:
                x = i.split('/')
                for j in x:
                    code_list.append(j)
        code_avg_dict = {}
        code_cnt_dict = dict(Counter(code_list))
        for k, v in code_cnt_dict.items():
            code_avg_dict[k] = v / len(test)
        # 排序后的数字组
        code_sort_list = sorted(code_avg_dict.items(), key=lambda item: item[1], reverse=True)
        # 判断最大值和第二大值相差多少，如果相差0.5倍以下，将最大值、第二大值的key都加入labl，如果大于0.5倍，只加入最大值的key
        list_temp = []
        if code_sort_list[0][1] * 0.5 < code_sort_list[1][1]:
            list_temp.append(code_sort_list[0][0])
            list_temp.append(code_sort_list[1][0])
        else:
            list_temp.append(code_sort_list[0][0])
        map[label] = list_temp


compute_code_label('Detainable_Code', detainable_code_label_test)
compute_code_label('Code', code_label_test)
print("detainable_code_label_test", detainable_code_label_test)
print("code_label_test", code_label_test)

#  1、SRP：带加权的众数作为label，label和原来的特征一致则为准确
correct_number = [len(test[(test['y_pred'] == i) & (test['SRP'] == modes_test[i])]) for i in range(3)]
accuracy_srp_test = sum(correct_number) / len(test)
print("accuracy_srp_test:", accuracy_srp_test)

# 2、deficiency_no_mse_test
from sklearn.metrics import mean_squared_error
detention_no_mse_test = 0
for label in range(3):
    lengh = len(test['deficiency_no'][test['y_pred'] == label])
    y = []
    for i in range(0, lengh):
        y.append(avg_deficiency_no_test[label])
    print("cluter%s mean_squared_error:" % label, mean_squared_error(test['deficiency_no'][test['y_pred'] == label], y))
    detention_no_mse_test += mean_squared_error(test['deficiency_no'][test['y_pred'] == label], y)
print("detention_no_mse_test", detention_no_mse_test)
# 2、deficiency_no: 真实的船的deficiency_no值在该类平均值的上下80%范围内则可视为准确
# count = 0
# for i in test.index:
#     y_pred = test.loc[i, 'y_pred']
#     range_ = avg_deficiency_no_test[y_pred] * 0.8, avg_deficiency_no_test[y_pred] * 1.8
#     if range_[0] <= test.loc[i, 'deficiency_no'] <= range_[1]:
#         count += 1
# ccuracy_deficiency_no_test = count / len(test)
# print("ccuracy_deficiency_no_test:", ccuracy_deficiency_no_test)

# 3、detention_mse_test
from sklearn.metrics import mean_squared_error
detention_mse_test = 0
for label in range(3):
    lengh = len(test['detention'][test['y_pred'] == label])
    y = []
    for i in range(0, lengh):
        y.append(avg_deficiency_no_test[label])
    print("cluter%s mean_squared_error:" % label, mean_squared_error(test['detention'][test['y_pred'] == label], y))
    detention_mse_test += mean_squared_error(test['detention'][test['y_pred'] == label], y)
print("detention_mse_test", detention_mse_test)
# 3、由于avg_detention可知cluter0的均值是其他簇的十倍，又由于detention中位数是0，所以在cluter0中的值为1为正确，在cluter1、2为0为正确
# count = 0
# for i in test.index:
#     y_pred = test.loc[i, 'y_pred']
#     if (y_pred == 0 and test.loc[i, 'detention'] == 1) or (y_pred != 1 and test.loc[i, 'detention'] == 0):
#         count += 1
# accuracy_detention_test = count / len(test)
# print("accuracy_detention_test:", accuracy_detention_test)

# 4、通过 detainable_code_label来判断准确率
count = 0
for i in test.index:
    y_pred = test.loc[i, 'y_pred']
    if test.loc[i, 'Detainable_Code'] != 0:
        # 取交集
        res = [v for v in detainable_code_label_test[y_pred] if v in test.loc[i, 'Detainable_Code'].split('/')]
        if len(res) > 0:
            count += 1
accuracy_detainable_code_test = count / len(test)
print("accuracy_detainable_code_test:", accuracy_detainable_code_test)

# 5、通过code_label来判断准确率
count = 0
for i in test.index:
    y_pred = test.loc[i, 'y_pred']
    if test.loc[i, 'Code'] != 0:
        # 取交集
        res = [v for v in code_label_test[y_pred] if v in test.loc[i, 'Code'].split('/')]
        if len(res) > 0:
            count += 1
accuracy_code_test = count / len(test)
print("accuracy_code_test:", accuracy_code_test)

"""kmeans评估"""
valid_data = valid[final_columns]
inertia_scores = []
for n in range(2, 10):
    km = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=n))])
    km.fit(valid_data)
    inertia_scores.append(km[1].inertia_)

    # 轮廓系数接收的参数中，第二个参数至少有两个分类
    sc = silhouette_score(valid_data, km[1].labels_)
    # sil_scores.append(sc)
    print("n_clusters: {}\tinertia: {}\tsilhoutte_score: {}".format(
        n, km[1].inertia_, sc))
del train_data['y_pred']
train_all = train_data.append(valid_data, ignore_index=True)
model_all = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=2))])
model_all.fit(train_all)

"""训练test数据集"""
model_all.fit(test_data)