class Item(object):
    def __init__(self, name, description, inventory_space):
        self.name = name
        self.description = description
        self.inventory_space = inventory_space

    def pick_up(self):
