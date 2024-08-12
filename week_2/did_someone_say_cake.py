import csv

if __name__ == '__main__':
    choice = input("What is the cake of the day? ")
    with open("resources/cake.csv") as csvfile:
    # with open("cake.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        cake = {}
        for line in csvreader:
            if line[1] in cake:
                if line[0] not in cake[line[1]]:
                    cake[line[1]].append(line[0])
                    cake[line[1]].sort()
            else:
                cake[line[1]] = [line[0]]
        for line in csvreader:
            print(line)

    if choice in cake:
        print(f"Set of friends to share the cake: {cake[choice]}")
    else:
        print(f"{choice} cake is all yours!")
