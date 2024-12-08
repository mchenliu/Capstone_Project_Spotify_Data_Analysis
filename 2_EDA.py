# import libraries
import pandas as pd

# load the cleaned data
music_tracks_df = pd.read_csv('./Cleaned_Data/Music_Streaming_History.csv')
podcast_episodes_df = pd.read_csv('./Cleaned_Data/Podcast_Streaming_History.csv')


# check the first few rows
print(music_tracks_df.head())
print(podcast_episodes_df.head())


# check column types, null counts and summary stats of numeric columns 
# music tracks
print(music_tracks_df.info()) 
print(music_tracks_df.describe())  

# podcast episodes
print(podcast_episodes_df.info())
print(podcast_episodes_df.describe())


# check for null values in music data
print(music_tracks_df.isnull().sum())

# check for null values in podcast data
print(podcast_episodes_df.isnull().sum())

'''
The null values are associated with false in offline column.
Thus the null values are valid.
'''

# EDA with visuals
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# set font to Microsoft YaHei to show Chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# visualize top 20 most played artists
top_artists = music_tracks_df['artist_name'].value_counts().head(20)
sns.barplot(x=top_artists.values, y = top_artists.index, palette='Blues_r')
plt.title('Top 20 Most Played Artists')
plt.xlabel('Artist')
plt.ylabel('Number of Plays')
plt.show()
