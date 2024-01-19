import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('../data/sample.csv')

# 删除任意有空值的数据
df = df.dropna(axis=0, how="any")

# print("*"*100)
# print(df.describe())
# print("*"*100)
# print(df.columns)
# print("*"*100)
# print(df.head(2))

# 进行初步的有意义的数据拆分
# 个人信息数据集：
# 个人编码，是否挂号，RES
personal_info_df = df[['个人编码', '是否挂号', 'RES']]

# 就诊信息数据集：
# 一天去两家医院的天数 到 医院_就诊天数_AVG
# 就诊次数_SUM 到 月就诊次数_AVG
# 出院诊断病种名称_NN 到 出院诊断LENTH_MAX
visit_info_df = df.iloc[:, 1:26]

# 费用信息数据集：
# 住院天数_SUM 到 本次审批金额_SUM
# 补助审批金额_SUM 到 城乡优抚补助_SUM
expense_info_df = df.iloc[:, 26:61]

# 费用占比信息数据集：
# 起付线标准金额_MAX 到 个人支付治疗费用占比
expense_ratio_info_df = df.iloc[:, 61:69]

# 其他信息数据集：
# BZ_民政救助 到 是否挂号
other_info_df = df.iloc[:, 69:]

