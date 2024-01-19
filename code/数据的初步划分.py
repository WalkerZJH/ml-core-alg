import pandas as pd
# 对数据进行训练集和测试集的划分，并首先只使用少量数据进行测试。


df = pd.read_csv("../data/complete.csv")
# index=False 表示行索引不加入
df.head(1600).to_csv("../data/sample.csv", index=False)
