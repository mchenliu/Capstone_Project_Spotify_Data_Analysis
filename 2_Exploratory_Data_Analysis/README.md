# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introducation](#introducation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [EDA on Music and Podcast Streaming History](#eda-on-music-and-podcast-streaming-history)
  - [EDA on Artist Genres](#eda-on-artist-genres)
- [Conclusion](#conclusion)

# Introducation
:mega: This is the second part of the project. In this section, I performed **Exploratory Data Analysis (EDA)** on the cleaned datasets from Part 1 [Data Collection and Preparation](/1_Data_Collection_and_Preparation/). EDA is an essential step to understand the cleaned data, identify potential issues, and determine which columns are most relevant for further analysis. It also serves as a guide for answering questions I want to answer in this project.  


# Exploratory Data Analysis (EDA)  
## EDA on Music and Podcast Streaming History
Performed general EDA on datasets Music_Stremaing_History and Podcast_Streaming_History, including checked for missing values and identified outliers.

View my notebook with detailed steps here :point_right: [1_Streaming_Hisotry_General_EDA.ipynb](/2_Exploratory_Data_Analysis/1_Streaming_Hisotry_General_EDA.ipynb)

**Code Implementation**

:one: **General EDA:**  
- **Inspected Data:** Looked at the first few rows, column names and data types.
  ``` python
  # check the first few rows
  print(music_tracks_df.head())
  print(podcast_episodes_df.head())
  ```
- **Statistical Summary:**
  ``` python
  # music tracks
  print(music_tracks_df.info()) 
  print(music_tracks_df.describe())
  ```
- **Checked Missing Values:**
  ``` python
  # check for null values in music data
  print(music_tracks_df.isnull().sum())
  ```
- **Interpretation:**  
  The null values are associated with `false` in the `offline` column.
  Thus the null values are valid.  


- **Identify Music Played Outliers with BoxPlot:**
  ``` python
  # use minutes_played to create the boxplot
  sns.boxplot(x=music_tracks_df['minutes_played'], palette='Blues_r')
  plt.title('Boxplot of Minutes Played (Music)', fontsize = 20)
  plt.xlabel('Minutes Played')
  plt.show()
  ```
  ![music_boxplot](/Images/boxplot_music_played.png)
  *Boxplot of music minutes played*  

  **Interpretation:**  
  1. Most tracks are played between **0 - 10 minutes**.
  2. The median playback time is around **4 minutes**. Half of the tracks are played for less than 4 minutes, and half are played for more than 4 minutes.  
  3. Tracks above the upper whisker are outliers. These tracks are played for an **unusally long duaration**. The potential explanations are:
       - Tracks being **repeatedly played**.
       - Tracks that are longer (e.g., live recordings or mixes).
       - Tracks being played as **background music**.  

  **What's Next:**  
  I identified outlying tracks by filtering for tracks with more than 10 minuets of playtime. There are 162 results. Some of them are live tracks while some are tracks by top played artists. Therefore, I conclude that this data is not unusual.  
    ```python
  outliers = music_tracks_df[music_tracks_df['minutes_played'] > 10]
  print(outliers[['track_name','artist_name','minutes_played','reason_start']])
  ```

  | track_name | artist_name | minutes_played | reason_start |
  |------------|-------------|----------------|--------------|
  | 不為誰而作的歌 | JJ Lin | 13.096067 | fwdbtn |
  | 心酸+浪費+耳朵+想自由 - Live | Yoga Lin | 10.658817 | fwdbtn |
  |愛情的模樣 Life Live | Mayday | 10.308067 | fwdbtn | 不煽情 | 許嵩 | 10.352750 | trackdone 
  | Faded | Alan Walker | 11.337850 | appload |
  |... | ... | ...| ... | ... |
  | 牽手 | Julie Sue | 11.593617| trackdone |
  | 花又開好了  | S.H.E |  10.777100 |  backbtn|
  | 姐 | Hebe Tien  |    14.522633 | clickrow|
  | 勁歌金曲2 - 情歌王 - Live  |    Leo Ku  |     12.641317 |   trackdone|
  | 灵魂伴侣   | Hebe Tien |      13.299400  |  trackdone|
- **Identify Podcast Played Outliers with BoxPlot:**
  ```python
  plt.figure(figsize=(10,8))
  # use minutes played to create the boxplot
  sns.boxplot(x=podcast_episodes_df['minutes_played'], palette = 'Blues_r')
  plt.title('Boxplot of Minutes Played (Podcast)', fontsize = 20)
  plt.xlabel('Minuetes Played')
  plt.show()
  ```
  ![podcast_boxplot](/Images/boxplot_podcast_played.png)  
  *Boxplot of podcast minutes played* 
**Interpretation:**  
  1. Most podcasts are played between **0 - 50 minutes**.
  2. The median playback time is around **30 minutes**. Half of the podcasts are played for less than 30 minutes, and half are played for more than 30 minutes.  
  3. Podcasts above the upper whisker are outliers. These podcasts are played for an **unusally long duaration**. The potential explanations are:
       - Podcasts are longer.
       - Podcasts being played as **background music**.  
  
  **What's Next:**  
  I identified outlying shows by filtering for shows with more than 50 minutes of playtime. This resulted in 2,577 entries, most of which were podcasts from top-played shows. Therefore, I conclude that this data is not unusual.  
    ```python
  outliers = podcast_episodes_df[podcast_episodes_df['minutes_played'] > 50]
  print(outliers[['show_name','minutes_played']])
  ```
   show_name |  minutes_played |
  |----|---|
  | 腦闆想什麼？   |    50.655633 |
  |腦闆想什麼？   |    77.188250 |
  |腦闆想什麼？   |    53.257400 |
  | 劉軒的How to人生學 |      60.853683|
  |劉軒的How to人生學  |     60.512700|
  |...    |         ...    |     ...|
  | 我在案發現場     |  64.543600 |
  |童話裡都是騙人的   |   166.049717|
  | 時間的女兒：八卦歷史   |    77.487683|
  | 時間的女兒：八卦歷史   |    85.699383|
  | 時間的女兒：八卦歷史   |    53.468050|  
 

:two: **Targeted EDA:**

Performed targeted EDA to find top 10 most played artists/shows and listening trend over time.

View my notebook with detailed steps here :point_right: [2_Streaming_Hisotry_Targeted_EDA.ipynb](/2_Exploratory_Data_Analysis/2_Streaming_History_Targeted_EDA.ipynb)

**Code Implementation**

- **Visualize Top 10 Most Played Music Artists & Podcast Shows:**
``` python
fig, ax = plt.subplots(2,1)
# visualize top 10 most played artists
top_artists = music_tracks_df['artist_name'].value_counts().head(10)
sns.barplot(
    x=top_artists.values,
    y = top_artists.index,
    ax=ax[0],
    palette='Blues_r'
)
ax[0].set_title('Top 10 Most Played Artists')
ax[0].set_ylabel('')
ax[0].set_xlabel('')
ax[0].xaxis.set_major_formatter(FuncFormatter(lambda x,_: f'{int(x/1000)}K'))
```
![top_10_most_played](/Images/top_artists_and_shows.png)  
*Top 10 most played artists and shows*  

- **Viusalize Listening Trends Over Time:**
``` python
sns.lineplot(
    data=music_month_year_trend,
    ax=ax[0]
)
ax[0].set_title('Total Hours Played Over Time', fontsize=14)
ax[0].set_ylabel('Music Trakcs (hrs)', fontsize=12)
ax[0].set_xlabel('Date', fontsize=12)
ax[0].set_xticks(desired_dates)
ax[0].set_xticklabels(desired_labels, rotation=45, ha='right') #rotate and right edge is aligned with anchor point
ax[0].yaxis.set_major_formatter(FuncFormatter(lambda y,_: f'{int(y/60)}'))
```
![hours_over_time](/Images/hours_played_over_time.png)
*Hours played over time for music tracks and podcast shows*

## EDA on Artist Genres  

:one: **General EDA:**  

View my notebook with detailed steps here :point_right: [3_Genre_General_EDA.ipynb](/2_Exploratory_Data_Analysis/3_Genre_General_EDA.ipynb)    

- **Inspected Data:** Looked at the first few rows, column names and data types.
``` python
# check the first few rows
print(artist_genre_df.head())
```
- **Statistical Summary:**
``` python
# check column types, null counts and summary stats of numeric columns 
# music tracks
print(artist_genre_df.info()) 
print(artist_genre_df.describe())
```

:two: **Targeted EDA:**  

View my notebook with detailed steps here :point_right: [4_Genre_Targeted_EDA.ipynb](/2_Exploratory_Data_Analysis/4_Genre_Targeted_EDA.ipynb) 
- **Visualize Top 10 Genres:**
``` python
fig, ax = plt.subplots(2,1,figsize=(12,8))
# create bar plot with seaborn
sns.set(style='darkgrid')
sns.barplot(
    x=genre_count_sorted.values,
    y=genre_count_sorted.index,
    ax=ax[1]
)
# add title and labels
ax[1].set_title('Top 10 Genres', fontsize=14)
ax[1].set_ylabel('')
ax[1].set_xlabel('Number of Artists',fontsize=12)
# create pie chart with matplotlib
labels = top_genre.index
sizes=top_genre.values
```
![top_genres](/Images/top_genres.png)

# Conclusion
In this section, I conducted EDA on in-depth EDA on the cleaned stremaing history and genre datasets. Key insights include:

**Music and Podcast Streaming History:**

Most music tracks are played within 10 minutes, with a median playback time of **4 minutes**. Outliers in playback duration were analyzed and found to include live tracks, extended mixes or background music.
Podcasts generally have a higher playback duration with most episodes played within 50 minutes and a median of **30 minutes**. Outliers largely consisted of popular, longer-format shows.

The top 10 most played artists and shows were identified, showcasing my preferences and trends over time.

**Artist Genres:**

A general analysis of the genres revealed the top 10 most frequent genres, highlighting the dominance of specific musical styles (mandopop and pop) in my listening history.

Visualization of genre distributions through bar plots and pie charts provided a clearer understanding of my genre preferences.

Overall, the EDA provided valuable insights into streaming patterns, my preferences, and key data features. These findings will guide the next steps in the project.