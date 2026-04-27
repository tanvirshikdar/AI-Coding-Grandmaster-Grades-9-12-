import imblearn
from pandas import read_csv
from collections import Counter
from matplotlib import pyplot
from sklearn.preprocessing import LabelEncoder

path = r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 19 (Machine Learning - II)\Lesson 1 (Classification Analysis)\ACP (Data Classification)\dataset.csv'

df = read_csv(path, header=None)
data = df.values

X, y = data[:, :-1], data[:, -1]

y = LabelEncoder().fit_transform(y)

counter = Counter(y)
for k,v in counter.items():
    per = v / len(y) * 100
    print('Class=%d, n=%d (%.3f%%)' % (k, v, per))

pyplot.bar(counter.keys(), counter.values())
pyplot.show()