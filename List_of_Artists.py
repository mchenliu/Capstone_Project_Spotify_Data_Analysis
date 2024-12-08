import pandas as pd

# Load the cleaned music tracks data from the VS Code project directory
file_path = './Cleaned_Data/Music_Streaming_History.csv'
df = pd.read_csv(file_path)

# Find unique artists
unique_artists = df['artist_name'].dropna().unique()

# Convert to a DataFrame for saving or further analysis
unique_artists_df = pd.DataFrame(unique_artists, columns=['artist_name'])

# Save the unique artists to a new CSV file in the project directory
output_path = r'C:\Users\Administrator\Desktop\artist.csv'
unique_artists_df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Unique artists saved to {output_path}")
