import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spotify_synthetic_dataset_5000.csv")

# Show first 5 rows
print(df.head())
print(df.info())       # Columns, datatypes, null values
print(df.describe())   # Summary statistics
df.drop_duplicates(inplace=True)
# Handle missing values (drop rows where important columns are missing)
df.dropna(subset=["track_name", "artist_name"], inplace=True)
# Fill numeric missing values with median
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

print("\nAfter Cleaning:")
print(df.isnull().sum())

# Step 5: Exploratory Data Analysis (EDA)

# 1️⃣ How many songs are in the dataset?
print("\nTotal songs:", len(df))

# 2️⃣ Which artist has the most songs?
print("\nTop artist by number of songs:")
print(df["artist_name"].value_counts().head(10))

# 🔹 Visualization: Top artists
df["artist_name"].value_counts().head(10).plot(kind="bar", figsize=(10,5), color="lightblue")
plt.title("Top 10 Artists by Number of Songs")
plt.ylabel("Number of Songs")
plt.xlabel("Artist Name")
plt.xticks(rotation=45)
plt.show()

# 3️⃣ What are the most common genres?
print("\nMost popular genres:")
print(df["genre"].value_counts().head(10))

# 🔹 Visualization: Top genres
df["genre"].value_counts().head(10).plot(kind="bar", figsize=(10,5), color="lightgreen")
plt.title("Top 10 Genres")
plt.ylabel("Number of Songs")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.show()

# 4️⃣ Which song has the highest popularity score?
most_popular = df.loc[df["popularity"].idxmax()]
print("\nMost popular song:")
print(most_popular[["track_name", "artist_name", "popularity"]])

df.groupby("year")["popularity"].mean().plot(figsize=(12,6))
plt.title("Average Popularity of Songs Over Years")
plt.ylabel("Average Popularity")
plt.xlabel("Year")
plt.show()


# 5️⃣ Average duration of songs per genre
print("\nAverage song duration per genre:")
print(df.groupby("genre")["duration_ms"].mean().sort_values(ascending=False).head(10))

# 6️⃣ Average danceability per genre
print("\nAverage danceability by genre:")
print(df.groupby("genre")["danceability"].mean().sort_values(ascending=False).head(10))

df.groupby("genre")["danceability"].mean().sort_values(ascending=False).head(10).plot(
    kind="bar", color="skyblue"
)
plt.title("Top 10 Genres by Average Danceability")
plt.ylabel("Danceability")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.show()

# 7️⃣ Top 10 longest songs
print("\nTop 10 longest songs:")
print(df.nlargest(10, "duration_ms")[["track_name", "artist_name", "duration_ms"]])

# 8️⃣ Distribution of popularity
print("\nPopularity stats:")
print(df["popularity"].describe())

plt.hist(df["popularity"], bins=20, edgecolor="black")
plt.title("Distribution of Popularity")
plt.xlabel("Popularity")
plt.ylabel("Frequency")
plt.show()

# 9️⃣ Average loudness by genre
print("\nAverage loudness per genre:")
print(df.groupby("genre")["loudness_db"].mean().sort_values(ascending=False).head(10))

# 🔟 Top 10 most energetic songs
print("\nTop 10 most energetic songs:")
print(df.nlargest(10, "energy")[["track_name", "artist_name", "energy"]])

df.groupby("genre")["energy"].mean().sort_values(ascending=False).head(10).plot(kind="bar", color="orange")
plt.title("Top 10 Genres by Average Energy")
plt.ylabel("Energy")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.show()

# 1️⃣1️⃣ Tempo distribution by year
df.groupby("year")["tempo_bpm"].mean().plot(figsize=(12,6), color="purple")
plt.title("Average Tempo of Songs Over Years")
plt.ylabel("Tempo (BPM)")
plt.xlabel("Year")
plt.show()


# 1️⃣2️⃣ Evolution of danceability & energy over years
df.groupby("year")["danceability"].mean().plot(label="Danceability")
df.groupby("year")["energy"].mean().plot(label="Energy")
plt.title("Song Characteristics Over Time")
plt.ylabel("Average Value")
plt.xlabel("Year")
plt.legend()
plt.show()


