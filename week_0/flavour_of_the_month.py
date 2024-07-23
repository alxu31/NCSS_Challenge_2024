
with open("resources/flavours.txt") as txtfile:
# with open("flavours.txt") as txtfile:
    flavours = [line.strip() for line in txtfile]

while True:
    flavour = input("Check flavour: ")
    if not flavour: break
    elif flavour in flavours: print("Done it already.")
    else: print("Sounds good!")