import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

music_tracks_df = pd.read_csv('./Cleaned_Data/Music_Streaming_History.csv')
podcast_episodes_df = pd.read_csv('./Cleaned_Data/Podcast_Streaming_History.csv')


# create boxplot for minutes_played in music streaming dataset
plt.figure(figsize=(10,8))
# use minutes_played to create the boxplot
sns.boxplot(x=music_tracks_df['minutes_played'], palette='Blues_r')
plt.title('Boxplot of Minutes Played (Music)', fontsize = 20)
plt.xlabel('Minutes Played')
plt.show()

# create boxplot for minutes_played in postcast streaming dataset
plt.figure(figsize=(10,8))
# use minutes played to create the boxplot
sns.boxplot(x=podcast_episodes_df['minutes_played'], palette = 'Blues_r')
plt.title('Boxplot of Minuets Played (Podcast)', fontsize = 20)
plt.xlabel('Minuetes Played')
plt.show()
