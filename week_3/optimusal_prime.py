import math

def is_prime(x) -> bool:
    if x % 2 == 0: return False
    for i in range(3, int(math.sqrt(x)+1), 2):
        print(f"Checking if {x} is evenly divisible by {i}")
        if x % i == 0: return False
    return True

num = int(input("Enter the number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
