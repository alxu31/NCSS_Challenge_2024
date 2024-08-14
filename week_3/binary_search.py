import csv

def recursive_binary_search(data, target, low, high) -> int:
    if low > high:
        return -1
    print(f'Checking between range of {data[low]} and {data[high]}')
    #! Complete the function below
    mid = (low+high)//2
    if target > data[mid]:
        return recursive_binary_search(data, target, mid+1, high)
    elif target < data[mid]:
        return recursive_binary_search(data, target, low, mid-1)
    else:
        return mid

def load_data(filename) -> list:
    numbers = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                numbers.append(int(item.strip()))
    return numbers  

file_name = ("resources/values.csv")
# file_name = ("values.csv")
target = int(input("What's the value you want to search for: "))

input_data = load_data(file_name)
input_data.sort()

result = recursive_binary_search(input_data, target, 0, len(input_data) - 1)
if result != -1:
    print(f'Target value of {target} was located in {file_name} at index {result}')
else:
    print(f'Target value {target} not located in file {file_name}')