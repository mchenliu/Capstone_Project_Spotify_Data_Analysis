# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introducation](#introducation)
  - [Questions to Answer](#questions-to-answer)
  - [Tools Used](#tools-used)
  - [EDA on Streaming History](#eda-on-streaming-history)
  - [EDA on Artist Genres](#eda-on-artist-genres)
- [Conclusion](#conclusion)

# Introducation
:mega: This is the second part of the project. In this section, I performed **Exploratory Data Analysis (EDA)** on the cleaned datasets from Part 1 [Data_Collection_and_Preparation](/1_Data_Collection_and_Preparation/). EDA is an essential step to understand the cleaned data, identify potential issues, and determine which columns are most relevant for further analysis. It also serves as a guide for answering questions in outlined in Part 3: [Data_Analysis](/3_Data_Analysis/).  

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

## EDA on Streaming History
Perform General EDA:

Inspect Data: Look at the first few rows (df.head()), column names, and data types.
Summary Statistics: Use df.describe() to get a statistical summary.
Missing Values: Check for null or missing data (df.isnull().sum()).
Outliers: Plot boxplots to identify extreme values.
Distributions: Visualize numeric columns with histograms to understand data spread.
Targeted EDA:

Focus on features relevant to your questions.
For time-of-day analysis: Extract and inspect timestamp-based columns.
For artist diversity: Explore artist and genre columns.
For skipped tracks: Analyze play duration (ms_played).
## EDA on Artist Genres
# Conclusion