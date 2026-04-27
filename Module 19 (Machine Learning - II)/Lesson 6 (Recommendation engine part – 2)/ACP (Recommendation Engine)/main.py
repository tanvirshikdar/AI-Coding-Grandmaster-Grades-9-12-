import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_url = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
data = pd.read_csv(data_url, sep='\t', names=column_names)

titles_url = 'https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv'
movie_titles = pd.read_csv(titles_url)

data = pd.merge(data, movie_titles, on='item_id')

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

sns.set_style('white')

plt.figure(figsize=(10, 4))
ratings['num of ratings'].hist(bins=70)
plt.title('Number of Ratings Distribution')
plt.show()

plt.figure(figsize=(10, 4))
ratings['rating'].hist(bins=70)
plt.title('Average Rating Distribution')
plt.show()

moviemat = data.pivot_table(index='user_id', columns='title', values='rating')

starwars_user_ratings = moviemat['Star Wars (1977)']
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars = corr_starwars.join(ratings['num of ratings'])

print("Top Recommendations for Star Wars (1977):")
print(corr_starwars[corr_starwars['num of ratings'] > 100].sort_values('Correlation', ascending=False).head())

liarliar_user_ratings = moviemat['Liar Liar (1997)']
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])

print("\nTop Recommendations for Liar Liar (1997):")
print(corr_liarliar[corr_liarliar['num of ratings'] > 100].sort_values('Correlation', ascending=False).head())