# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Tools Used](#tools-used)
- [My Findings](#my-findings)

# Introduction
:mega: In this project, I analyzed my Spotify streaming history, covering both music tracks and podcast shows from 2018 to 2024. The goal is to uncover insights into my listening habits and predict future listening trends. This project is split into four parts:
1. [Data Collection and Preparation](/1_Data_Collection_and_Preparation/)
2. [Exploratary Data Analysis](/2_Exploratory_Data_Analysis/)
3. [Data Analysis](/3_Data_Analysis/)
4. [Problems](/4_Problems/)

# Tools Used
- :snake: Python: The backbone of my project, used to perform all tasks. Key libraries include:
  - Pandas: Used for data cleaning and manipulation.
  - Spotipy: Used to fetch artist genres.
  - dotenv: Used to securely manage my Spotify API keys.
  - Matplotlib
  - Seaborn
- :notebook: Jupyter Notebooks: Used to run my Python scripts and seemlessly integrate notes and analysis.
- :crystal_ball: ChatGPT & search engine: 
- :computer: Visual Studio Code: My pirmary IDE for executing Python scripts.
- :octopus: Git & Github: My go-to for version control and tracking my project progress.

# My Findings
Below are my findings through this project:  
:one:  Who are the top 10 most played artists and podcast shows? 🏆
  - 🎨 Artists:
    - **Hebe Tien** leads in both play count and playtime.
    - **S.H.E** and **JJ Lin** follow closely, with S.H.E leading in play count while JJ Lin surpasses in total playtime. 
  - 🎙️ Podcasts:
      - **童話裡都是騙人的** and **時間的女兒** are the most streamed show, excelling in both frequency and total play time.
      - **我在案發現場** and **善嵐慶女** follow, with moderate play count and high play times.  

![top_10_artists](/Images/top_10_artist_bar.png)  
*Top 10 most played artists by play count and by play time*   

![top_10_shows](/Images/top_10_podcast_bar.png)  
*Top 10 most played podcast shows by play count and by play time*  

:two:  How diverse are the genres of music artists? 🌟  
- **Mandopop** dominates at 27.2%, reflecting my strong preference for pop music.
- **Hip Hop** and **Rap** each hold over 10%, showcasing my appreciation for contemporary rhythmic styles.
- My interest in **Rock**, **Indie**, and **EDM** further highlights the diversity in my musical tastes.  

![genre_pie](/Images/genre_pie.png)  
*Top 10 genres*  

:three:  Based on the past data, will podcasts occupy most listening time or music tracks? 🕒  
- **Podcasts** are likely to continue grow, reaching even higher average hours per day. Tracks may stabilize at lower levels or continue their gradual decline.  

![average_per_day](/Images/average_per_day.png)  
*Average Tracks and Podcast Streaming Hours Per Day*  

:four:  Based on the past data, who will be the most played artist and podcast for 2025?" :question:  
  - 🎨 Artists:
    - **OneRepublic** has shown consistent growth since 2022. By 2024, they surpassed all other artists to become the most played. Based on this trajectory, OneRepublic is likely to maintain this momentum and emerge as the most played artist in 2025.  
  - 🎙️ Podcasts:
    - **童話裡都是騙人的** demonstrated consistent growth since 2022, with a sharp acceleration into 2024. This show has now outperformed all others and is likely to dominate 2025 if this trajectory continues.  

![top_10_artists_over_time](/Images/top_10_artist_over_time.png)  
*Top 10 most played artists over years*  

![top_10_shows_over_time](/Images/top_10_podcast_over_time.png)  
*Top 10 most played podcast shows over years*