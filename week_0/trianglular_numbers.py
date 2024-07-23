def get_triangle_numbers(lim) -> list:
    nums = []
    i = 2
    temp = 1
    while temp <= int(lim):
        nums.append(temp)
        temp += i
        i += 1
    return nums

limit = input("Limit: ")
triangleNumbers = get_triangle_numbers(limit)
print(*triangleNumbers, sep='\n')