world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': 'You are west of a white house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }

    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': 'You are south of a white house.',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': 'You are north of a white house.',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}
