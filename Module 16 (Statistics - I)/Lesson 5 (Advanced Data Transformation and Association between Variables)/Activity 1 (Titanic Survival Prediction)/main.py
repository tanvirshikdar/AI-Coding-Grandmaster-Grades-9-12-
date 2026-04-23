import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 5 (Advanced Data Transformation and Association between Variables)\Activity 1 (Titanic Survival Prediction)\dataset.csv')

print(data.head(5))

minimum_age = data['Age'].min()
print('Minimum Age :', minimum_age)

maximum_age = data['Age'].max()
print('Maximum Age :', maximum_age)

bins = [0, 15, 30, 45, 60, 80]
age_labels = ['Young', 'Young - Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']

data['binned_age'] = pd.cut(data['Age'], bins=bins, labels=age_labels)
print(data[['binned_age', 'Age']].head())

data['binned_age'].value_counts().plot(kind='bar')
plt.title('Age Distribution')
plt.xlabel('Ages')
plt.ylabel('Count')
plt.show()

labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for label in labels:
    print('Distribution of', label)
    sns.histplot(data[label], kde=True)
    plt.show()
    print('Skewness -', data[label].skew())

data['log_SibSp'] = np.log1p(data['SibSp'])
data['log_Parch'] = np.log1p(data['Parch'])
data['log_Fare'] = np.log1p(data['Fare'])

print(data[['log_SibSp', 'log_Parch', 'log_Fare']].head())