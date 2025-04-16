import pandas as pd
import matplotlib.pyplot as plt

# List of movies enter 1990 and 1999
movies = netflix_df[["title", "release_year", "duration", "genre"]]
old_movies = movies[(movies["release_year"] >= 1990) & (movies["release_year"] < 2000)]
print(old_movies)

print("What was the most common film length in the 1990s?")
# Old movies's duration histogram
plt.figure(figsize=(10, 6))
netflix_red = '#E50914'
netflix_dark = '#221F1F'
netflix_grey = '#4E4E4E'
plt.hist(old_movies["duration"], bins=10, color=netflix_red, edgecolor=netflix_dark, alpha=0.8)
plt.title("Movies's duration enter 1990 and 1999", fontsize=14, color='white')
plt.xlabel("duration (min)", fontsize=12, color='white')
plt.ylabel("Number of movies", fontsize=12, color='white')
plt.gca().set_facecolor(netflix_dark)
plt.gcf().set_facecolor(netflix_dark)
plt.tick_params(colors='white')
for spine in plt.gca().spines.values():
    spine.set_color(netflix_grey)
    plt.legend(facecolor=netflix_dark, edgecolor=netflix_grey, labelcolor='white')
    plt.tight_layout()
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
