import pandas as pd


train_data = pd.read_csv('train.csv')

print(train_data.info())
print("===========================================")
print(train_data.describe())

print("===========================================")

print(train_data.describe(include=['O']))

print("===========================================")

print(train_data.head())

print("===========================================")

print(train_data.tail())