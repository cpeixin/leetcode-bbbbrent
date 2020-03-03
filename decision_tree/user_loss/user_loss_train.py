"""https://zhuanlan.zhihu.com/p/31196728?utm_medium=social&utm_source=wechat_session"""
import pandas as pd

df = pd.read_csv('customer_churn.csv')


"""
行号，客户编号，姓氏，信用评分，地理，性别，年龄，当了本银行多少年用户，余额，使用产品数量，是否有本行信用卡，是否活跃，估计薪水，是否流失

RowNumber：行号，这个肯定没用，删除
CustomerID：用户编号，这个是顺序发放的，删除
Surname：用户姓名，对流失没有影响，删除
CreditScore：信用分数，这个很重要，保留
Geography：用户所在国家/地区，这个有影响，保留
Gender：用户性别，可能有影响，保留
Age：年龄，影响很大，年轻人更容易切换银行，保留
Tenure：当了本银行多少年用户，很重要，保留
Balance：存贷款情况，很重要，保留
NumOfProducts：使用产品数量，很重要，保留
HasCrCard：是否有本行信用卡，很重要，保留
IsActiveMember：是否活跃用户，很重要，保留
EstimatedSalary：估计收入，很重要，保留
Exited：是否已流失，这将作为我们的标签数据

"""

"""
构建特征矩阵
data.loc[:,['column_name']] 提取列值"""

X = df.loc[:,['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']]

print(X)

"""
构建目标数据, 用户是否流失标签
"""
y = df.Exited

print(y)


"""Geography和Gender两项数据都不符合要求。它们都是分类数据。我们需要做转换，把它们变成数值

"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder1 = LabelEncoder()
X.Geography= labelencoder1.fit_transform(X.Geography)
X.Gender = labelencoder1.fit_transform(X.Gender)

print(X.head())