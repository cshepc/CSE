class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


cell1 = Room("Cell", 'You are in a dimly lit prison cell. There is a single bed and a toilet in the corner. A door '
                     'hangs slightly ajar to the north.', 'hall1', None, None, None, None, None)
hall1 = Room()
cell2 = Room()
staircase1 = Room()
shotgun = Room()
well1 = Room()
guardroom = Room()
key1 = Room()
armory = Room()
hall2 = Room()
cafeteria = Room()
guardhouse = Room()
current_node = cell1
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while True:
    print(current_node.name + '\n' + current_node.description)
    command = input(">_")
    if command == 'quit':
        quit(0)
    if command in directions:
        try:

        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
