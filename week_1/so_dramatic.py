def add(m) -> list:
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
    return m

def print_members(m) -> None:


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


'''
<a>dd a new member, <p>rint members, <q>uit: a
Enter your first name: Trixie
Enter your last name: Wizzlefizz
Are you interested in acting? <y>es, <n>o: y
Are you interested in helping with the production? <y>es, <n>o: y
<a>dd a new member, <p>rint members, <q>uit: p

Our current list of members and preferences
-------------------------------------------
'''