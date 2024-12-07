import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Set up your credentials
client_id = 'my client id'
client_secret = 'my client secret'

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

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
