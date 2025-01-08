# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introducation](#introducation)
- [Questions to Answer](#questions-to-answer)
- [Analysis](#analysis)
    - [:one: Who are the top 10 most played artists and podcast shows? 🎶](#one-who-are-the-top-10-most-played-artists-and-podcast-shows-)
    - [:two: How diverse are the genres of music artists? 🌟](#two-how-diverse-are-the-genres-of-music-artists-)
    - [:three: Based on the past data, will podcasts occupy most listening time or music tracks? :headphones:](#three-based-on-the-past-data-will-podcasts-occupy-most-listening-time-or-music-tracks-headphones)
    - [:four:  Based on past data, who will be the most played artist and podcast for 2025?" :question:](#four--based-on-past-data-who-will-be-the-most-played-artist-and-podcast-for-2025-question)
- [Conclusion](#conclusion)

# Introducation
# Questions to Answer
Below are the questions I want to answer in my project:  
1.  Who are the top 10 most played artists and podcast shows? 🎶
2.  How diverse are the genres of music artists? 🌟
3.  Based on the past data, will podcasts occupy most listening time or music tracks? :headphones:
4.  Based on past data, who will be the most played artist and podcast for 2025?" :question:  

# Analysis
### :one: Who are the top 10 most played artists and podcast shows? 🎶

View my notebook with detailed steps here :point_right: [1_Top_10_Most_Played.ipynb](/3_Data_Analysis/1_Top_10_Most_Played.ipynb) 

**Code Implementation**

``` python
sns.barplot(
    x=top_artists.values,
    y=top_artists.index,
    ax=ax[0],
    palette=sns.color_palette('Blues_r',len(top_artists)),
    hue=top_artists.index # #assign y variable to hue
)
ax[0].set_title('Top 10 Most Played Artists by Count')
ax[0].set_ylabel('')
ax[0].set_xlabel('Play Counts')
ax[0].xaxis.set_major_formatter(FuncFormatter(lambda x,_: f'{int(x/1000)}K'))
```

**Result**  

![top_10_artists](/Images/top_10_artist_bar.png)  
*Top 10 most played artists by play count and by play time*  


**Insight**  
- **Hebe Tien**:
  Leads in both play count and playtime, showing she is the most versatile artist with frequent and extended engagement.
- **S.H.E** and **JJ Lin**:
  While S.H.E has a higher play count, JJ Lin has a higher total playtime. This might due to JJ Lin's songs.

- **許嵩** and **G.E.M.**
  Artists like 許嵩 and G.E.M. show longer playtime relative to their play  count, likely indicating longer average track durations.

- **Jay Chou**, **Sodagreen**, and **Joker Xue**
  These artists rank lower but appear on both charts, showing steady and loyal engagement.

**Result**  

![top_10_shows](/Images/top_10_podcast_bar.png)  
*Top 10 most played podcast shows by play count and by play time*  

 

**Insight**  

### :two: How diverse are the genres of music artists? 🌟  
View my notebook with detailed steps here :point_right: [2_Genre_Analysis.ipynb](/3_Data_Analysis/2_Genre_Analysis.ipynb)  
**Code Implementation**  
```python
# select top 10 genres and sort in descending order
genre_count_sorted = genre_count.sort_values(ascending=False).head(10)
# create pie chart with matplotlib
labels = top_genre.index
sizes=top_genre.values
plt.pie(
    sizes,
    labels=labels,
    #format percentage with 1 decimal place
    autopct='%1.1f%%',
    # rotate the first slice to start at 120 degree
    startangle=120,
    colors=sns.color_palette('Blues_r',n_colors=len(labels)),
    pctdistance=0.8 #pull percentage labels away from centre
)
plt.title('Genre Distribuion', fontsize=14)
plt.tight_layout()
plt.show()
```  
**Result**
**Insight**
### :three: Based on the past data, will podcasts occupy most listening time or music tracks? :headphones:
### :four:  Based on past data, who will be the most played artist and podcast for 2025?" :question:  

To predict most played artist for 2025, I calculated total play time for all artists in each year. Then picked out the top 10 artists based on the total play time across all years and plot them as a line chart. Vise versa for the podcast dataset.

View my notebook with detailed steps here :point_right: [4_Predict_Future_Most_Played.ipynb](/3_Data_Analysis/4_Predict_Future_Most_Played.ipynb)  

**Code Implementation**  

```python
sns.lineplot(
    data=filtered_data,
    x='year',
    y='hours_played',
    hue='artist_name',
    palette='tab10',
)
# move legend to right
plt.legend(loc='center left',bbox_to_anchor=(1,0.5), title='Artist')
# Add titles and labels
plt.ylabel('Hours Played')
plt.xlabel('')
plt.title('Top 10 Most Played Artists Over Years', fontsize=16)
plt.tight_layout()
plt.show()
```
**Results**  
![top_10_artists_over_time](/Images/top_10_artist_over_time.png)  
*Top 10 most played artists over years*   



**Insight**  
- Artists with Peaked Popularity:
  - JJ Lin peaked significantly in 2020 and declined sharply afterward.
  - Artists like Hebe Tien and S.H.E also peaked early (2019-2020) and declined gradually.
- Consistent Performers:
  - Artists like Jay Chou and Sodagreen showed relatively consistent playtime across the years, with no extreme peaks or drops.
- Declining Artists:
  All artists show a steady decline, indicating diminishing interest except for One Repulic. 
- Inclining Artists:
  **OneRepublic** has shown consistent growth since 2022, with a steady upward trend that accelerated significantly in 2023. By 2024, they surpassed all other artists to become the most played. Based on this trajectory, OneRepublic is likely to maintain this momentum and emerge as the most played artist in 2025.  

![top_10_shows_over_time](/Images/top_10_podcast_over_time.png)  
*Top 10 most played podcast shows over years*   

# Conclusion