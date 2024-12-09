# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introducation](#introducation)
  - [Questions to Answer](#questions-to-answer)
  - [Tools Used](#tools-used)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [EDA on Music and Podcast Streaming History](#eda-on-music-and-podcast-streaming-history)
  - [EDA on Artist Genres](#eda-on-artist-genres)
- [Conclusion](#conclusion)

# Introducation
:mega: This is the second part of the project. In this section, I performed **Exploratory Data Analysis (EDA)** on the cleaned datasets from Part 1 [Data_Collection_and_Preparation](/1_Data_Collection_and_Preparation/). EDA is an essential step to understand the cleaned data, identify potential issues, and determine which columns are most relevant for further analysis. It also serves as a guide for answering questions outlined in Part 3: [Data_Analysis](/3_Data_Analysis/).  

## Questions to Answer
Below are the questions I want to answer in my project:  
1.  What are the most played tracks and artists? 🎶
2.  How do listening habits vary by time of day? 🕒
3.  How diverse are the genres of music artists? 🌟
4.  Which tracks were frequently skipped?　⏭️
5.  What are the top podcast episodes 🎙️  
6.  Based on the past data, will podcasts occupy most listening time or tracks? :headphones:
7.  Based on past data, who are the most played artists and tracks for 2025?" :question:  

## Tools Used
- :snake: Python: The backbone of my project, used to perform all tasks. Key libraries include:
  - Pandas: Used for data cleaning and manipulation.
  - Spotipy: Used to fetch artist genres.
  - Matplotlib:
  - Seaborn:
- :notebook: Jupyter Notebooks: Used to run my Python scripts and seemlessly integrate notes and analysis.
- :computer: Visual Studio Code: My pirmary IDE for executing Python scripts.
- :octopus: Git & Github: My go-to for version control and tracking my project progress.

# Exploratory Data Analysis (EDA)  
## EDA on Music and Podcast Streaming History
:one: **General EDA:**  
- **Inspected Data:** Looked at the first few rows, column names and data types.
  ``` python
  # import libraries
  import pandas as pd

  # load the cleaned data
  music_tracks_df = pd.read_csv('./Cleaned_Data/Music_Streaming_History.csv')
  podcast_episodes_df = pd.read_csv('./Cleaned_Data/Podcast_Streaming_History.csv')
  # check the first few rows
  print(music_tracks_df.head())
  print(podcast_episodes_df.head())
  ```
- **Statistical Summary:**
  ``` python
  # music tracks
  print(music_tracks_df.info()) 
  print(music_tracks_df.describe())  

  # podcast episodes
  print(podcast_episodes_df.info())
  print(podcast_episodes_df.describe())
  ```
- **Checked Missing Values:**
  ``` python
  # check for null values in music data
  print(music_tracks_df.isnull().sum())

  # check for null values in podcast data
  print(podcast_episodes_df.isnull().sum())

  '''
  The null values are associated with `false` in the `offline` column.
  Thus the null values are valid.
  '''
  ``` 
- **Visualize Outliners:**

- **Visulaize Distributions:**  

:two: **Targeted EDA:**
- **Visualize Top 20 Most Played Music Artists & Podcast Shows:**
``` python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# set font to Microsoft YaHei to show Chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# visualize top 20 most played artists
top_artists = music_tracks_df['artist_name'].value_counts().head(20)
sns.barplot(x=top_artists.values, y = top_artists.index, palette='Blues_r')
plt.title('Top 20 Most Played Artists', fontsize = 40)
plt.xlabel('Number of Plays')
plt.ylabel('Artist')
plt.show()

# visualize top 20 most played shows (podcast)
top_show = podcast_episodes_df['show_name'].value_counts().head(20)
# wrap labels inline
wrapped_labels = [textwrap.fill(show_name, width = 15) for show_name in top_show.index]
# adjust width and height
plt.figure(figsize=(30, 20))  
sns.barplot(x=top_show.values, y = wrapped_labels, palette='Blues_r')
plt.title('Top 20 Most Played Shows', fontsize = 35)
plt.xlabel('Number of Plays')
plt.ylabel('Show')
# ensure everything fits properly
plt.tight_layout()
plt.show()
```
![top_20_most_played_artists](/Images/Top_20_Artists.jpeg)
![top_20_most_played_podcasts](/Images/Top_20_Shows.png)
- **Viusalize Listening Trends Over Time:**
``` python
# music listending trends
# group by month_year
music_month_year_trend = music_tracks_df.groupby('month_year').sum()['minutes_played']

# plot
music_month_year_trend.plot(figsize=(30, 20))
plt.title('Total Minutes Played Over Time (Music)', fontsize = 40)
plt.xlabel(None)
plt.ylabel('Total Minutes Played')
plt.grid(True)
plt.show()

# podcast listending trends
# group by month_year
podcast_month_year_trend = podcast_episodes_df.groupby('month_year').sum()['minutes_played']

# plot
podcast_month_year_trend.plot(figsize=(30, 20))
plt.title('Total Minutes Played Over Time (Podcast)', fontsize = 40)
plt.xlabel(None)
plt.ylabel('Total Minutes Played')
plt.grid(True)
plt.show()
```
![music_over_time](/Images/Music_Played_Over_Time.png)
![podcast_over_time](/Images/Podcast_Played_Over_Time.png)

## EDA on Artist Genres
``` python
# import library
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# load the cleaned data
artist_genre_df = pd.read_csv('./Cleaned_Data/Artist_Genre_List.csv')
```
``` python
# split multiple-genres
artist_genre_df['genres_split'] = artist_genre_df['genres'].str.split(', ')
genre_exploded = artist_genre_df.explode('genres_split').rename(columns={'genres_split':'genre'})

# check the first few rows
print(artist_genre_df.head())

# check column types, null counts and summary stats of numeric columns 
# music tracks
print(artist_genre_df.info()) 
print(artist_genre_df.describe())
```
``` python
# count genre occurances
genre_count = genre_cleaned['genre'].value_counts()
print(genre_count)

# identify top 10 genres
top_genre = genre_count.head(10)
print(top_genre)

# select top 10 genres and sort in descending order
genre_count_sorted = genre_count.sort_values(ascending=False).head(10)

# create bar plot with seaborn
sns.set(style='darkgrid')
plt.figure(figsize = (30,20))
sns.barplot(
    x=genre_count_sorted.values,
    y=genre_count_sorted.index,
    palette= 'Blues_r'
)

# add title and labels
plt.title('Top 10 Genres', fontsize = 40)
plt.xlabel('Number of Artists')
plt.ylabel(None)
plt.show()

# create bar chart
labels = top_genre.index
sizes = top_genre.values

plt.figure(figsize=30,20))
plt.pie(
    sizes,
    labels= labels,
    # format percentages with 1 decimal place
    autopct='%1.1f%%',
    # rotate the first slice to start at 140 degrees for better visuals
    startangle=140,
    colors=sns.color_palette('Blues_r', n_colors=len(labels))
)

plt.title('Top 10 Genres Distribution', fontsize = 40)
plt.ylabel(None)
plt.show()
```
![top_10_genre_bar_chart](/Images/Top_Genre_Bar_1.png)
![top_10_genre_pie_chart](/Images/Top_genre_Pie.jpeg)

# Conclusion