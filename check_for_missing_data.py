# Check missing values
print(df.isnull().sum())

# Drop podcast columns
df = df.drop(columns=['ip_addr', 'spotify_episode_uri', 'episode_name', 'episode_show_name'])
