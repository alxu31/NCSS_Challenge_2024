import time

timeout = 2
start_time = time.time()

count = 0
total = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while count < len(numbers):
    if time.time() - start_time > timeout:
        break
    if numbers[count] % 2 == 0:
        total += numbers[count]
    count += 1
        
print(total)