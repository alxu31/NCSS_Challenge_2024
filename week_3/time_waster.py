import time
import json

start_time = time.time()

def sort_customers(customer_dictionary) -> dict:
    customer_dictionary = dict(sorted(customer_dictionary.items()))
    for key, val in customer_dictionary.items():
        temp = sorted(val)
        customer_dictionary[key] = temp
    return customer_dictionary

def check_efficient_duration(duration) -> bool:
    if duration > 0.001: return False
    else: return True

def print_dictionary(dictionary) -> None:
    for customer, pets in dictionary.items():
        if pets:
            print(f"{customer}: {', '.join(pets)}")
        else:
            print(f"{customer}: No pets")

if __name__ == '__main__':
    with open('resources/vet_customers.json') as f:
    # with open('vet_customers.json') as f:
        customers = json.load(f)
        print(customers)
        sorted_customers = sort_customers(customers)
        print_dictionary(sorted_customers)

        end_time = time.time()
        duration = end_time - start_time
        is_efficient_algorithm = check_efficient_duration(duration)
        print()
        if is_efficient_algorithm:
            print('Efficient time complexity based on small data sample.')
        else:
            print('Not the most efficient algorithm!')