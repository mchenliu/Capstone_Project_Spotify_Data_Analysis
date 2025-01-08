# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introducation](#introducation)
  - [Questions to Answer](#questions-to-answer)
  - [Tools Used](#tools-used)
- [Analysis](#analysis)
    - [What are the 20 most played tracks and artists? 🎶](#what-are-the-20-most-played-tracks-and-artists-)
- [Conclusion](#conclusion)

# Introducation
## Questions to Answer
Below are the questions I want to answer in my project:  
1.  Who are the top 10 most played artists and podcast shows? 🎶
2.  How diverse are the genres of music artists? 🌟
3.  Based on the past data, will podcasts occupy most listening time or tracks? :headphones:
4.  Based on past data, who are the most played artists and podcast for 2025?" :question:  
## Tools Used
- :snake: Python: The backbone of my project, used to perform all tasks. Key libraries include:
  - Pandas: Used for data cleaning and manipulation.
  - Spotipy: Used to fetch artist genres.
  - Matplotlib:
  - Seaborn:
- :notebook: Jupyter Notebooks: Used to run my Python scripts and seemlessly integrate notes and analysis.
- :computer: Visual Studio Code: My pirmary IDE for executing Python scripts.
- :octopus: Git & Github: My go-to for version control and tracking my project progress.
# Analysis
### What are the 20 most played tracks and artists? 🎶
``` python
# import library
import pandas as pd

# load the data
music_track_df = pd.read_csv('./Cleaned_Data/Music_Streaming_History.csv')
podcast_episodes_df = pd.read_csv('./Cleaned_Data/Podcast_Streaming_History.csv')

top_artists = music_track_df['artist_name'].value_counts().head(20)

#format artist counts with thousand seperator
top_artists = top_artists.apply(lambda x: f'{x:,}')
# reset the index
top_artists = top_artists.reset_index()
# remove index in result
print(top_artists.to_string(index=False))
```
*Top 20 Artists by Counts:*
| artist_name | count |
|-------------|-------|
|Hebe Tien| 14,441|
|S.H.E| 12,149| 
|JJ Lin| 11,464|
|Yoga Lin|  8,739|
|Leehom Wang | 8,312|
| 許嵩 | 6,570|
| G.E.M.| 5,692|
| Jay Chou |5,590|
|sodagreen | 5,478|  
|OneRepublic | 5,259|
|Joker Xue | 4,665| 
|路嘉欣 | 4,045|
| Eason Chan | 3,560|
   Aska Yang | 3,554|  
  |Steve Chou | 2,891|   
|Taylor Swift | 2,505|
 許光漢 | 2,504|
 Niall Horan | 2,465|
Charlie Puth | 2,429|
 Joanna Wang | 2,111|

```python
# group by artist name and sum the minutes played
top_artists_by_minutes = round(music_track_df.groupby('artist_name')['minutes_played'].sum(),2)

# sort the results in descending order and select the top 20
top_artists_by_minutes = top_artists_by_minutes.sort_values(ascending=False).head(20)

# format minutes with thousand seperator
top_artists_by_minutes = top_artists_by_minutes.apply(lambda x: f'{x:,}')

# reset the index
top_artists_by_minutes = top_artists_by_minutes.reset_index()

# print the result without the index
print(top_artists_by_minutes.to_string(index=False))
```

*Top 20 Artists by Minutes Played:*
|artist_name |minutes_played|
|------------|--------------|
| Hebe Tien     | 36,692.95|
|JJ Lin   |    36,191.6|
| S.H.E  |    27,279.01|
|Yoga Lin|      23,260.59|
| Leehom Wang   |   19,066.72|
|許嵩 |      16,147.8|
|G.E.M. |     14,951.88|
|Jay Chou |     14,117.79|
|路嘉欣   |   11,822.62 |
| Joker Xue |     11,655.04|
|sodagreen |     11,652.2|
| OneRepublic|       9,960.75|
|Aska Yang |      9,256.75|
|許光漢 |       7,875.6|
|Steve Chou  |     6,341.16|
|Eason Chan|       4,659.56|
|吳青峰 |      4,103.88|
|Niall Horan|       3,849.25|
|Taylor Swift  |     3,679.96|
|Charlie Puth |      3,542.84|


# Conclusion