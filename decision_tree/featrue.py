from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import load_iris
# 方差选择法，返回值为特征选择后的数据
# 参数threshold为方差的阈值

iris=load_iris()
print(iris.data)
print(VarianceThreshold(threshold=3).fit_transform(iris.data))


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# 选择K个最好的特征，返回选择特征后的数据
print(SelectKBest(chi2,k=2).fit_transform(iris.data,iris.target))