print("A feast of bugs")
print("---------------")

magpie = ["beetles", "caterpillars", "grasshoppers", "crickets", "spiders", "worms"]
kookaburra = ["beetles", "caterpillars", "grasshoppers", "crickets", "spiders"]
lorikeet = ["aphids", "caterpillars", "beetles", "spiders"]


insects = ["ants", "aphids", "beetles", "caterpillars", "cockroach", "flies", "termites", "crickets", "grasshoppers"]
invertebrates = ["beetles", "cockroaches", "spiders", "worms"]

print("Select from the following list of birds")
print("---------------------------------------")
print()
print("(1) Australian magpie")
print("(2) Kookaburra")
print("(3) Rainbow Lorikeet")
print()

bird = input("Bird choice: ")
if bird == "1":
    bug = input("Select either (1) Insects or (2) Invertebrates? ")
    if bug == "1":
        print("The Australian magpie prefers the following insects:")
        for each in insects:
            if each in magpie:
                print(f"* {each}")
    elif bug == "2":
        print("The Australian magpie prefers the following invertebrates:")
        for each in invertebrates:
            if each in magpie:
                print(f"* {each}")
    else:
        print("That's not a valid bug choice.")
elif bird == "2":
    bug = input("Select either (1) Insects or (2) Invertebrates? ")
    if bug == "1":
        print("The kookaburra prefers the following insects:")
        for each in insects:
            if each in kookaburra:
                print(f"* {each}")
    elif bug == "2":
        print("The kookaburra prefers the following invertebrates:")
        for each in invertebrates:
            if each in kookaburra:
                print(f"* {each}") 
    else:
        print("That's not a valid bug choice.")          
elif bird == "3":
    bug = input("Select either (1) Insects or (2) Invertebrates? ")
    if bug == "1":
        print("The Rainbow Lorikeet prefers the following insects:")
        for each in insects:
            if each in lorikeet:
                print(f"* {each}")
    elif bug == "2":
        print("The Rainbow Lorikeet prefers the following invertebrates:")
        for each in invertebrates:
            if each in lorikeet:
                print(f"* {each}")
    else:
        print("That's not a valid bug choice.")
else:
    print("That's not a valid bird choice.")