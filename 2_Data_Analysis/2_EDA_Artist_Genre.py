# EDA on genre
# import library
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# load the cleaned data
artist_genre_df = pd.read_csv('./Cleaned_Data/Artist_Genre_List.csv')

# split multiple-genres
artist_genre_df['genres_split'] = artist_genre_df['genres'].str.split(', ')
genre_exploded = artist_genre_df.explode('genres_split').rename(columns={'genres_split':'genre'})

# replace no genres found with NaN
genre_exploded['genres'].replace('No genres found', pd.NA, inplace= True)
genre_cleaned = genre_exploded.dropna(subset=['genre'])

# check the first few rows
print(artist_genre_df.head())

# check column types, null counts and summary stats of numeric columns 
# music tracks
print(artist_genre_df.info()) 
print(artist_genre_df.describe())  

# count genre occurances
genre_count = genre_cleaned['genre'].value_counts()
print(genre_count)

# identify top 10 genres
top_genre = genre_count.head(10)
print(top_genre)

# select top 10 genres and sort in descending order
genre_count_sorted = genre_count.sort_values(ascending=False).head(10)

# create bar plot with seaborn
sns.set(style='darkgrid')
plt.figure(figsize = (30,20))
sns.barplot(
    x=genre_count_sorted.values,
    y=genre_count_sorted.index,
    palette= 'Blues_r'
)

# add title and labels
plt.title('Top 10 Genres',fontsize = 40)
plt.xlabel('Number of Artists')
plt.ylabel(None)
plt.show()

# create bar chart
labels = top_genre.index
sizes = top_genre.values

plt.figure(figsize=(30,20))
plt.pie(
    sizes,
    labels= labels,
    # format percentages with 1 decimal place
    autopct='%1.1f%%',
    # rotate the first slice to start at 140 degrees for better visuals
    startangle=140,
    colors=sns.color_palette('Blues_r', n_colors=len(labels))
)

plt.title('Top 10 Genres Distribution',fontsize = 40)
plt.ylabel(None)
plt.show()