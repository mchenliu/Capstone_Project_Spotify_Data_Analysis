import pandas as pd
import time
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
from dotenv import load_dotenv

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

# find artist genres

# enter spotify credentials
load_dotenv()

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

# create DataFrame with the results
artist_genre_data = pd.DataFrame({
    'artist_name': artist_names,
    'genres': artist_genre
})

# clean the genres
# normalize genres
artist_genre_data['genres'] = artist_genre_data['genres'].str.lower()
artist_genre_data['genres'] = artist_genre_data['genres'].str.strip()


# define genre mapping
# used regular expression \b (word boundaries) for precise genre replacement to avoid partial matches 
genre_mapping = {
    r'\bc-pop\b': 'mandopop',
    r'\bclassic mandopop\b': 'mandopop',
    r'\bmando pop\b': 'mandopop',
    r'\bmandarin pop\b': 'mandopop',
    r'\bchinese pop\b': 'mandopop',
    r'\btaiwanese pop\b': 'mandopop',
    r'\bmainland chinese pop\b': 'mandopop',
    r'\btaiwan pop\b': 'mandopop',
    r'\bchinese jazz\b': 'jazz',
    r'\bpop dance\b': 'dance pop'
}


# replace substrings in genres
for old_genre, new_genre in genre_mapping.items():
    artist_genre_data['genres'] = artist_genre_data['genres'].str.replace(old_genre,new_genre,regex=True) #regex=True ensures \b to function

# remove duplicates in genres
artist_genre_data['genres'] = artist_genre_data['genres'].str.split(', ').apply(lambda x: ', '.join(sorted(set(x))))

artist_df['genre'] = artist_genre
# save to csv
updated_path = './Cleaned_Data/Artist_Genre_List.csv'
artist_df.to_csv(updated_path, index= False, encoding= 'utf-8-sig')
