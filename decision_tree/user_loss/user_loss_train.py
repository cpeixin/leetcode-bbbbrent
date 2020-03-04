"""https://zhuanlan.zhihu.com/p/31196728?utm_medium=social&utm_source=wechat_session"""
import pandas as pd
import numpy as np
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

# print(X)

"""
构建目标数据, 用户是否流失标签
"""
y = df.Exited

# print(y)


"""Geography和Gender两项数据都不符合要求。它们都是分类数据。我们需要做转换，把它们变成数值

"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder1 = LabelEncoder()
X.Geography= labelencoder1.fit_transform(X.Geography)
labelencoder2 = LabelEncoder()
X.Gender = labelencoder2.fit_transform(X.Gender)

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
"""
[1.0000000e+00 0.0000000e+00 0.0000000e+00 6.1900000e+02 0.0000000e+00
 4.2000000e+01 2.0000000e+00 0.0000000e+00 1.0000000e+00 1.0000000e+00
 1.0000000e+00 1.0134888e+05]
 
 
 delete after:
 
 [0.0000000e+00 0.0000000e+00 6.1900000e+02 0.0000000e+00 4.2000000e+01
 2.0000000e+00 0.0000000e+00 1.0000000e+00 1.0000000e+00 1.0000000e+00
 1.0134888e+05]
"""
X = np.delete(X, [0], 1)

"""标签变成 列向量"""
y = y[:, np.newaxis]


onehotencoder = OneHotEncoder()
"""标签为类别数据，也需要进行转换"""
y = onehotencoder.fit_transform(y).toarray()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""特征矩阵 标准化处理"""
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""创建模型"""
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

"""测试数据预测"""
y_pred = clf.predict(X_test)

"""生成报告"""
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


"""
              precision    recall  f1-score   support

           0       0.89      0.87      0.88      1595
           1       0.52      0.58      0.55       405

   micro avg       0.81      0.81      0.81      2000
   macro avg       0.71      0.72      0.71      2000
weighted avg       0.81      0.81      0.81      2000
 samples avg       0.81      0.81      0.81      2000
"""