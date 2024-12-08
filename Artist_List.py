import pandas as pd


# flad the cleaned datasets
music_file_path = './Cleaned_Data/Music_Streaming_History.csv'
df = pd.read_csv(music_file_path)

# find unique artists
unique_artists = df['artist_name'].dropna().unique()

# convert to a dataFrame
unique_artists_df = pd.DataFrame(unique_artists, columns=['artist_name'])

# save the unique artists to a new csv file
output_path = './Cleaned_Data/Artist_List.csv'
unique_artists_df.to_csv(output_path, index=False, encoding='utf-8-sig')

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# set up spotify credentials
client_id = 'd9fcdeb841a84c9c86093bc2b742a18d'
client_secret = '081b2925bd47442aaa96fc651afe422e'

# authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# read artist csv
input_path = './Cleaned_Data/Artist_List.csv'
artists_df = pd.read_csv(input_path)
artist_names = artists_df['artist_name'].tolist()

# assign a list to store results
artist_genre = []

# loop through artist names for genres
for artist_name in artist_names:
    try:
        results = sp.search(q=artist_name, type= 'artist', limit= 1)
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            name = artist['name']
            genres = artist['genres']
        else:
            name = artist_name
            genres = ' Not Found'
    except Exception as e:
        name = artist_name
        generes = f'Error: {e}'

    # add result to list
    artist_genre.append({'name': name, 'genres': genres})
    print(f'Aritist: {name} | Genres: {', '. join(genres) if isinstance(genres, list) else genres}')

# convert to dataframe and save as csv

                                    






"""
# List of artist names
artist_names = ['Adele', 'Beyoncé', 'Taylor Swift']

# Prepare an empty list to store results
data = []

# Loop through each artist and get their genres
for artist_name in artist_names:
    results = sp.search(q=artist_name, type='artist', limit=1)
    
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        artist_name = artist['name']
        genres = artist['genres']
    else:
        artist_name = artist_name  # If no artist found, use the search term
        genres = []

    data.append([artist_name, ', '.join(genres)])

# Create a DataFrame and save to CSV
df = pd.DataFrame(data, columns=['Artist Name', 'Genres'])
df.to_csv('multiple_artists_genres.csv', index=False, encoding='utf-8')
"""