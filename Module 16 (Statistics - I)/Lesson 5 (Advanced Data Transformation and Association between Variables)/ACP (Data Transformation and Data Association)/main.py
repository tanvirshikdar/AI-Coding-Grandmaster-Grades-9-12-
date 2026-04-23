import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 5 (Advanced Data Transformation and Association between Variables)\ACP (Data Transformation and Data Association)\dataset.csv')

print(data.head())
print(data.info())
print(data.isnull().any())

print(data['Genre'].value_counts())

min_rating = data['User Rating'].min()
max_rating = data['User Rating'].max()
print("Minimum Rating:", min_rating)
print("Maximum Rating:", max_rating)

bins = [0, 4.4, 5.0]
rating_labels = ['Good', 'Excellent']
data['binned_rating'] = pd.cut(data['User Rating'], bins=bins, labels=rating_labels)

print(data[['User Rating', 'binned_rating']].head())

num_labels = ['User Rating', 'Reviews', 'Price', 'Year']

for l in num_labels:
    sns.histplot(data[l], kde=True)
    plt.title(f'Distribution of {l}')
    plt.show()
    print(f"Skewness of {l}: {data[l].skew()}")

data['log_Reviews'] = np.log1p(data['Reviews'])
data['log_Price'] = np.log1p(data['Price'])

sns.boxplot(data=data, x='Genre', y='User Rating')
plt.title('Association between Genre and User Rating')
plt.show()

plt.scatter(x=data['User Rating'], y=data['Price'])
plt.xlabel('User Rating')
plt.ylabel('Price')
plt.title('Association between User Rating and Price')
plt.show()

association_genre_rating = pd.crosstab(data['Genre'], data['binned_rating'])
print(association_genre_rating)