import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 4 (Statistics for Categorical Variables and Data Transformation – I)\ACP (Statistics for Categorical Variables and Data Transformation)\dataset.csv')

print(data.head())
print(data.info())

print(data.isnull().sum())
data = data.dropna()

print("Frequency of Categories of Genre :")
print(data['Genre'].value_counts())

categories = ['Fiction', 'Non Fiction']
data['Genre'] = pd.Categorical(data['Genre'], categories=categories, ordered=True)
median_index = np.median(data['Genre'].cat.codes)
median_cat = categories[int(median_index)]
print("Median Value of Genre is :", median_cat)

sns.countplot(x='Genre', data=data, palette='winter', hue='Genre', legend=False)
plt.show()

data.groupby('Genre', observed=False).size().plot(kind='pie', autopct='%.2f')
plt.ylabel('')
plt.show()

num_data = data[['User Rating', 'Reviews', 'Price', 'Year']]

for col in num_data.columns:
    plt.boxplot(num_data[col])
    plt.title(f'Spread of {col}')
    plt.show()

scaler = StandardScaler()
scaled_num_data = scaler.fit_transform(num_data)

print("Scaled Data Shape:", scaled_num_data.shape)
print("First 5 rows of scaled data:\n", scaled_num_data[:5])