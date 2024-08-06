import csv

def read_numbers_from_csv(filename) -> list:
    numbers = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    try:
                        numbers.append(int(item.strip()))
                    except(ValueError):
                        print("ValueError: The file contains a value that is not a valid number.")
                        return numbers
    except(FileNotFoundError):
        print("FileNotFoundError: The file does not exist.")
    return numbers

def calculate_average(numbers) -> int|None:
    average = None
    try:
        average = sum(numbers) / len(numbers)
    except(ZeroDivisionError):
        print("ZeroDivisionError: Cannot calculate average of an empty list.")
        return
    return average

# Enter one of {resources/values1.csv, resources/values2.csv, resources/values3.csv, resources/values4.csv}
# Or one of {values1.csv, values2.csv, values3.csv, values4.csv} in Grok
filename = input("Enter the filename: ")
numbers = read_numbers_from_csv(filename)
average = calculate_average(numbers)
if average:
    print(f"The average of the numbers is: {average}")