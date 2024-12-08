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
import textwrap

# set font to Microsoft YaHei to show Chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# visualize top 20 most played artists (music)
top_artists = music_tracks_df['artist_name'].value_counts().head(20)
sns.barplot(x=top_artists.values, y = top_artists.index, palette='Blues_r')
plt.title('Top 20 Most Played Artists', fontsize = 40)
plt.xlabel('Number of Plays')
plt.ylabel(None)
plt.show()
    

# visualize top 20 most played shows (podcast)
top_show = podcast_episodes_df['show_name'].value_counts().head(20)
# wrap labels inline
wrapped_labels = [textwrap.fill(show_name, width = 15) for show_name in top_show.index]
# adjust width and height
plt.figure(figsize=(30, 20))  
sns.barplot(x=top_show.values, y = wrapped_labels, palette='Blues_r')
plt.title('Top 20 Most Played Shows', fontsize = 35)
plt.xlabel('Number of Plays')
plt.ylabel(None)
# ensure everything fits properly
plt.tight_layout()
plt.show()


# visualize music listending trends over time
# group by month_year
music_month_year_trend = music_tracks_df.groupby('month_year').sum()['minutes_played']

# plot
music_month_year_trend.plot(figsize=(30, 20))
plt.title('Total Minutes Played Over Time (Music)', fontsize = 40)
plt.xlabel(None)
plt.ylabel('Total Minutes Played', fontsize = 40)
plt.grid(True)
plt.show()

# visualize podcast listending trends over time
# group by month_year
podcast_month_year_trend = podcast_episodes_df.groupby('month_year').sum()['minutes_played']

# plot
podcast_month_year_trend.plot(figsize=(30, 20))
plt.title('Total Minutes Played Over Time (Podcast)', fontsize = 40)
plt.xlabel(None)
plt.ylabel('Total Minutes Played')
plt.grid(True)
plt.show()