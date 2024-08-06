import csv
import json

titles = []
with open('resources/movies.csv') as csvfile, open('resources/reviews.json') as jsonfile:
# with open('movies.csv') as csvfile, open('reviews.json') as jsonfile:
    for row in csv.DictReader(csvfile):
        titles.append(row)
    reviews = json.load(jsonfile)

print("Movie ratings:")
for key, value in reviews.items():
    title = titles[int(key)-1]['title']
    if titles[int(key)-1]['id'] == key:
        temp = 0
        for item in value:
            temp += int(item)
        rating = f"{(temp/len(value)):.2f}"
        print(f"{key}. {title}: {rating}")