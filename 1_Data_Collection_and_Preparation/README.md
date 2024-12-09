# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
  - [Tools Used](#tools-used)
- [Steps Taken](#steps-taken)
  - [:one: Data Collection](#one-data-collection)
  - [:two: Data Cleaning](#two-data-cleaning)
  - [:three: Prepare Artist List](#three-prepare-artist-list)
  - [:four: Prepare Artist Genre List](#four-prepare-artist-genre-list)
- [Conclusion](#conclusion)

# Introduction
:mega: This is the first part of the project. In this section, I collected raw data from Spotify and cleaned it with **Python Pandas** to prepare for Part 2: [Exploratory_Data_Analysis](/2_Exploratory_Data_Analysis/). Additionally, I used the cleaned data to create a list of unique artists and employed **Python Spotipy** to fetch the genres associated with each artist.

## Tools Used
- :snake: Python: The backbone of my project, used to perform all tasks. Key libraries include:
  - Pandas: Used for data cleaning and manipulation.
  - Spotipy: Used to fetch artist genres.
  - dotenv: Used to securely manage my Spotify API keys.
- :notebook: Jupyter Notebooks: Used to run my Python scripts and seemlessly integrate notes and analysis.
- :computer: Visual Studio Code: My pirmary IDE for executing Python scripts.
- :octopus: Git & Github: My go-to for version control and tracking my project progress.
# Steps Taken
## :one: Data Collection
The raw data used in this project is the streaming history from my Spotify account, provided by Spotify. It spans from October 2018 to November 2024. The raw data is in JSON format. Check out the data :point_right: [here](/Raw%20Data_Spotify%20Extended%20Streaming%20History/).
## :two: Data Cleaning
I used **Pyhon Pandas** to clean the data. Below are the stpes I followed:
1. Combined all JSON files. Since the source data contains Chinese characters, I used `utf-8` encoding.
2. Converted data format from JSON to DataFrame.
3. Renamed columns to meaningful names.
4. Fixed data types (e.g., timestamps and boolean columns).
5. Removed rows with `Null` playtime.
6. Normalized text fields (e.g., trimmed whitespace).
7. Added new columns for time-based analysis and other futher work.
8. Split the data into **Music** and **Podcasts**, then saved them as separate CSV files.

**Code Implementation**

```python
# import libraries
import json
import pandas as pd

# list of JSON file paths
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
# load the JSON data from file using UTF-8 encoding
dataframes = [pd.read_json(fp, encoding='utf-8') for fp in file_paths]


# convert JSON data to a DataFrame
df = pd.concat(dataframes, ignore_index=True)

# rename columns
df.rename(columns={'ts': 'date_time', 'master_metadata_track_name': 'track_name', 'conn_country' : 'country', 'master_metadata_album_artist_name': 'artist_name', 'master_metadata_album_album_name': 'album_name','episode_show_name': 'show_name'}, inplace=True)

# convert timestamp column to datetime
df['date_time'] = pd.to_datetime(df['date_time'])
# standardize boolean columns (e.g., shuffle)
df['shuffle'] = df['shuffle'].astype(bool)

# remove playtime is null
df = df[df['ms_played'] > 0]

# normalize text columns
df['track_name'] = df['track_name'].str.strip()
df['album_name'] = df['album_name'].str.strip()
df['episode_name'] = df['episode_name'].str.strip()
df['show_name'] = df['show_name'].str.strip()

# extract useful time-related columns
df['date'] = df['date_time'].dt.date
df['date'] = df['date_time'].dt.date
df['year'] = df['date_time'].dt.year
df['month'] = df['date_time'].dt.month
df['day'] = df['date_time'].dt.day
df['month_year'] = df['date_time'].dt.to_period('M')

# add a new column to convert ms_played to minutes played
df['minutes_played'] = df['ms_played'] / 60000

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
```  
## :three: Prepare Artist List
I used **Pyhon Pandas** to clean the data further. Below are the stpes I followed:  
1. Loaded the cleaned music track data.
2. Find unique artists.
3. Converted file to DataFrame and saved as CSV file.
```python
import pandas as pd

# load the cleaned music tracks data from the VS Code project directory
file_path = './Cleaned_Data/Music_Streaming_History.csv'
df = pd.read_csv(file_path)

# find unique artists
unique_artists = df['artist_name'].dropna().unique()

# convert to a DataFrame
unique_artists_df = pd.DataFrame(unique_artists, columns=['artist_name'])

# save the unique artists to a new CSV
output_path = './Cleaned_Data/Artist_List.csv'
unique_artists_df.to_csv(output_path, index=False, encoding='utf-8-sig')
```
## :four: Prepare Artist Genre List  
I used **Python Spotipy** to fetch artist genres from Spotify and **Python dotenv** to securely manage my API keys, keeping them out of the source code. Below are the steps I followed:  
1. Requested Web API credential from [Spotify_for_Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).
2. Used the credentials to access Spotify's API via Spotipy library.
3. Used dotenv to securely manage my API keys.
4. Iterated through the artist list extracted from the data.
5. Created a new list to store genres fetched for each artist.
6. Added a new column for genres alongside artist names in the dataset.
7. Saved the updated dataset as a new CSV file. 

```python
# find artist genres
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
from dotenv import load_dotenv

# enter spotify credentials
load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# authenticate with spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret= client_secret)
sp= spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# read artist csv
input_path = './Cleaned_Data/Artist_List.csv'
artist_df = pd.read_csv(input_path)
artist_names = artist_df['artist_name'].tolist()

# create a list to store results
artist_genre =[]

# find genres for each artist
for artist_name in artist_names:
    try:
        # search for artist on Spotify
        results = sp.search(q=artist_name,type='artist', limit =1)
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            genres = ', '.join(artist['genres']) if artist['genres'] else 'No genres found'
        else:
            genres = 'Not Found'
    except Exception as e:
        genres = f'Error: {e}'
    artist_genre.append(genres)

# add genres as a new column
artist_df['genres'] = artist_genre

# save to csv
updated_path = './Cleaned_Data/Artist_Genre_List.csv'
artist_df.to_csv(updated_path, index= False, encoding= 'utf-8-sig')
```

# Conclusion
In this section, I collected raw data directly from Spotify and cleaned it using **Python** and **Pandas**. Additionally, I created two CSV files: an artist list and an artist genre list. To fetch artist genres, I used **Spotipy** and secured my Spotify API keys with **dotenv**.

The data cleaning process included:
- Transforming file types from JSON to DataFrame,
- Renaming columns,
- Converting data types (e.g., timestamps and booleans), and
- Normalizing the data.  

Finally, I split the dataset into **Music Tracks** and **Podcast Shows** and saved them as separate CSV files. For collecting genres, I obtained a Spotify Web API token from [Spotify_for_Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started), used **Spotipy**, and iterated through the artist list to assign genres to their corresponding artists.