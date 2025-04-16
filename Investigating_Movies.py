# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
netflix_df.head()

# List of movies enter 1990 and 1999
movies = netflix_df[["title", "release_year", "duration", "genre"]]
old_movies = movies[(movies["release_year"] >= 1990) & (movies["release_year"] < 2000)]
print(old_movies)

print("What was the most common film length in the 1990s?")
# Old movies's duration histogram
plt.hist(old_movies["duration"])
plt.title("Movies's duration enter 1990 and 1999")
plt.xlabel("duration")
plt.ylabel("Number of movies")
plt.show()

duration = 110

print("Which action films last less than 90 minutes?")
# List of short movies
action_movies = []
for lab, row in old_movies.iterrows():
    if row["genre"] == "Action":
        action_movies.append(row)

df_action_movies = pd.DataFrame(action_movies)
print(df_action_movies)

# List of action movies, less 90 minutes
short_movie_count = 0
for lab, row in df_action_movies.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1
print("Total of short action movies:", short_movie_count)
