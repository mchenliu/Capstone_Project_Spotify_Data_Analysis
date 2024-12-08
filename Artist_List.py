import pandas as pd

# Load the cleaned music tracks data from the VS Code project directory
file_path = './Cleaned_Data/Music_Streaming_History.csv'
df = pd.read_csv(file_path)

# Find unique artists
unique_artists = df['artist_name'].dropna().unique()

# Convert to a DataFrame for saving or further analysis
unique_artists_df = pd.DataFrame(unique_artists, columns=['artist_name'])

# Save the unique artists to a new CSV file in the project directory
output_path = './Cleaned_Data/Artist_List.csv'
unique_artists_df.to_csv(output_path, index=False, encoding='utf-8-sig')

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

# set up spotify credentials
client_id = 'my id'
client_secret = 'my secret'

# authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

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
updated_path = './Cleaned_Data/Artist_List_Updated.csv'
artist_df.to_csv(updated_path, index= False, encoding= 'utf-8-sig')
# convert to dataframe and save as csv

                                    





