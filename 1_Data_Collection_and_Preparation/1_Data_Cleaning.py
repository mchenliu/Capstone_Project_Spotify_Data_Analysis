import json
import pandas as pd

# list of JSON filr paths
file_paths = [
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2020-2021_5.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2020_3.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2020_4.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2021-2022_6.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2022-2023_7.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2023_8.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2023-2024_9.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2018-2019_0.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2019-2020_2.json',
    './Raw_Data_Spotify_Streaming_History/Streaming_History_Audio_2019_1.json'
]

try: 
    # load the JSON data from file using UTF-8 encoding
    dataframes = [pd.read_json(fp, encoding='utf-8') for fp in file_paths]


    # convert JSON data to a DataFrame
    df = pd.concat(dataframes, ignore_index=True)

    # rename columns
    df.rename(columns={'ts': 'date_time', 'master_metadata_track_name': 'track_name', 'conn_country' : 'country', 'master_metadata_album_artist_name': 'artist_name', 'master_metadata_album_album_name': 'album_name','episode_show_name': 'show_name'}, inplace=True)

    # convert timestamp column to datetime
    df['date_time'] = pd.to_datetime(df['date_time'])

    # extract useful time-related columns
    df['date'] = df['date_time'].dt.date
    df['year'] = df['date_time'].dt.year
    df['month'] = df['date_time'].dt.month
    df['day'] = df['date_time'].dt.day
    df['month_year'] = df['date_time'].dt.to_period('M')

    # remove playtime is null
    df = df[df['ms_played'] > 0]

    # add a new column to convert ms_played to minutes played
    df['minutes_played'] = df['ms_played'] / 60000

    # standardize boolean columns (e.g., shuffle)
    df['shuffle'] = df['shuffle'].astype(bool)
    
    # normalize text columns
    df['track_name'] = df['track_name'].str.strip()
    df['album_name'] = df['album_name'].str.strip()
    df['episode_name'] = df['episode_name'].str.strip()
    df['show_name'] = df['show_name'].str.strip()

    # filter data into music tracks and podcast episodes
    music_tracks_df = df[df['track_name'].notna()]
    podcast_episodes_df = df[df['episode_name'].notna()]
    
    # drop podcast columns from music tracks data
    music_tracks_df = music_tracks_df.drop(columns=['ip_addr', 'spotify_episode_uri', 'episode_name', 'show_name'])

    # drop music track columns podcast data
    podcast_episodes_df = podcast_episodes_df.drop(columns=['ip_addr', 'track_name', 'artist_name', 'album_name','spotify_track_uri'])

    # save music tracks data to a separate CSV
    music_tracks_output_path = './Cleaned_Data/Music_Streaming_History.csv'
    music_tracks_df.to_csv(music_tracks_output_path, index=False, encoding='utf-8-sig')
  
    # save podcast episodes data to a separate CSV
    podcast_episodes_output_path = './Cleaned_Data/Podcast_Streaming_History.csv'
    podcast_episodes_df.to_csv(podcast_episodes_output_path, index=False, encoding='utf-8-sig')

except PermissionError as e:
    print(f"Permission Error: {e}")
except FileNotFoundError as e:
    print(f"File Not Found: {e}")
except UnicodeDecodeError as e:
    print(f"Encoding Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")