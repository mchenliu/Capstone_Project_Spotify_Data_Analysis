# import libraries
import pandas as pd

# load the cleaned data
music_tracks_df = pd.read_csv('./Cleaned_Data/Music_Streaming_History.csv')
podcast_episodes_df = pd.read_csv('./Cleaned_Data/Podcast_Streaming_History.csv')
# check the first few rows
print(music_tracks_df.head())
print(podcast_episodes_df.head())


# get statistical summary 
# music tracks
print(music_tracks_df.info()) 
print(music_tracks_df.describe())  

# podcast episodes
print(podcast_episodes_df.info())
print(podcast_episodes_df.describe())