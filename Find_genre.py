import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


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



# Set up Spotify API credentials
CLIENT_ID = "your_client_id"  # Replace with your Spotify Client ID
CLIENT_SECRET = "your_client_secret"  # Replace with your Spotify Client Secret

# Authenticate with Spotify API
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = Spotify(auth_manager=auth_manager)

# Load the CSV file
file_path = '/mnt/data/artist.csv'
df = pd.read_csv(file_path)

# Function to fetch artist genres
def fetch_artist_genres(artist_name):
    try:
        # Search for the artist on Spotify
        results = sp.search(q=f"artist:{artist_name}", type='artist', limit=1)
        if results['artists']['items']:
            genres = results['artists']['items'][0].get('genres', [])
            return ", ".join(genres)  # Join genres as a comma-separated string
        else:
            return "No genres found"
    except Exception as e:
        return f"Error: {str(e)}"

# Add genres to the DataFrame
df['genres'] = df['artist_name'].apply(fetch_artist_genres)

# Save the updated DataFrame with genres
output_path = '/mnt/data/artist_with_genres.csv'
df.to_csv(output_path, index=False)

print(f"Updated CSV with genres saved to: {output_path}")
