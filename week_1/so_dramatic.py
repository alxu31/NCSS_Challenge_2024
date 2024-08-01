def add(m) -> list:
    unchanged = m
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    name = f"{first} {last}"
    m[0].append(name)
    act = input("Are you interested in acting? <y>es, <n>o: ")
    production = input("Are you interested in helping with the production? <y>es, <n>o: ")
    if act == "y":
        m[1].append(name)
    if production == "y":
        m[2].append(name)
    if first == "" or last == "":
        print("""You need to enter a first name AND a last name
Details have not been added. Please try again.""")
        print()
        return unchanged
    return m

def print_members(m) -> None:
    print("""
Our current list of members and preferences
-------------------------------------------

Members
------""")
    if len(members[0]) > 0: print(*(m for m in members[0]), sep='\n')
    print("""
Actors
------""")
    if len(members[1]) > 0: print(*(m for m in members[1]), sep='\n')
    print("""
Helpers
------""")
    if len(members[2]) > 0: print(*(m for m in members[2]), sep='\n')
    print()


if __name__ == '__main__':
    print("The Drama Tisers")
    print("----------------")
    print()
    print("Select an option below")
    print()
    members = [[], [], []]

    while True:
        options = input("<a>dd a new member, <p>rint members, <q>uit: ")
        if options == "a":
            members = add(members)
        elif options == "p":
            print_members(members)
        else: break
