# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introducation](#introducation)
- [Questions to Answer](#questions-to-answer)
- [Analysis](#analysis)
    - [:one: Who are the top 10 most played artists and podcast shows? 🏆](#one-who-are-the-top-10-most-played-artists-and-podcast-shows-)
    - [:two: How diverse are the genres of music artists? 🌟](#two-how-diverse-are-the-genres-of-music-artists-)
    - [:three: Based on the past data, will podcasts occupy most listening time or music tracks? 🕒](#three-based-on-the-past-data-will-podcasts-occupy-most-listening-time-or-music-tracks-)
    - [:four:  Based on the past data, who will be the most played artist and podcast for 2025?" :question:](#four--based-on-the-past-data-who-will-be-the-most-played-artist-and-podcast-for-2025-question)
- [Conclusion](#conclusion)

# Introducation

This is the final section of the project. Here, I conducted an in-depth analysis of the cleaned data from Part 1 [Data_Collection_and_Preparation](/1_Data_Collection_and_Preparation/) to address the four key questions outlined below.

# Questions to Answer
Below are the questions I want to answer in my project:  
1.  Who are the top 10 most played artists and podcast shows? 🏆
2.  How diverse are the genres of music artists? 🌟
3.  Based on the past data, will podcasts occupy most listening time or music tracks? 🕒
4.  Based on past data, who will be the most played artist and podcast for 2025?" :question:  

# Analysis
### :one: Who are the top 10 most played artists and podcast shows? 🏆
I used two approaches to answer this question. The first approach identifies the top artists and podcasts based on the highest play counts, which I determined using the `value_counts` method. The second approach focuses on total playtime by grouping the data by `artist_name` and `show_name`, summing the `minutes_played` for each group, and sorting the results in descending order to find the top ten entries.  

View my notebook with detailed steps here :point_right: [1_Top_10_Most_Played.ipynb](/3_Data_Analysis/1_Top_10_Most_Played.ipynb) 

**Code Implementation**

``` python
# group by artist_name and sum the minutes played
artist_played_hours=(
    music_tracks_df.groupby('artist_name')['minutes_played']
    .sum().sort_values(ascending=False)/60 
)
sns.barplot(
    x=top_artists.values,
    y=top_artists.index,
    ax=ax[0],
    palette=sns.color_palette('Blues_r',len(top_artists)),
    hue=top_artists.index #assign y variable to hue
)
ax[0].set_title('Top 10 Most Played Artists by Count')
ax[0].set_ylabel('')
ax[0].set_xlabel('Play Counts')
ax[0].xaxis.set_major_formatter(FuncFormatter(lambda x,_: f'{int(x/1000)}K'))
```

**🎨 Artist Results**  

![top_10_artists](/Images/top_10_artist_bar.png)  
*Top 10 most played artists by play count and by play time*  


**🎨 Artist Insights**  
- **Hebe Tien**:  
  Leads in both play count and playtime, showing she is the most versatile artist with frequent and extended engagement.
- **S.H.E** and **JJ Lin**:    
  While S.H.E has a higher play count, JJ Lin surpasses in total playtime. This could be because I tend to listen to JJ Lin's entire albums, whereas with S.H.E, I selectively play specific tracks.
- **許嵩** and **G.E.M.**:  
  These two artists show longer playtime relative to their play count, likely indicating entire albums were played rather than selective tracks.
- **Jay Chou**, **Sodagreen**, and **Joker Xue**:  
  These artists rank lower but appear on both charts, showing steady and consist engagement.

**🎙️ Podcast Results**  

![top_10_shows](/Images/top_10_podcast_bar.png)  
*Top 10 most played podcast shows by play count and by play time*  

 

**🎙️ Podcast Insights**  
- **童話裡都是騙人的** and **時間的女兒**:  
  These two shows are clearly the most popular, excelling in both frequency and total play time.
- **我在案發現場** and **善嵐慶女**:  
  These two shows are likely to have longer episodes or more replay value, leading to higher play times despite moderate play counts.


### :two: How diverse are the genres of music artists? 🌟  
To identify the top genres, I started by splitting the `genre` column on commas and exploding it to ensure each genre occupies its own row. I then counted the occurrences of each genre and extracted the top ten. Using this data, I created a pie chart with Matplotlib and added labels for clarity.  

View my notebook with detailed steps here :point_right: [2_Genre_Analysis.ipynb](/3_Data_Analysis/2_Genre_Analysis.ipynb)  

**Code Implementation**  
```python
# select top 10 genres and sort in descending order
genre_count_sorted = genre_count.sort_values(ascending=False).head(10)
# create pie chart with matplotlib
labels = top_genre.index
sizes=top_genre.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=120,
    colors=sns.color_palette('Blues_r',n_colors=len(labels)),
    pctdistance=0.8)
plt.title('Genre Distribuion', fontsize=14)
plt.tight_layout()
plt.show()
```  
**🌈 Genre Results**  

![genre_pie](/Images/genre_pie.png)  
*Top 10 genres*

**🌈 Genre Insights**  
- **Pop** Domination:
  - Pop genres account for over 50% of the total distribution, with **Mandopop** leading at 27.2%, highlighting my strong preference for these genres.
- **Hip Hop** and **Rap**'s Rising Appeal:
  - With over 10% share each, they hold significant importance. Shows I also have a taste for contemporary rhythmic music. 
- Diversity:
  - While smaller genres like **Rock**, **Indie**, and **EDM** have less representation, their inclusion highlights the diversity in my musical tastes.  

### :three: Based on the past data, will podcasts occupy most listening time or music tracks? 🕒  
I addressed this question by calculating the average hours played per year for both tracks and podcasts. The results were visualized in a line chart, enhanced with labels for each marker to improve clarity and detail.

View my notebook with detailed steps here :point_right: [3_Predict_Future_Show_and_Track.ipynb](/3_Data_Analysis/3_Predict_Future_Show_and_Track.ipynb)  

**Code Implementation**  

```python
plt.figure(figsize=(12,8))
# assign the axis to ax
ax= sns.lineplot(data=melted_data, x='year', y='Average Hours', hue='Category', marker='o')
# ensure year label is unique integer
plt.xticks(ticks=melted_data['year'].unique(),   labels=melted_data['year'].unique().astype(int))
# rename legend labels
legend_labels = {
    'avg_track_hours': 'Average Track Hours',
    'avg_podcast_hours': 'Average Podcast Hours'
}
#retrieve the current handles and labels from the plot
handles, labels=ax.get_legend_handles_labels()
#update the legend labels
updated_labels=[legend_labels[label] for label in labels]
# Add labels to each marker
for line_category in melted_data['Category'].unique():
    category_data = melted_data[melted_data['Category'] == line_category]
    for x, y in zip(category_data['year'], category_data['Average Hours']):
        plt.text(x, y, f'{y:.1f}',  # Format the label to 1 decimal place
            fontsize=10, ha='left', va='bottom')
# apply the updated labels to the legend
plt.legend(handles=handles, labels=updated_labels, title='Category',
loc='lower right')
```  

**Results**  

![average_per_day](/Images/average_per_day.png)  
*Average Tracks and Podcast Streaming Hours Per Day*  

**Insights**  
- Trend Shift:
  - Tracks dominated in 2020 but experienced a steady decline over the years.
  - Podcasts, on the other hand, showed consistent growth and surpassed track streaming in 2021.
- Crossing Point:
  - 2021 was a pivotal year when podcasts overtook tracks in daily average hours, indicating my change streaming preference.
- Podcasts' Steady Growth:
  - Podcasts showed a clear upward trend, reaching their peak engagement of 6.0 hours per day in 2024.
- Tracks' Decline:
  - Tracks dropped sharply after 2020, this is due to my shift in streaming habit.
- 2025 Prediction:
  - If the current trends persist, **podcasts** are likely to continue grow, reaching even higher average hours per day. Tracks may stabilize at lower levels or continue their gradual decline.  

### :four:  Based on the past data, who will be the most played artist and podcast for 2025?" :question:  

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
**🎨 Artist Results**  
 
![top_10_artists_over_time](/Images/top_10_artist_over_time.png)  
*Top 10 most played artists over years*   



**🎨 Artist Insights**  
- Artists with Peaked Popularity:
  - **JJ Lin** peaked significantly in 2020 and declined sharply afterward.
  - Artists like **Hebe Tien** and **S.H.E** also peaked early (2019-2020) and declined gradually.
- Consistent Performers:
  - Artists like **Jay Chou** and **Sodagreen** showed relatively consistent playtime across the years, with no extreme peaks or drops.
- Declining Artists:
  - All artists show a steady decline, indicating diminishing interest except for One Republic. 
- Inclining Artists:
  - **OneRepublic** has shown consistent growth since 2022, with a steady upward trend that accelerated significantly in 2023. By 2024, they surpassed all other artists to become the most played. Based on this trajectory, OneRepublic is likely to maintain this momentum and emerge as the most played artist in 2025.  

**🎙️ Podcast Results** 

![top_10_shows_over_time](/Images/top_10_podcast_over_time.png)  
*Top 10 most played podcast shows over years*   

**🎙️ Podcast Insights**    

- Shows with Peaked Popularity:
  - **時間的女兒: 八卦歷史** peaked early (2021-2022) and declined steadily over the years.
  - **劉軒的How to人生學** and **吃史 Eat History** have their highest engagement in 2021 but declined sharply afterward.  
- Rapid Stoppers:  
  - Sreaming for **我在案發現場**, **宮說宮有理 National Palace Museum**, **阿善師鑑識實錄** rapidly stopped in 2023.
- Consistent Performers:
  - **愚樂百昏百** showed steady, consistent playtime.
- Inclining Shows:  
  - **童話裡都是騙人的** demonstrated consistent growth since 2022, with a sharp acceleration into 2024. This show has now outperformed all others and is likely to dominate 2025 if this trajectory continues.


# Conclusion
In this section, I analyzed the cleaned data to answer four key questions, uncovering valuable insights into my streaming behavior. The analysis revealed that my top ten most played artists include **Hebe Tien** and **JJ Lin**, while my most played podcasts feature **童話裡都是騙人的** and **時間的女兒: 八卦歷史**. Although **Mandopop** is my favorite genre, my musical preferences are diverse, spanning various styles. The analysis also highlights a significant shift in my listening habits over time, with **podcasts** demonstrating **consistent growth** and surpassing music tracks as the dominant category. Predictions indicate that **One Republic** and **童話裡都是騙人的** are likely to be the most played artist and podcast in 2025, providing a deeper understanding of my evolving streaming patterns.