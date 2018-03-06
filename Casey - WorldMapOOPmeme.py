from colorama import Fore, Style


class Settings:
    main_health = 10
    main_hunger = 50
    main_inventory = 100
    main_items = []


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
        self.items = []

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Item(object):
    def __init__(self, name, description, inventory_space):
        self.name = name
        self.description = description
        self.inventory_space = inventory_space
        self.picked_up = False

    def pick_up(self):
        if self.picked_up:
            print("You are already carrying the %s." % self.name)
        elif Settings.main_inventory < self.inventory_space:
            print(Fore.RED + "Your inventory is full." + Style.RESET_ALL)
        else:
            self.picked_up = True
            current_node.items.remove(self)
            Settings.main_items.append(self)
            Settings.main_inventory = Settings.main_inventory - self.inventory_space
            print('You picked up the %s' % self.name)

    def put_down(self):
        if self.picked_up:
            self.picked_up = False
            current_node.items.append(self)
            Settings.main_items.remove(self)
            Settings.main_inventory += self.inventory_space
            print('You put down the %s' % self.name)


class Character(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.alive = True
        self.inventory = []


player = Character("Casey", "Me")
testItem = Item('test', 'Test Item', 20)
cell1 = Room("Cell", 'You are in a dimly lit prison cell. There is a single bed and a toilet in the corner. A door '
                     'hangs slightly ajar to the north.', 'hall1', None, None, None, None, None)
cell1.items.append(testItem)
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
well1 = Room('Bottom of Well', 'You are at the bottom of a well. There is a door to the west.', None, None, None,
             'shotgun', None, None)
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
cafeteria = Room('Cafeteria', 'You walk in to what appears to be the former prison cafeteria. There is a bag on one of '
                              'the tables. There is a door to the west.', None, None, None, 'armory', None, None)
guardhouse = Room('Guards\' Quarters', 'You are in a room that seems to be the old guard\'s quarters. There is a bed on'
                                       ' the wall with a backpack on it. There are doors to the south, north, and '
                                       'east.', 'gameroom', 'armory', 'tunnel', None, None, None)
tunnel = Room('Secret Tunnel', 'You are in a secret tunnel that starts going east, slopes down south, and then curves '
              'back west. There is a door to the north and to the south.', 'guardhouse', 'staircase1', None, None, None,
              None)
gameroom = Room('Game Room', 'You are in a game room. There are arcade games on the wall, and in the middle there is a '
                'pool table with some pool balls and cues on it. There is a door to the south.', None, 'guardhouse',
                None, None, None, None)
current_node = cell1
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
long_test_name = list(testItem.name)

while True:
    print('\n' + Fore.BLUE + current_node.name + Style.RESET_ALL + '\n' + current_node.description)
    command = input(">_").lower().strip()
    long_command = list(command)
    if command == 'quit':
        print("Thanks for Playing!")
        quit(0)
    elif command in short_directions:
        command = directions[short_directions.index(command)]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    elif command == 'jump':
        print(Fore.GREEN + Style.BRIGHT + 'Whee!' + Style.RESET_ALL)
    elif 'pick up' in command:
        added = False
        for item in current_node.items:
            if command[7:] == item.name.lower():
                player.inventory.append(item)
                added = True
        if not added:
            print("I don't see it there")

    else:
        print(Fore.RED + "Command not recognized" + Style.RESET_ALL)
