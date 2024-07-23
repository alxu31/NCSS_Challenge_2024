
def get_allowed(people, num) -> list:
    allowed = []
    capacity = 8
    numAllowed = capacity - num
    people = people.split(", ")
    for i in range(numAllowed):
        try:
            allowed.append(people[i])
        except(IndexError):
            pass
    return allowed

people = input("People in line: ")
num = int(input("Number of people inside: "))

allowed = get_allowed(people, num)
if len(allowed) > 0:
    print("These people can enter:", end=" ")
    print(*allowed, sep=", ")
else:
    print("No more room!")