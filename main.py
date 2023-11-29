import pandas as pd
import random

movies = pd.read_csv("movies_metadata.csv", low_memory=False)
print(movies["genres"].unique())
genre = "Romance"
adult = True
runtime = 60
adult_find = movies[movies["adult"] == str(adult)]
if adult:
    genre_find = movies[movies["genres"].str.contains(genre)]
    runtime_find = genre_find[movies["runtime"] < runtime]
    movie_find = (runtime_find["original_title"]).values.tolist()
else:
    genre_find = adult_find[movies["genres"].str.contains(genre)]
    runtime_find = genre_find[movies["runtime"] < runtime]
    movie_find = (runtime_find["original_title"]).values.tolist()

for i in range(10):
    print(movie_find[random.randint(0, len(movie_find))])