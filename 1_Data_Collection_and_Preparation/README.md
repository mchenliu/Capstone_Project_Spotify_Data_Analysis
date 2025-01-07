# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Steps Taken](#steps-taken)
  - [:one: Data Collection](#one-data-collection)
  - [:two: Data Cleaning](#two-data-cleaning)
  - [:three: Prepare Artist List](#three-prepare-artist-list)
  - [:four: Prepare Artist Genre List](#four-prepare-artist-genre-list)
  - [:five: Fill rows with no genres](#five-fill-rows-with-no-genres)
- [Conclusion](#conclusion)

# Introduction
:mega: This is the first part of the project. In this section, I collected raw data from Spotify and cleaned it with **Python Pandas** to prepare for Part 2: [Exploratory Data Analysis](/2_Exploratory_Data_Analysis/). Additionally, I used the cleaned data to create a list of unique artists and employed **Python Spotipy** to fetch the genres associated with each artist.

# Steps Taken
## :one: Data Collection
The raw data used in this project is the streaming history from my Spotify account, provided by Spotify. It spans from October 2018 to November 2024. The raw data is in JSON format. Check out the data :point_right: [here](/Raw_Data_Spotify_Streaming_History/).
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

View my notebook with detailed steps here :point_right: [1_Data_Cleaning.ipynb](/1_Data_Collection_and_Preparation/1_Data_Cleaning.ipynb)

**Code Implementation**

```python
# import libraries
import json
import pandas as pd
# load the JSON data from file using UTF-8 encoding
dataframes = [pd.read_json(fp, encoding='utf-8') for fp in file_paths]
# rename columns
df.rename(columns={'ts': 'date_time', 'master_metadata_track_name': 'track_name', 'conn_country' : 'country', 'master_metadata_album_artist_name': 'artist_name', 'master_metadata_album_album_name': 'album_name','episode_show_name': 'show_name'}, inplace=True)
# convert timestamp column to datetime
df['date_time'] = pd.to_datetime(df['date_time'])
# normalize text columns
df['track_name'] = df['track_name'].str.strip()
df['album_name'] = df['album_name'].str.strip()
df['episode_name'] = df['episode_name'].str.strip()
df['show_name'] = df['show_name'].str.strip()
# add a new column to convert ms_played to minutes played
df['minutes_played'] = df['ms_played'] / 60000
# filter data into music tracks and podcast episodes
music_tracks_df = df[df['track_name'].notna()]
podcast_episodes_df = df[df['episode_name'].notna()]
```  
## :three: Prepare Artist List
I used **Pyhon Pandas** to clean the data further. Below are the stpes I followed:  
1. Loaded the cleaned music track data.
2. Find unique artists.
3. Converted file to DataFrame and saved as CSV file.

View my notebook with detailed steps here :point_right: [2_Artist_List.ipynb](/1_Data_Collection_and_Preparation/2_Artist_List.ipynb)

**Code Implementation**

```python
import pandas as pd
# find unique artists
unique_artists = df['artist_name'].dropna().unique()
```
## :four: Prepare Artist Genre List  
I used **Python Spotipy** to fetch artist genres from Spotify and **Python dotenv** to securely manage my API keys, keeping them out of the source code. Below are the steps I followed:  
1. Requested Web API credential from [Spotify for Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).
2. Used the credentials to access Spotify's API via Spotipy library.
3. Used dotenv to securely manage my API keys.
4. Iterated through the artist list extracted from the data.
5. Created a new list to store genres fetched for each artist.
6. Added a new column for genres alongside artist names in the dataset.
7. Normalized text fields by trimming whitespace and converting all text to lowercase.
8. Mapped genres names to standardized labels for consistency (e.g., replacing 'mandarin pop' with 'mandopop').
9. Removed duplicated genre entries for each artist to clean the data.
10. Saved the updated dataset as a new CSV file. 

View my notebook with detailed steps here :point_right: [3_Artist_Genre_List.ipynb](/1_Data_Collection_and_Preparation/3_Artist_Genre_List.ipynb)

**Code Implementation**

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
```
## :five: Fill rows with no genres 
Due to the limitation of Spotipy package, there are artists with no genres after above step. I decided to manually map genres to artists with help from ChatGPT and Google. Below are the steps I followed:  
1. Fill genres and saved the file as 'Empty_Genres_Filled.csv'.
2. Drop rows with `no genres found` in the genres column from the original file.
3. Append the filled data and save as 'Completed_Artist_Genre_List.csv'.

View my notebook with detailed steps here :point_right: [4_Fill_Empty_Genres.ipynb](/1_Data_Collection_and_Preparation/4_Fill_Empty_Genre.ipynb)

**Code Implementation**

```python
# drop rows where genre is 'no genres found'
filter_genre_df = artist_genre_df[artist_genre_df['genres'] != 'no genres found']
# append filled genres
# file paths
genres_filled_file_path = '../Cleaned_Data/Empty_Genres_Filled.csv'
# load dataframes
genre_filled_df = pd.read_csv(genres_filled_file_path)
# combine both DataFrames
combined_df = pd.concat([filter_genre_df,genre_filled_df], ignore_index=True)
# remove duplicates based on artist_name and genres
combined_df=combined_df.drop_duplicates(subset=['artist_name','genres']).reset_index(drop=True)
```

# Conclusion
In this section, I collected raw data directly from Spotify and cleaned it using **Python** and **Pandas**. Additionally, I created two CSV files: an artist list and an artist genre list. To fetch artist genres, I used **Spotipy** and secured my Spotify API keys with **dotenv**. I cleaned the artist genre list further by standardizing the labels and removed duplicates. Due to Spotipy limitation, I manually mapped artists without genres and updated the genre list.

The data cleaning process included:
- Transforming file types from JSON to DataFrame,
- Renaming columns,
- Converting data types (e.g., timestamps and booleans), and
- Normalizing the data.  

Finally, I split the dataset into **Music Tracks** and **Podcast Shows** and saved them as separate CSV files. For collecting genres, I obtained a Spotify Web API token from [Spotify for Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started), used **Spotipy**, and iterated through the artist list to assign genres to their corresponding artists.