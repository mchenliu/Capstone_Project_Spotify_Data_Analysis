import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

music_tracks_df = pd.read_csv('./Cleaned_Data/Music_Streaming_History.csv')
podcast_episodes_df = pd.read_csv('./Cleaned_Data/Podcast_Streaming_History.csv')

# set font to Microsoft YaHei to show Chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# visualize top 20 most played artists
top_artists = music_tracks_df['artist_name'].value_counts().head(20)
sns.barplot(x=top_artists.values, y = top_artists.index, palette='Blues_r')
plt.title('Top 20 Most Played Artists', fontsize = 20)
plt.xlabel('Number of Plays')
plt.ylabel(None)
plt.show()

# visualize top 20 most played shows (podcast)
top_show = podcast_episodes_df['show_name'].value_counts().head(20)
# adjust width and height
plt.figure(figsize=(10, 8))  
sns.barplot(x=top_show.values, y = top_show.index, palette='Blues_r')
plt.title('Top 20 Most Played Shows', fontsize = 20)
plt.xlabel('Number of Plays')
plt.ylabel(None)
# ensure everything fits properly
plt.tight_layout()
plt.show()
