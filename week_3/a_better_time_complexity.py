import time
start = time.time()
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
pairs = []
target = int(input("Enter target value: "))
seen = []
for i in numbers:
  complement = target - i
  if complement in seen:
    pairs.append((complement, i))
  seen.append(i)
print()
print(f"Pairs with sum adding to {target}: {pairs}")
print(f"--- {time.time() - start} seconds ---")
