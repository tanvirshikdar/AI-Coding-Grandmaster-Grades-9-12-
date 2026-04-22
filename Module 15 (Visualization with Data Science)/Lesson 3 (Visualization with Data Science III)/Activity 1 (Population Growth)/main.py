import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 3 (Visualization with Data Science III)\Activity 1 (Population Growth)\dataset.csv"

countries = pd.read_csv(file_path)
print(countries.head(3))

c_52 = countries.loc[countries['year'] == 1952]
c_07 = countries.loc[countries['year'] == 2007]

c_merge = c_52.merge(c_07, left_on='country', right_on='country')

c_merge = c_merge.drop(['year_x', 'year_y'], axis=1)

c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']

c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)

names = c_merge['country']
pop_grow = (c_merge['population_growth'] / 10**6)

plt.figure(figsize=(15,9))
plt.bar(names, pop_grow, width=0.6, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title('Top 10 Countries w/ the Biggest Population Growth from 1952 to 2007')
plt.xticks(rotation=45)

for x, y in zip(names, pop_grow):
    label = "{:.2f}".format(y)
    plt.annotate(label, 
                 (x, y), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center')

plt.tight_layout()
plt.show()