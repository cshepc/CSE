# pick up items
# move?
# attack
# death
# dialogue
# perform Action(use, push, etc)
# status effect(paralyze, poison, burn, etc.)
# take damage
#
# Create a Character class. It must have five(5) instance variables. All five instance variable MUST be used.
# It must also have at least two (2) methods and a constructor.


class Room(object):
    def __init__(self, name):
        self.name = name
        self.items = []


class Item(object):
    def __init__(self, name, inventory_space):
        self.name = name
        self.inventory_space = inventory_space


class Character(object):
    def __init__(self, name, description, health, accuracy):
        self.name = name
        self.description = description
        self.health = health
        self.items = []
        self.inventory_space = 100
        self.accuracy = accuracy

    def pick_up(self):
        if item in self.items:
            print("You are already carrying the item")
        elif self.inventory_space < item.inventory_space:
            print("Your inventory is full.")
        else:
            item.picked_up = True
            room.items.remove(item)
            self.items.append(item)
            self.inventory_space = self.inventory_space - item.inventory_space
            print('You picked up the %s' % item.name)

    def put_down(self):
        if item in self.items:
            item.picked_up = False
            self.items.remove(self)
            room.items.remove(self)
            self.inventory_space += item.inventory_space
            print('You put down the %s' % item.name)


room = Room("room")
item = Item('item')
room.items.append(item)
