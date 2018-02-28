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
hall1 = Room('Hallway', 'You walk in to a relatively long hallway. At the north end there is a door. There is a door to'
                        ' the south, and two doors to the east and west.', 'shotgun', 'cell1', 'staircase1', 'cell2',
             None, None)
cell2 = Room('Formerly Occupied Cell', 'You are in a cell. There is a skeleton lying on the bed, and a light bulb is '
                                       'flickering above your head. There is a door behind you to th east',
             None, None, 'hall1', None, None, None)
staircase1 = Room('Staircase', 'You are in a room with a staircase leading up to a door. The door appears locked. '
                               'There is a door to the west.', None, None, None, 'hall1', None, None)
shotgun = Room('Shotgun Room', 'You are in a room with a table in the center. There are doors to the north, south, east'
                               ', and west.', 'hall2', 'hall1', 'well1', 'guardroom', None, None)
well1 = Room('Bottom of Well', 'You are at the bottom of a well. There is a door to the west.', None, None, None, 'shot'
             'gun', None, None)
guardroom = Room('Guard Room', 'You are in a room with several computer monitors and bright harsh lights. There is a '
                               'door to the east and o the west.', None, None, 'shotgun', 'key1', None, None)
key1 = Room('Key Room', 'You are in a room with a small table in the center. There is a large brass key on the table. '
            'There is a door to the east.', None, None, 'guardroom', None, None, None)
hall2 = Room('North/South Hallway', 'You are in a hallway with a door to the north and a door to the south. The north '
                                    'door appears locked', 'armory', 'shotgun', None, None, None, None)
armory = Room('Armory', 'You are in the armory. There is a bulletproof vest on a table in the middle of the room with'
              ' three shotgun shells in it. There are doors to the north, south, east and west.', 'guardhouse',
              'hall2', 'cafeteria', 'key2', None, None)
key2 = Room('Staircase Key Room', 'You are in a very dimly lit room. There is a small key on the floor in the corner. '
                                  'There is a door to the east.', None, None, 'armory', None, None, None)
# cafeteria = Room()
# guardhouse = Room()
# tunnel = Room()
# gameroom = Room()
current_node = cell1
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while True:
    print('\n' + current_node.name + '\n' + current_node.description)
    command = input(">_")
    if command == 'quit':
        quit(0)
    if command in short_directions:
        command = directions[short_directions.index(command)]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
