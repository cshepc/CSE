world_map = {
    # 1
    'CELL1': {
        'NAME': "Cell",
        'DESCRIPTION': 'You are in a dimly lit prison cell. There is a single bed and a toilet in the corner. '
                       'A door hangs slightly ajar to the north.',
        'PATHS': {
            'NORTH': 'HALL1'
        }

    },
    # 2
    'HALL1': {
        'NAME': 'Hallway',
        'DESCRIPTION': 'You walk in to a relatively long hallway. At the north end there is a door. There is a door to '
                       'the south, and two doors to the east and west.',
        'PATHS': {
            'SOUTH': 'CELL1',
            'NORTH': 'SHOTGUN',
            'WEST': 'CELL2',
            'EAST': 'STAIRCASE1'
        }
    },
    # 3
    'CELL2': {
        'NAME': 'Formerly Occupied Cell',
        'DESCRIPTION': 'You are in a cell. There is a skeleton lying on the bed, and a light bulb is flickering above'
                       ' your head. There is a door behind you to th east',
        'PATHS': {
            'EAST': 'HALL1'
        }
    },
    # 4
    'STAIRCASE1': {
        'NAME': 'Staircase',
        'DESCRIPTION': 'You are in a room with a staircase leading up to a door. THe door appears locked. '
                       'There is a door to the west.',
        'PATHS': {
            'WEST': 'HALL1'
            # , 'UP': 'STAIRCASE2'
        }
    },
    # 5
    'SHOTGUN': {
        'NAME': 'Shotgun Room',
        'DESCRIPTION': 'You are in a room with a table in the center. There are doors to the north, south, east, '
                       'and west.',
        'PATHS': {
            'SOUTH': 'HALL1',
            'NORTH': 'HALL2',
            'WEST': 'GUARDROOM',
            'EAST': 'WELL1'
        }
    },
    # 6
    'WELL1': {
        'NAME': 'Bottom of Well',
        'DESCRIPTION': 'You are at the bottom of a well. There is a door to the west.',
        'PATHS': {
            'WEST': 'SHOTGUN',
        }
    },
    # 7
    'GUARDROOM': {
        'NAME': 'Guard Room',
        'DESCRIPTION': 'You are in a room with several computer monitors and bright harsh lights. There is a guard in '
                       'here that seems to have gone crazy. He rushes at you.',
        'PATHS': {
            'WEST': 'KEY1',
            'EAST': 'SHOTGUN'
        }
    },
    # 8
    'KEY1': {
        'NAME': "Key Room #1",
        'DESCRIPTION': 'You are in a room with a small table in the center. THere is a large brass key on the table.',
        'PATHS': {
            'EAST': 'GUARDROOM'
        }
    },
    # 9
    'HALL2': {
        'NAME': 'North/South Hallway',
        'DESCRIPTION': 'You are in a hallway with a door to the north and a door to the south. The north door '
                       'appears locked',
        'PATHS': {
            'NORTH': 'ARMORY',
            'SOUTH': 'SHOTGUN'
        }
    },
    # 10
    'ARMORY': {
        'NAME': 'ARMORY',
        'DESCRIPTION': 'You are in the armory. There is a bulletproof vest on a table in the middle of the room with'
                       ' three shotgun shells in it. There are doors to the north, south, east and west.',
        'PATHS': {
            'SOUTH': 'HALL2',
            'NORTH': 'GUARDHOUSE',
            'WEST': 'KEY2',
            'EAST': 'CAFETERIA'
        }
    },
    # 11
    'KEY2': {
        'NAME': 'Staircase Key Room',
        'DESCRIPTION': 'You are in a very dimly lit room. There is a small key on the floor in the corner. There is a '
                       'door to the east.',
        'PATHS': {
            'EAST': 'ARMORY'
        }
    },
    # 12
    'CAFETERIA': {
        'NAME': 'Cafeteria',
        'DESCRIPTION': '',
        'PATHS': {
            'WEST': 'ARMORY'
        }
    },
    # 13
    'GUARDHOUSE': {
        'NAME': 'Guards\' Quarters',
        'DESCRIPTION': 'You are in a room that seems to be the old guard\'s quarters. There is a bed on the wall with a'
                       ' backpack on it. There are doors to the south, north, and east.',
        'PATHS': {
            'SOUTH': 'ARMORY',
            'NORTH': 'GAMEROOM',
            'EAST': 'TUNNEL'
        }
    },
    # 14
    'TUNNEL': {
        'NAME': 'Secret Tunnel',
        'DESCRIPTION': 'You are in a secret tunnel that starts going east, slopes down south, and then curves back '
                       'west. There is a door to the north and to the south.',
        'PATHS': {
            'NORTH': 'GUARDHOUSE',
            'SOUTH': 'STAIRCASE1'
        }
    },
    # 15
    'GAMEROOM': {
        'NAME': 'Game Room',
        'DESCRIPTION': 'You are in a game room. There are arcade games on the wall, and in the middle there is a pool '
                       'table with some pool balls and cues on it. There is a door to the south.',
        'PATHS': {
            'SOUTH': 'GUARDHOUSE'
        }
    }
}

current_node = world_map['CELL1']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node['NAME'] + '\n' + current_node['DESCRIPTION'])

    command = input(">_")
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
