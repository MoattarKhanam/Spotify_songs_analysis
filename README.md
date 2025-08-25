# SQL_Spotify_analysis

# Project Overview

This project explores trends in music features such as popularity, danceability, energy, tempo, and genre using a dataset of Spotify songs.
The goal is to analyze and visualize patterns in song characteristics, discover top artists/genres, and track the evolution of music over time.

# Dataset

File used: spotify_synthetic_dataset_5000.csv

Contents: Song metadata (track name, artist, album, year, genre) and audio features (danceability, energy, tempo, loudness, etc.)

# Tools Used

1. Python

Pandas (data cleaning & analysis)

Matplotlib (visualization)

2. GitHub (project hosting & documentation)

# Data Cleaning

1. Removed duplicates.

2. Dropped rows missing critical values (track_name, artist_name).

3. Filled missing numeric values with median.

# Analysis Performed

1. Dataset Overview

Total number of songs

Most frequent artists & genres

2. Feature Trends

Popularity distribution

Average danceability, energy, tempo, loudness (by genre)

Top 10 longest songs

Top 10 most energetic songs

3. Evolution Over Time

Popularity trend across years

Danceability vs. Energy across years

Tempo trend across years

# Q2.
<img width="1000" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/8c7fe417-e6c9-4099-a641-f90b9ec6a2e9" />

# Q3. 
<img width="1000" height="500" alt="Figure_3" src="https://github.com/user-attachments/assets/01e6092b-3365-43b6-bc8b-a21865b26bcc" />

# Q4.
<img width="1200" height="600" alt="Figure_4" src="https://github.com/user-attachments/assets/24af0ad2-aeef-4f43-8f58-431168411150" />

# Q6.
<img width="640" height="480" alt="Figure_6" src="https://github.com/user-attachments/assets/a2676d92-e56e-4997-a14a-a4325203068a" />

# Q9.
<img width="640" height="480" alt="Figure_9" src="https://github.com/user-attachments/assets/c436f4a7-30ff-4bf9-9730-e3d760aa4a1b" />

# Q10.
<img width="640" height="480" alt="Figure_10" src="https://github.com/user-attachments/assets/56c052ed-f58b-4ccf-b10d-46065c099b99" />

# 11.
<img width="1200" height="600" alt="Figure_11" src="https://github.com/user-attachments/assets/cccfeab6-a791-4043-b32c-427bb26cef42" />

# 12.
<img width="640" height="480" alt="Figure_12" src="https://github.com/user-attachments/assets/a76d73d6-f0c6-4396-964e-f6369f8357b7" />

# Insights

The dataset is not dominated by one artist — instead, multiple artists contribute almost equally, showing diversity in representation.
The dataset is genre-diverse, but HipHop/Rap, Jazz, and KPop clearly dominate, showing modern trends and listener preferences.
Popularity of songs has shown a positive trend over the years, possibly due to streaming platforms, wider accessibility, and global reach of music.
Insight: Genres like Latin and EDM are typically designed for movement and rhythm, while Jazz and Classical focus more on musical complexity than danceability.
Music consumption is dominated by top hits — fewer songs achieve moderate popularity compared to the overwhelming number of high-popularity songs.
EDM and KPop are not only danceable but also high in energy, making them suitable for parties and workouts. In contrast, Classical and Jazz are calmer, more suited for relaxed listening.

#  How to Run

Clone this repo:

git clone https://github.com/MoattarKhanam/Spotify_songs_analysis.git
cd Spotify_songs_analysis


Install dependencies:

pip install pandas matplotlib


Run the script:

python spotify/spotify_analysis.py


