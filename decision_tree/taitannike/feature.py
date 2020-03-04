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
print(train_features)


dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))

print(train_features)


from sklearn.feature_selection import VarianceThreshold
print(VarianceThreshold(threshold=3).fit_transform(train_features))
#
#
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
#
# # 选择K个最好的特征，返回选择特征后的数据
# print(SelectKBest(chi2,k=2).fit_transform(iris.data,iris.target))