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
    def __init__(self, name, items=None):
        if items is None:
            items = []
        self.name = name
        self.items = items


class Item(object):
    def __init__(self, name, inventory_space, damage, accuracy, armor):
        self.name = name
        self.inventory_space = inventory_space
        self.damage = damage
        self.accuracy = accuracy
        self.armor = armor


class Character(object):
    def __init__(self, name, description, health, accuracy, base_damage, armor):
        self.name = name
        self.description = description
        self.health = health
        self.items = []
        self.inventory_space = 100
        self.accuracy = accuracy
        self.base_damage = base_damage
        self.armor = armor

    def pick_up(self, placeholder):
        if placeholder in self.items:
            print("You are already carrying the item")
        elif self.inventory_space < placeholder.inventory_space:
            print("Your inventory is full.")
        else:
            main.items.append(placeholder)
            room.items.remove(placeholder)
            main.accuracy += placeholder.accuracy
            main.base_damage += placeholder.damage
            main.armor += placeholder.armor
            main.inventory_space -= placeholder.inventory_space
            print('%s picked up the %s' % (main.name, placeholder.name))

    def put_down(self):
        if item in self.items:
            main.items.remove(item)
            room.items.append(item)
            main.accuracy -= item.accuracy
            main.base_damage -= item.damage
            main.armor -= item.armor
            main.inventory_space += item.inventory_space
            print('%s put down the %s' % (main.name, item.name))


item = Item('item', 10, 10, 10, 0)
item2 = Item('flashlight', 10, 10, 10, 0)
main = Character('You', 'The main character', 100, 70, 10, 0)
room = Room("room", [item, item2])

command = input('>_')
if 'pick up' in command:
    command = command[8:]
    acquired = False
    for num in range(len(room.items)):
        if command in room.items[num].name:
            main.pick_up(room.items[num])
            acquired = True
    if not acquired:
        print("You can't")
elif command == 'put down':
    main.put_down()
