from itertools import zip_longest
import csv

if __name__ == '__main__':
    names, liked, disliked, likedNew, dislikedNew = [], [], [], [], []
    with open('resources/preferences.csv') as csvfile:
    # with open('preferences.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for line in csvreader:
            name = f"{line[0]} {line[1]}"
            if name not in names:
                names.append(name)
            liked.append(line[2].split("/"))
            disliked.append(line[3].split("/"))
            for l, d in zip_longest(liked, disliked):
                if l != None:
                    likedNew += l
                if d != None:
                    dislikedNew += d

    likedNew = list(dict.fromkeys(likedNew))
    dislikedNew = list(dict.fromkeys(dislikedNew))
    for item in dislikedNew:
        if item in likedNew:
            likedNew.remove(item)
    likedNew.sort()
    names.sort()

    print(f"Friends: {names}")
    print(f"Suggested Movies: {likedNew}")