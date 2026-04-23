import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 5 (Advanced Data Transformation and Association between Variables)\Activity 2 (Titanic Survival Prediction)\dataset.csv')

print(data.head(5))

sns.boxplot(data=data, x='Embarked', y='Age')
plt.title('Association between Embarked and Age')
plt.show()

plt.scatter(x=data['Fare'], y=data['Survived'])
plt.ylabel('Survived')
plt.xlabel('Fare')
plt.title('Association between Fare and Survived')
plt.show()

plt.scatter(x=data['Parch'], y=data['Survived'])
plt.ylabel('Survived')
plt.xlabel('Parch')
plt.title('Association between Parch and Survived')
plt.show()

plt.scatter(x=data['SibSp'], y=data['Survived'])
plt.ylabel('Survived')
plt.xlabel('SibSp')
plt.title('Association between SibSp and Survived')
plt.show()

association_categorical = pd.crosstab(data['Gender'], data['Embarked'])
print(association_categorical)

sns.heatmap(association_categorical, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Association between Gender and Embarked')
plt.show()