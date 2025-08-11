import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Titanic-Dataset.csv')

print(df.info())

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df.drop(columns=['Cabin'], inplace=True)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

sns.boxplot(x=df['Age'])
plt.title("Boxplot of Age")
plt.show()

sns.boxplot(x=df['Fare'])
plt.title("Boxplot of Fare")
plt.show()

df.to_csv('cleaned_titanic.csv', index=False)
print("Data preprocessing complete. Cleaned file saved as 'cleaned_titanic.csv'.")
