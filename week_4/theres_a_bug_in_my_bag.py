class Backpack:
    def __init__(self, brand, colour, capacity):
        self.brand = brand
        self.colour = colour
        self.capacity = capacity

if __name__ == '__main__':
    my_backpack = Backpack('Billabong', 'Aqua', 18)
    print(my_backpack.colour)