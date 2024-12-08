import json
import pandas as pd

# list of JSON filr paths
file_paths = [
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2020-2021_5.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2020_3.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2020_4.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2021-2022_6.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2022-2023_7.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2023_8.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2023-2024_9.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2018-2019_0.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2019-2020_2.json',
    './Raw Data_Spotify Extended Streaming History/Streaming_History_Audio_2019_1.json'
]

# Load the JSON data from file using UTF-8 encoding
dataframes = [pd.read_json(fp, encoding='utf-8') for fp in file_paths]


# Convert JSON data to a DataFrame
df = pd.concat(dataframes, ignore_index=True)
    
df.rename(columns={"master_metadata_track_name": "track_name"}, inplace=True)

print(df.columns)

    # Rename columns
    #df.rename(columns={"conn_country": "country", "master_metadata_track_name": "track_name"}, inplace=True)