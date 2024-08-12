import csv

if __name__ == '__main__':
    inventory = []
    with open('resources/clothing.csv') as csvfile:
    # with open('clothing.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)

        for row in csvreader:
            row = list(row)
            inventory.append((int(row[0]), (row[1], row[2], row[3])))

    print("What would you like to sort on?")
    choice = input("type - 1, colour - 2, size - 3: ")
    options = ["type", "colour", "size"]
    print(f"You are sorting on the {options[int(choice)-1]} of clothing.")
    if choice == "1":
        inventory.sort(key = lambda x: x[1][0])
    if choice == "2":
        inventory.sort(key = lambda x: x[1][1])
    if choice == "3":
        inventory.sort(key = lambda x: x[1][2])
    
    for item in inventory:
        print(item)
