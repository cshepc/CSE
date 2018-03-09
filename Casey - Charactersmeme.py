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
import random


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
        self.alive = True

    def pick_up(self, thing):
        if thing in self.items:
            print("You are already carrying the item")
        elif self.inventory_space < thing.inventory_space:
            print("Your inventory is full.")
        else:
            main.items.append(thing)
            room.items.remove(thing)
            main.accuracy += thing.accuracy
            main.base_damage += thing.damage
            main.armor += thing.armor
            main.inventory_space -= thing.inventory_space
            print('%s picked up the %s' % (main.name, thing.name))

    def put_down(self, thing):
        self.items.remove(thing)
        room.items.append(thing)
        self.accuracy -= thing.accuracy
        self.base_damage -= thing.damage
        self.armor -= thing.armor
        self.inventory_space += thing.inventory_space
        print('%s put down the %s' % (main.name, thing.name))

    def attack(self, target):
        chance_of_succeeding = self.accuracy * target.evasiveness
        chance_of_succeeding = chance_of_succeeding / 2
        succeed_num = random.randint(1, 100)
        if chance_of_succeeding >= succeed_num:
            target.take_damage(self)
        else:
            print("%s missed." % self)

    def take_damage(self, attacker):
        damage_taken = attacker.base_damage - self.armor
        self.health -= damage_taken
        if self.health <= 0:
            print('%s died.' % self.name)
            self.alive = False


item = Item('item', 10, 10, 10, 0)
item2 = Item('flashlight', 10, 10, 10, 0)
main = Character('You', 'The main character', 100, 70, 10, 0)
room = Room("room", [item, item2])


while False:
    command = input('>_')
    if command == 'quit':
        quit(0)
    if 'pick up' in command:
        command = command[8:]
        acquired = False
        for num in range(len(room.items)):
            if command in room.items[num].name:
                main.pick_up(room.items[num])
                acquired = True
                break
        if not acquired:
            print("You can't")
    if 'put down' in command:
        command = command[8:]
        for num in range(len(main.items)):
            if command in main.items[num].name:
                main.put_down(main.items[num])
                dropped = True
