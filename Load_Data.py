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
# Load multiple JSON files into a single DataFrame
dataframes = [pd.read_json(fp, encoding='utf-8') for fp in file_paths]
df = pd.concat(dataframes, ignore_index=True)


# Inspect the first rows
print(df.head())


# check_for_missing_data
# Check missing values
print(df.isnull().sum())

# Drop podcast columns
df = df.drop(columns=['ip_addr', 'spotify_episode_uri', 'episode_name', 'episode_show_name'])

#convert timestamp
# Convert timestamp column to datetime
df['ts'] = pd.to_datetime(df['ts'])

# Extract useful time-related columns
df['date'] = df['ts'].dt.date
df['hour'] = df['ts'].dt.hour

#remove playtime is null
df = df[df['ms_played'] > 0]

#remove duplicates
df = df.drop_duplicates()

#standardize data
# Standardize boolean columns (e.g., shuffle)
df['shuffle'] = df['shuffle'].astype(bool)

# Normalize text columns
df['master_metadata_track_name'] = df['master_metadata_track_name'].str.strip()
df['master_metadata_album_artist_name'] = df['master_metadata_album_artist_name'].str.strip()

# Total playtime per day
daily_playtime = df.groupby('date')['ms_played'].sum()

# Most-played tracks
most_played = df.groupby('master_metadata_track_name')['ms_played'].sum().sort_values(ascending=False)

print(daily_playtime)
print(most_played)

df.to_csv('cleaned_streaming_history.csv', index=False)
