from dataclasses import dataclass
import json
import math

@dataclass
class Movie:
    title: str
    year: int
    rating: float
    director: str

def calculate_average_ratings_by_decade(movies) -> dict:
    ratings = {}
    for movie in movies:
        decade = math.floor(movie.year/10)*10
        if f"{decade}s" in ratings:
            ratings[f"{decade}s"].append(movie.rating)
        else:
            ratings[f"{decade}s"] = [movie.rating]

    for dec, rat in ratings.items():
        num = len(rat)
        ratings[dec] = sum(rat)/num
    return dict(sorted(ratings.items()))

movies = []
with open('resources/movies.json') as jsonfile:
# with open('movies.json') as jsonfile:
    info = json.load(jsonfile)
    for item in info:
        movies.append(Movie(**item))

decade_ratings = calculate_average_ratings_by_decade(movies)

for decade, avg_rating in decade_ratings.items():
    print(f"{decade}: {avg_rating:.2f}")