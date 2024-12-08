import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Your Spotify Credentials
client_id = 'd9fcdeb841a84c9c86093bc2b742a18d'
client_secret = '081b2925bd47442aaa96fc651afe422e'

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Artist Spotify ID
artist_id = '3hhUgkTf3fFYGogFMbV5Wv'

# Fetch artist information
artist = sp.artist(artist_id)

# Display artist name and genres
print(f"Artist: {artist['name']}")
print("Genres:", ", ".join(artist['genres']) if artist['genres'] else "No genres found")
