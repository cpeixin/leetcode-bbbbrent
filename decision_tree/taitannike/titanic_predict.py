import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

"""
将空值用此列最多值来补齐
index 获取索引值。 [num] 下标获取返回值 ，ascending=True 降序排列
"""
train_data['Embarked'].fillna(train_data['Embarked'].value_counts().index[0], inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].value_counts().index[0], inplace=True)

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

train_features = train_data[features]
train_labels = train_data['Survived']

test_features = test_data[features]


dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))

# 构造ID3决策树
clf = DecisionTreeClassifier(criterion='entropy')
# 决策树训练
clf.fit(train_features, train_labels)

test_features=dvec.transform(test_features.to_dict(orient='record'))

# 决策树预测
# pred_labels = clf.predict(test_features)
# # 得到决策树准确率
# acc_decision_tree = round(clf.score(train_features, train_labels), 6)
# print(u'score准确率为 %.4lf' % acc_decision_tree)



import numpy as np
from sklearn.model_selection import cross_val_score
# 使用K折交叉验证 统计决策树准确率
print(u'cross_val_score准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))