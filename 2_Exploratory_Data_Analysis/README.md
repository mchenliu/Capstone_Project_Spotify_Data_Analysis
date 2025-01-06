# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introducation](#introducation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [EDA on Music and Podcast Streaming History](#eda-on-music-and-podcast-streaming-history)
  - [EDA on Artist Genres](#eda-on-artist-genres)
- [Conclusion](#conclusion)

# Introducation
:mega: This is the second part of the project. In this section, I performed **Exploratory Data Analysis (EDA)** on the cleaned datasets from Part 1 [Data Collection and Preparation](/1_Data_Collection_and_Preparation/). EDA is an essential step to understand the cleaned data, identify potential issues, and determine which columns are most relevant for further analysis. It also serves as a guide for answering questions I want to answer through this project.  


# Exploratory Data Analysis (EDA)  
## EDA on Music and Podcast Streaming History

View my notebook with detailed steps here :point_right: [1_1_Streaming_Hisotry_General_EDA.ipynb](/2_Exploratory_Data_Analysis/1_Streaming_Hisotry_General_EDA.ipynb)

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
**Interpretation:**  
  The null values are associated with `false` in the `offline` column.
  Thus the null values are valid.

   
- **Identify Outliners with BoxPlot:**
  ``` python
  # use minutes_played to create the boxplot
  sns.boxplot(x=music_tracks_df['minutes_played'], palette='Blues_r')
  plt.title('Boxplot of Minutes Played (Music)', fontsize = 20)
  plt.xlabel('Minutes Played')
  plt.show()
  ```
  ![music_boxplot](/Images/music_boxplot.png)
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

  ![podcast_boxplot](/Images/podcast_boxplot.png)  
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
  
- **Visulaize Distributions:**  

:two: **Targeted EDA:**

View my notebook with detailed steps here :point_right: [2_Streaming_Hisotry_Targeted_EDA.ipynb](/2_Exploratory_Data_Analysis/2_Streaming_History_Targeted_EDA.ipynb)

- **Visualize Top 20 Most Played Music Artists & Podcast Shows:**
``` python
# visualize top 20 most played artists
top_artists = music_tracks_df['artist_name'].value_counts().head(20)
sns.barplot(x=top_artists.values, y = top_artists.index, palette='Blues_r')
plt.title('Top 20 Most Played Artists', fontsize = 20)
plt.xlabel('Number of Plays')
plt.ylabel(None)
plt.show()
```
![top_20_most_played_artists](/Images/top_20_played_artists.png)
![top_20_most_played_podcasts](/Images/top_20_played_shows.png)
- **Viusalize Listening Trends Over Time:**
``` python
podcast_month_year_trend.plot(figsize=(10, 8))
plt.title('Total Minutes Played Over Time (Podcast)', fontsize = 20)
plt.xlabel(None)
plt.ylabel('Total Minutes Played')
plt.grid(True)
plt.show()
```
![music_over_time](/Images/Music_Played_Over_Time.png)
![podcast_over_time](/Images/Podcast_Played_Over_Time.png)

## EDA on Artist Genres  
View my notebook with detailed steps here :point_right: [3_Genre_General_EDA.ipynb](/2_Exploratory_Data_Analysis/3_Genre_General_EDA.ipynb)  

:one: **General EDA:** 
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
- **Visualize Top 10 Genres:**
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
plt.figure(figsize = (10,8))
sns.barplot(
    x=genre_count_sorted.values,
    y=genre_count_sorted.index,
    palette= 'Blues_r'
)

# add title and labels
plt.title('Top 10 Genres', fontsize = 20)
plt.xlabel('Number of Artists')
plt.ylabel(None)
plt.show()

# create bar chart
labels = top_genre.index
sizes = top_genre.values

plt.figure(figsize=10,8))
plt.pie(
    sizes,
    labels= labels,
    # format percentages with 1 decimal place
    autopct='%1.1f%%',
    # rotate the first slice to start at 140 degrees for better visuals
    startangle=140,
    colors=sns.color_palette('Blues_r', n_colors=len(labels))
)

plt.title('Top 10 Genres Distribution', fontsize = 20)
plt.ylabel(None)
plt.show()
```
![top_10_genre_bar_chart](/Images/top10_genres.png)
![top_10_genre_pie_chart](/Images/top10_genres_distribution.png)

# Conclusion
In this section, I conducted EDA on 
