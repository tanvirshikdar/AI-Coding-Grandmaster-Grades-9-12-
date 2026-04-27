import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import os

folder_path = r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 19 (Machine Learning - II)\Lesson 6 (Recommendation engine part – 2)\Activity 1 (Make a recommendation Engine Model)'

ratings_df = pd.read_csv(os.path.join(folder_path, 'ratings.csv'))
movies_df = pd.read_csv(os.path.join(folder_path, 'movies.csv'))

movies_df['year'] = movies_df.title.str.extract(r'(\(\d\d\d\d\))', expand=True)
movies_df['year'] = movies_df.year.str.extract(r'(\d\d\d\d)', expand=True)
movies_df['title'] = movies_df.title.str.replace(r'(\(\d\d\d\d\))', '', regex=True)
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
movies_df['genres'] = movies_df.genres.str.split('|')

movies_copy = movies_df.copy()

for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1

movies_copy = movies_copy.fillna(0)
ratings_df = ratings_df.drop(['timestamp'], axis=1)

user_input = [
    {'title': 'Grand Slam', 'rating': 5.6},
    {'title': 'Zero', 'rating': 7},
    {'title': 'Jumanji', 'rating': 8.5},
    {'title': 'Toy Story', 'rating': 4.5}
]

movies_input = pd.DataFrame(user_input)
input_id = movies_df[movies_df['title'].isin(movies_input['title'].tolist())]
movies_input = pd.merge(input_id, movies_input)
movies_input = movies_input.drop(['genres', 'year'], axis=1)

movies_user = movies_copy[movies_copy['movieId'].isin(movies_input['movieId'].tolist())]
movies_user = movies_user.reset_index(drop=True)
UserGenreTable = movies_user.drop(['movieId', 'title', 'genres', 'year'], axis=1)

UserProfile = UserGenreTable.transpose().dot(movies_input['rating'])

GenreTable = movies_copy.set_index(movies_copy['movieId'])
GenreTable = GenreTable.drop(['movieId', 'title', 'genres', 'year'], axis=1)

Recommendation_df = ((GenreTable * UserProfile).sum(axis=1)) / UserProfile.sum()
Recommendation_df = Recommendation_df.sort_values(ascending=False)

RecommendationTable = movies_df.loc[movies_df['movieId'].isin(Recommendation_df.head(20).keys())]
print(RecommendationTable)