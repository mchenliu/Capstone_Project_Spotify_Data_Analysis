"""
1.  What are the 20 most played tracks and artists? 🎶
2.  How do listening habits vary by time of day? 🕒
3.  How diverse are the genres of music artists? 🌟
4.  Which tracks were frequently skipped?　⏭️
5.  What are the top podcast episodes 🎙️  
6.  Based on the past data, will podcasts occupy most listening time or tracks? :headphones:
7.  Based on past data, who are the most played artists and tracks for 2025?" :question:  
"""

# import library
import pandas as pd

# load the data
music_track_df = pd.read_csv('./Cleaned_Data/Music_Streaming_History.csv')
podcast_episodes_df = pd.read_csv('./Cleaned_Data/Podcast_Streaming_History.csv')

top_artists = music_track_df['artist_name'].value_counts().head(20)

#format artist counts with thousand seperator
top_artists = top_artists.apply(lambda x: f'{x:,}')
# reset the index
top_artists = top_artists.reset_index()


print(top_artists.to_string(index=False))

# group by artist name and sum the minutes played
top_artists_by_minutes = round(music_track_df.groupby('artist_name')['minutes_played'].sum(),2)

# sort the results in descending order and select the top 20
top_artists_by_minutes = top_artists_by_minutes.sort_values(ascending=False).head(20)

# format minutes with thousand seperator
top_artists_by_minutes = top_artists_by_minutes.apply(lambda x: f'{x:,}')

# reset the index
top_artists_by_minutes = top_artists_by_minutes.reset_index()

# print the result without the index
print(top_artists_by_minutes.to_string(index=False))
