# :construction: PROJECT UNDER CONSTRUCTION :construction:
# Table of Contents
- [:construction: PROJECT UNDER CONSTRUCTION :construction:](#construction-project-under-construction-construction)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
  - [Tools Used](#tools-used)
- [Steps Taken](#steps-taken)
  - [Data Collection](#data-collection)
  - [Data Cleaning](#data-cleaning)
  - [ETL with Power Query](#etl-with-power-query)
- [Conclusion](#conclusion)

# Introduction
:mega: In this project, I explored my own Spotify streaming history from 2018 - 2023. To find insights on my listening habit and predict my future listening trend. 
Final Deliverables
Create Jupyter Notebookss (showcasing core skills in Python).
Create a summary page (via README.md) to capture my findings.
Share this project via GitHub & LinkedIn.
Questions to Answer
What are the most played tracks and artists? 🎶
How do listening habits vary by time of day? 🕒
How diverse are the genres of music artists? 🌟
Which tracks were frequently skipped?　⏭️
What are the top podcast episodes 🎙️
## Tools Used
- Excel
- Python
- Tableau
- SQL
- Visual Studio Code
- Git & Github
# Steps Taken
## Data Collection
## Data Cleaning
I used Pyhon Pandas to clean data.
First combined all JSON files. And because the source data contains Chinese characters, I used `utf-8` to encode.

```python
import json
import pandas as pd

# list of JSON filr paths
file_paths = [
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020-2021_5.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020_3.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020_4.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2021-2022_6.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2022-2023_7.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2023_8.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2023-2024_9.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2018-2019_0.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2019-2020_2.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2019_1.json'
]


try:
    # Load the JSON data from file using UTF-8 encoding
    dataframes = [pd.read_json(fp, encoding='utf-8') for fp in file_paths]


    # Convert JSON data to a DataFrame
    df = pd.concat(dataframes, ignore_index=True)
```
The next step is to convert column `ts` to datetime format. Then 

```python
    # Convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'])

    # Extract useful time-related columns
    df['date'] = df['ts'].dt.date
    df['hour'] = df['ts'].dt.hour

    #remove playtime is null
    df = df[df['ms_played'] > 0]

    # Standardize boolean columns (e.g., shuffle)
    df['shuffle'] = df['shuffle'].astype(bool)

    # Normalize text columns
    df['master_metadata_track_name'] = df['master_metadata_track_name'].str.strip()
    df['master_metadata_album_artist_name'] = df['master_metadata_album_artist_name'].str.strip()
    df['master_metadata_album_album_name'] = df['master_metadata_album_album_name'].str.strip()
    df['episode_name'] = df['episode_name'].str.strip()
    df['episode_show_name'] = df['episode_show_name'].str.strip()
```


The next step is to split podcast data from music tracks data from source data.
```Python
    # Filter data into music tracks and podcast episodes
    music_tracks_df = df[df['master_metadata_track_name'].notna()]
    podcast_episodes_df = df[df['episode_name'].notna()]
    
    # Drop podcast columns from music tracks data
    music_tracks_df = music_tracks_df.drop(columns=['ip_addr', 'spotify_episode_uri', 'episode_name', 'episode_show_name'])

    # Drop music track columns podcast data
    podcast_episodes_df = podcast_episodes_df.drop(columns=['ip_addr', 'master_metadata_track_name', 'master_metadata_album_artist_name', 'master_metadata_album_album_name','spotify_track_uri'])

    # Save music tracks data to a separate CSV
    music_tracks_output_path = r'C:\Users\Administrator\Desktop\Streaming_History_Music_Tracks.csv'
    music_tracks_df.to_csv(music_tracks_output_path, index=False, encoding='utf-8-sig')
  
    # Save podcast episodes data to a separate CSV
    podcast_episodes_output_path = r'C:\Users\Administrator\Desktop\Streaming_History_Podcast_Episodes.csv'
    podcast_episodes_df.to_csv(podcast_episodes_output_path, index=False, encoding='utf-8-sig')

except PermissionError as e:
    print(f"Permission Error: {e}")
except FileNotFoundError as e:
    print(f"File Not Found: {e}")
except UnicodeDecodeError as e:
    print(f"Encoding Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## ETL with Power Query
# Conclusion