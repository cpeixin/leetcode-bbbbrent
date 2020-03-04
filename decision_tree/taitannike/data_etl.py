import pandas as pd

train_data = pd.read_csv('train.csv')

train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)

train_data['Embarked'].fillna('S', inplace=True)