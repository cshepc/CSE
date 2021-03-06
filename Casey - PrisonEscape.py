from colorama import Fore, Style
import random


class Item(object):
    def __init__(self, name, short_name, description, inventory_space):
        self.name = name
        self.short_name = short_name
        self.description = description
        self.inventory_space = inventory_space

    def get_picked_up(self, consumer, room):
        if consumer.inventory_space >= self.inventory_space:
            room.items.remove(self)
            consumer.items.append(self)
            consumer.inventory_space -= self.inventory_space
        else:
            print("You don't have room")

    def get_put_down(self, consumer, room):
        consumer.items.remove(self)
        room.items.append(self)
        consumer.inventory_space += self.inventory_space


class Bottle(Item):
    def __init__(self, name, short_name, description, inventory_space, fill_space):
        super(Bottle, self).__init__(name, short_name, description, inventory_space)
        self.fill_space = fill_space

    def get_drunk(self, character):
        if self.fill_space > 0:
            self.fill_space -= 1
            print("You took a drink")
            character.thirst = 100
        else:
            print("Your %s is empty" % self.name)


class Consumable(Item):
    def __init__(self, name, short_name, description, inventory_space):
        super(Consumable, self).__init__(name, short_name, description, inventory_space)

    def get_consumed(self, consumer):
        print("%s consumed the %s" % consumer, self.name)
        consumer.items.remove(self)


class Food(Consumable):
    def __init__(self, name, short_name, description, inventory_space, hunger_restoration):
        super(Food, self).__init__(name, short_name, description, inventory_space)
        self.hunger_restore = hunger_restoration

    def get_consumed(self, consumer):
        print("%s ate the %s" % (consumer.name, self.name))
        consumer.hunger += self.hunger_restore
        consumer.items.remove(self)


class HealthPack(Consumable):
    def __init__(self, name, short_name, description, inventory_space, health_boost):
        super(HealthPack, self).__init__(name, short_name, description, inventory_space)
        self.health_boost = health_boost

    def get_consumed(self, consumer):
        print("%s ate the %s. Their health was restored by %i" % consumer.name, self.name, self.health_boost)
        consumer.health += self.health_boost
        consumer.items.remove(self)


class Ammo(Consumable):
    def __init__(self, name, short_name, description, inventory_space, ammo):
        super(Ammo, self).__init__(name, short_name, description, inventory_space)
        self.ammo = ammo

    def reload(self, gun, consumer):
        gun.ammo += self.ammo
        consumer.items.remove(self)


class Weapon(Item):
    def __init__(self, name, short_name, description, inventory_space, damage, accuracy):
        super(Weapon, self).__init__(name, short_name, description, inventory_space)
        self.damage = damage
        self.accuracy = accuracy

    def get_picked_up(self, consumer, room):
        if consumer.inventory_space >= self.inventory_space:
            room.items.remove(self)
            consumer.items.append(self)
            consumer.inventory_space -= self.inventory_space

        else:
            print("You don't have room")

    def get_put_down(self, consumer, room):
        consumer.items.remove(self)
        room.items.append(self)
        consumer.inventory_space += self.inventory_space

    def get_equipped(self, character):
        character.base_damage += self.damage
        character.accuracy += self.accuracy
        character.accuracy = character.accuracy / 2
        character.weapon = self
        character.items.remove(self)

    def get_unequipped(self, character):
        character.items.append(character.weapon)
        character.base_damage -= self.damage
        character.accuracy = character.accuracy * 2
        character.accuracy -= self.accuracy
        character.weapon = None

    def attack(self, attacker, target):
        target.take_damage(attacker, self)


class Knife(Weapon):
    def __init__(self, name, short_name, description, inventory_space, damage, accuracy):
        super(Knife, self).__init__(name, short_name, description, inventory_space, damage, accuracy)


class Gun(Weapon):
    def __init__(self, name, short_name, description, inventory_space, damage, accuracy, ammunition):
        super(Gun, self).__init__(name, short_name, description, inventory_space, damage, accuracy)
        self.ammo = ammunition

    def attack(self, attacker, target):
        if self.ammo > 0:
            target.take_damage(attacker, self)
            self.ammo -= 1
        else:
            print("You are out of ammo.")


class Key(Item):
    def __init__(self, name, short_name, description, inventory_space,  direction, next_room):
        super(Key, self).__init__(name, short_name, description, inventory_space)
        self.direction = direction
        self.next_room = next_room


class Wearable(Item):
    def __init__(self, name, short_name, description, inventory_space, clothing_type):
        super(Wearable, self).__init__(name, short_name, description, inventory_space)
        self.clothing_type = clothing_type

    def get_equipped(self, player):
        if None in player.armor.values(self.clothing_type):
            player.armor.append(self.clothing_type)
        else:
            print("You can't do that right now.")


class Armor(Wearable):
    def __init__(self, name, short_name, description, inventory_space, clothing_type, armor_boost):
        super(Armor, self).__init__(name, short_name, description, inventory_space, clothing_type)
        self.armor = armor_boost

    def get_equipped(self, player):
        if player.helmet_equipped < 1:
            player.helmet_equipped = 1
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Helmet(Armor):
    def __init__(self, name, short_name, description, inventory_space, clothing_type, armor_boost):
        super(Helmet, self).__init__(name, short_name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.helmet_equipped:
            player.items.remove(self)
            player.helmet = self
            player.helmet_equipped = True
            player.armor += self.armor
            print("You put on the %s." % self.name)
        else:
            print("You can't do that right now.")

    def get_unequipped(self, player):
        if player.helmet_equipped:
            player.items.append(self)
            player.helmet = None
            player.helmet_equipped = False
            player.armor -= self.armor
            print("You took off the %s." % self.name)
        else:
            print("You can't do that right now.")


class Chestplate(Armor):
    def __init__(self, name, short_name, description, inventory_space, clothing_type, armor_boost):
        super(Chestplate, self).__init__(name, short_name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.chestplate_equipped:
            player.items.remove(self)
            player.helmet = self
            player.helmet_equipped = True
            player.armor += self.armor
            print("You put on the %s." % self.name)
        else:
            print("You can't do that right now.")

    def get_unequipped(self, player):
        if player.chestplate_equipped:
            player.items.append(self)
            player.chestplate = None
            player.chestplate_equipped = False
            player.armor -= self.armor
            print("You took off the %s." % self.name)
        else:
            print("You can't do that right now.")


class Leggings(Armor):
    def __init__(self, name, short_name, description, inventory_space, clothing_type, armor_boost):
        super(Leggings, self).__init__(name, short_name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.leggings_equipped:
            player.items.remove(self)
            player.leggings = self
            player.leggings_equipped = True
            player.armor += self.armor
            print("You put on the %s." % self.name)
        else:
            print("You can't do that right now.")

    def get_unequipped(self, player):
        if player.leggings_equipped:
            player.items.append(self)
            player.leggings = None
            player.leggings_equipped = False
            player.armor -= self.armor
            print("You took off the %s." % self.name)
        else:
            print("You can't do that right now.")


class Boots(Armor):
    def __init__(self, name, short_name, description, inventory_space, clothing_type, armor_boost):
        super(Boots, self).__init__(name, short_name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.boots_equipped:
            player.items.remove(self)
            player.boots = self
            player.boots_equipped = True
            player.armor += self.armor
            print("You put on the %s." % self.name)
        else:
            print("You can't do that right now.")


class Gauntlets(Armor):
    def __init__(self, name, short_name, description, inventory_space, clothing_type, armor_boost):
        super(Gauntlets, self).__init__(name, short_name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.gauntlets_equipped:
            player.gauntlets_equipped = True
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Bag(Item):
    def __init__(self, name, short_name, description, inventory_space, items, bag_space):
        super(Bag, self).__init__(name, short_name, description, inventory_space)
        self.items = items
        self.bag_space = bag_space

    def put_in(self, thing, character):
        if self.bag_space >= thing.inventory_space:
            character.items.remove(thing)
            self.items.append(thing)
            self.bag_space -= thing.inventory_space
        else:
            print("The %s is full" % self.name)

    def take_out(self, thing, character):
        if thing in self.items:
            self.items.remove(thing)
            character.items.append(thing)
        else:
            print("You can't do that right now.")


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, items, characters):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.items = items
        self.characters = characters
        self.first = True
        self.fillable = False

    def move(self, direction):
        global current_node
        current_node.first = False
        current_node = globals()[getattr(self, direction)]


class Character(object):
    def __init__(self, name, health, evasiveness, accuracy, base_damage, armor, helmet, chestplate, leggings, boots,
                 gauntlets, hostile, hunger, weapon):
        self.name = name
        self.health = health
        self.items = []
        self.inventory_space = 100
        self.evasiveness = evasiveness
        #  weapons
        self.accuracy = accuracy
        self.base_damage = base_damage
        # armor
        self.armor = armor
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.gauntlets = gauntlets
        self.alive = True
        self.helmet_equipped = False
        self.chestplate_equipped = False
        self.leggings_equipped = False
        self.boots_equipped = False
        self.gauntlets_equipped = False
        self.description = None
        self.attacking = False
        self.hostile = hostile
        self.hunger = hunger
        self.weapon = weapon

    def pick_up(self, thing, room):
        global inventory_full
        if thing in self.items:
            print("You are already carrying the item")
        elif self.inventory_space < thing.inventory_space:
            print("Your inventory is full.")
            inventory_full = True
        else:
            thing.get_picked_up(self, room)

    def put_down(self, thing):
        thing.get_put_down(self, current_node)

    def attack(self, target):
        chance_of_succeeding = self.accuracy + target.evasiveness
        chance_of_succeeding = chance_of_succeeding / 2
        succeed_num = random.randint(1, 100)
        if chance_of_succeeding >= succeed_num:
            target.take_damage(self)
        else:
            print("%s missed." % self.name)

    def take_damage(self, attacker):
        damage_taken = attacker.base_damage - self.armor * 0.8
        self.health -= damage_taken
        print("%s hit %s for %i damage." % (attacker.name, self.name, damage_taken))
        if self.health <= 0:
            self.die()

    def die(self):
        global current_node
        print("%s has died" % self.name)
        current_node.characters.remove(self)
        for thingy in self.items:
            current_node.items.append(thingy)
        self.alive = False

    def eat(self, food):
        food.get_consumed(self)

    def equip(self, thingy):
        thingy.get_equipped(self)

    def unequip(self, thingy):
        thingy.get_unequipped(self)

    def drink(self, bottle):
        bottle.get_drunk(self)


class MainCharacter(Character):
    def __init__(self, name, health, evasiveness, accuracy, base_damage, armor, helmet, chestplate, leggings, boots,
                 gauntlets, hunger, weapon, hostile=False):
        super(MainCharacter, self).__init__(name, health, evasiveness, accuracy, base_damage, armor, helmet, chestplate,
                                            leggings, boots, gauntlets, hostile, hunger, weapon)
        self.under_attack = False
        self.thirst = 100

    def die(self):
        global current_node
        print("%s has died" % self.name)
        for thingy in self.items:
            current_node.items.append(thingy)
        self.alive = False
        respawn = input("Do you want to respawn? >_")
        if respawn == 'yes':
            current_node = cell1
            main_character.thirst = 100
            main_character.hunger = 100

        else:
            exit(0)


def equip(thingy, slot):
    if main_character.__getattribute__(slot) is None:

        if slot == 'weapon':
            equip_weapon = input("You are not carrying a weapon. would you like to equip the %s?" % thingy.name)
            if equip_weapon == 'yes':
                main_character.equip(thingy)
                print("You equipped the %s." % thingy.name)
            else:
                pass

        else:
            equip_weapon = input("You are not wearing a %s. would you like to put on this %s?" % (slot, slot))
            if equip_weapon == 'yes':
                main_character.equip(thingy)

    else:
        if slot == 'weapon':
            equip_weapon = input("You are already carrying a weapon. would you like to equip the %s?" % thingy.name)
            if equip_weapon == 'yes':
                main_character.unequip(main_character.weapon)
                main_character.equip(thingy)

        else:
            equip_weapon = input("You are already wearing a %s. would you like to put on this %s?" % (slot, slot))
            if equip_weapon == 'yes':
                main_character.unequip(main_character.__getattribute__(slot))
                main_character.equip(thingy)


# Items

# Cell2
knife = Knife('Small Knife', 'knife', 'There is a small knife in the room.', 20, 15, 90)
ham_sandwich = Food("Ham Sandwich", 'ham sandwich', 'There is a ham sandwich in the room.', 10, 30)
water_bottle = Bottle("Water bottle", 'water bottle', 'There is a water bottle in the room.', 5, 3)
# Shotgun
shotgun = Gun("Shotgun", 'shotgun', "There is a shotgun in the room.", 40, 80, 60, 5)
# Armory
kevlar_helmet = Helmet('Kevlar Helmet', 'helmet', 'There is a black kevlar helmet in the room. ', 10, 'armor', 10)
kevlar_chestplate = Chestplate('Kevlar Chestplate', 'chestplate', 'There is a black kevlar chestplate in the room. ',
                               30, 'armor', 20)
kevlar_leggings = Leggings('Kevlar Leggings', 'leggings', 'There is a pair of black kevlar leggings in the room. ', 20,
                           'armor', 15)
steel_toed_boots = Boots('Steel Toed Boots', 'boots', 'There is a pair of black steel toed boots in the room. ', 10,
                         'armor', 10)
# Cafeteria
apple = Food('Apple', 'apple', 'A delicious looking apple is in the room.', 5, 20)
sandwich = Food('Sandwich', 'sandwich', 'A turkey sandwich is in the room.', 5, 40)
# Guard House
pistol = Gun("Pistol", 'pistol', "A small black pistol", 20, 20, 70, 5)

main_character = MainCharacter("You", 100, 90, 90, 10, 0, None, None, None, None, None, 100, None, False)
guard1 = Character("Insane Guard", 100, 90, 60, 20, 0, None, None, None, None, None, True, None, None)
guard1.description = "There is a person in the room blocking the door."

# Rooms
cell1 = Room("Cell", 'You are in a dimly lit prison cell. There is a single bed and a toilet in the corner. A door '
                     'hangs slightly ajar to the north. ', 'hall1', None, None, None, None, None, [], [])
hall1 = Room('Hallway', 'You walk in to a relatively long hallway. At the north end there is a door. There is a door to'
                        ' the south, and two doors to the east and west. ', 'shotgun', 'cell1', 'staircase1', 'cell2',
             None, None, [], [])
cell2 = Room('Formerly Occupied Cell', 'You are in a cell. There is a skeleton lying on the bed, and a light bulb is '
             'flickering above your head. There is a door behind you to the east. ', None, None, 'hall1', None, None,
             None, [knife, ham_sandwich, water_bottle], [])
staircase1 = Room('Staircase', 'You are in a room with a staircase leading up to a door. The door appears locked. '
                               'There is a door to the west. ', None, None, None, 'hall1', None, None, [apple], [])
staircase1.locked_door = 'up'
shotgun = Room('Shotgun Room', 'You are in a room with a table in the center. There are doors to the north, south, east'
                               ', and west. ', 'hall2', 'hall1', 'well1', 'guardroom', None, None, [shotgun], [])
well1 = Room('Bottom of Well', 'You are at the bottom of a well. There is a door to the west. ', None, None, None,
             'shotgun', None, None, [apple], [])
well1.fillable = True
guardroom = Room('Guard Room', 'You are in a room with several computer monitors and bright harsh lights. There is a '
                               'door to the east and to the west. ', None, None, 'shotgun', 'key1', None, None, [],
                               [guard1])
key1 = Room('Key Room', 'You are in a room with a small table in the center. There is a door to the east. ',
            None, None, 'guardroom', None, None, None, [], [])
hall2 = Room('North/South Hallway', 'You are in a hallway with a door to the north and a door to the south. The north '
                                    'door appears locked ', None, 'shotgun', None, None, None, None, [], [])
hall2.locked_door = 'north'
armory = Room('Armory', 'You are in the armory. There are doors to the north, south, east and west. ',
              'guardhouse', 'hall2', 'cafeteria', 'key2', None, None, [kevlar_helmet, kevlar_chestplate,
                                                                       kevlar_leggings, steel_toed_boots, apple], [])
key2 = Room('Staircase Key Room', 'You are in a very dimly lit room.  There is a door to the east. ', None, None,
            'armory', None, None, None, [], [])
cafeteria = Room('Cafeteria', 'You walk in to what appears to be the former prison cafeteria. There is a door to the '
                              'west. ', None, None, None, 'armory', None, None, [apple, sandwich], [])
guardhouse = Room('Guards\' Quarters', 'You are in a room that seems to be the old guard\'s quarters. There is a bed on'
                                       ' the wall with a backpack on it. There are doors to the south, north, and '
                                       'east. ', 'gameroom', 'armory', 'tunnel', None, None, None, [pistol], [])
tunnel = Room('Secret Tunnel', 'You are in a secret tunnel that starts going east, slopes down south, and then curves '
              'back west. There is a door to the north and to the south. ', 'guardhouse', 'staircase1', None, None,
              None, None, [], [])
gameroom = Room('Game Room', 'You are in a game room. There are arcade games on the wall, and in the middle there is a '
                'pool table with some pool balls and cues on it. There is a door to the south. ', None, 'guardhouse',
                None, None, None, None, [], [])
staircase2 = Room('Staircase Floor 2', 'You are on a staircase landing. ', 'win_room', None, None, None, None,
                  'staircase1', [apple], [])
win_room = Room("You Win!", "Congrats! You won the game!", None, None, None, None, None, None, [], [])

# Keys
staircase_key = Key('Staircase Key', 'key', 'There is a small key in the room.', 5, staircase1.up, 'staircase2')
key2.items.append(staircase_key)
stair = 'You are in a room with a staircase leading up to a door. There is a door to the west. '
guard_key = Key('Armory Key', 'key', 'There is a small key in the room.', 5, hall2.north, armory)
key1.items.append(guard_key)

current_node = cell1
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
attacking_char = None
inventory_full = False
warning1_food = False
warning2_food = False
warning3_food = False
warning1_water = False
warning2_water = False
warning3_water = False

print(Fore.LIGHTRED_EX + "Welcome to Prison Escape!" + Style.RESET_ALL)
inst = input("Would you like some instructions? (y/n)>_")
if inst == 'y':
    print("To move north, type 'north' or 'n'. \nTo move south, type 'south' or 's'.To move east, type 'east' or 'e'. "
          "\nTo move west, type 'west' or 'w'. \nTo move up, type 'up' or 'u'. \nTo move down, type 'down' or 'd'. \nTo"
          " see the items in your inventory, type 'i'.\nTo see the description of a room again, type 'l'.\nTo view your"
          " statistics, type 'stats'.\nTo pick up an item, type 'pick up' plus the name of the item.\nTo put down an "
          "item, type'put down' plus the name of the item.\n" + Fore.YELLOW + "Now, Enjoy...\n\n" + Style.RESET_ALL)
else:
    print("Oh, I see, you know everything! Good luck, and if you need help, type '?' for a list of commands. \n" +
          Fore.YELLOW + "Now, Enjoy...\n\n" + Style.RESET_ALL)

print(Style.BRIGHT + "  _____      _                   ______                           \n"
                     " |  __ \    (_)                 |  ____|                         \n"
                     " | |__) | __ _ ___  ___  _ __   | |__   ___  ___ __ _ _ __   ___ \n"
                     " |  ___/ '__| / __|/ _ \| '_ \  |  __| / __|/ __/ _` | '_ \ / _ \ \n"
                     " | |   | |  | \__ \ (_) | | | | | |____\__ \ (_| (_| | |_) |  __/\n"
                     " |_|   |_|  |_|___/\___/|_| |_| |______|___/\___\__,_| .__/ \___|\n"
                     "                                                     | |         \n"
                     "                                                     |_|         \n"
      + Style.RESET_ALL)

while True:
    desc = ''
    for item in current_node.items:
        desc += ('\n' + item.description)
    print('============================================================================================================'
          + '=====================================' + '\n' + Fore.BLUE + current_node.name + Style.RESET_ALL)

    if current_node.first:
        print(current_node.description + desc + '\n' + '==============================================================='
                                                       '==============================================================='
                                                       '===================')
        if current_node == win_room:
            exit(0)

    for char in current_node.characters:
        if isinstance(char, Character) and not isinstance(char, MainCharacter):
            print(char.description)
            if char.hostile:
                print("They rush at you.")
                char.attacking = True
                main_character.under_attack = True
                attacking_char = char

    command = input(">_").lower().strip()
    long_command = list(command)

    if command == 'quit':
        print("Thanks for Playing!")
        quit()

    elif current_node == win_room:
        exit(0)

    elif command in short_directions:
        command = directions[short_directions.index(command)]

    if command in directions:
        try:
            current_node.move(command)
            main_character.hunger -= 7
            main_character.thirst -= 5
            if main_character.hunger < 1:
                main_character.die()
            if main_character.thirst < 1:
                main_character.die()
        except KeyError:
            print("You cannot go this way")

    elif command == 'jump':
        print(Fore.GREEN + Style.BRIGHT + 'Whee!' + Style.RESET_ALL)

    elif 'eat' in command:
        for stuff in main_character.items:
            if isinstance(stuff, Food):
                main_character.eat(stuff)
    elif command == 'l':
        print(current_node.items)
        current_node.first = True

    elif command == 'i':
        print("Items:")
        for item in main_character.items:
            print("    " + item.name)

    elif command == 'stats':
        print("You have %i health left." % main_character.health)
        print("You have %i armor." % main_character.armor)
        print("With each blow, you deal %i damage." % main_character.base_damage)
        print("You have %i hunger left." % main_character.hunger)
        print("You have %i thirst." % main_character.thirst)
        print("You have %i inventory space left." % main_character.inventory_space)

    elif command == '?':
        print("To move north, type 'north' or 'n'. \nTo move south, type 'south' or 's'.To move east, type 'east' or "
              "'e'. \nTo move west, type 'west' or 'w'. \nTo move up, type 'up' or 'u'. \nTo move down, type 'down' or "
              "'d'. \nTo see the items in your inventory, type 'i'.\nTo see the description of a room again, type 'l'."
              "\nTo view your statistics, type 'stats'. \nTo pick up an item, type 'pick up' plus the name of the item."
              "\nTo put down an item, type'put down' plus the name of the item.")

    elif 'pick up' in command:
        added = False
        for item in current_node.items:
            if command[8:] == item.short_name:
                if inventory_full:
                    break
                    added = False
                main_character.pick_up(item, current_node)
                added = True
                print("You picked up the %s" % item.name)
                if isinstance(item, Weapon):
                    equip(item, 'weapon')

                if isinstance(item, Helmet):
                    equip(item, 'helmet')
                if isinstance(item, Chestplate):
                    equip(item, 'chestplate')
                if isinstance(item, Leggings):
                    equip(item, 'leggings')
                if isinstance(item, Boots):
                    equip(item, 'boots')
        if not added:
            print("I don't see it there")

    elif 'put down' in command:
        for item in main_character.items:
            if command[9:] == item.short_name.lower():
                main_character.put_down(item)
                print("You put down the %s" % item.name)

    elif 'unlock' in command:

        if current_node == hall2:
            if guard_key in main_character.items:
                hall2.north = 'armory'
                print("You unlocked the door")
                hall2.description = 'You are in a hallway with a door to the north and a door to the south.'
            else:
                print("You do not have a key")

        elif current_node == staircase1:
            if staircase_key in main_character.items:
                staircase1.up = 'staircase2'
                print("You unlocked the door.")
                staircase1.description = stair
            else:
                print("You do not have the key.")

    elif 'equip' in command:
        for item in main_character.items:
            if isinstance(item, Weapon):
                if item.short_name == command[6:]:
                    if main_character.weapon is None:
                        main_character.equip(item)
                        print("You equipped the %s" % item.name)
                    else:
                        equip_item = input("You already have a weapon equipped. \n Would you like to replace the %s"
                                           " with the %s? >_" % (main_character.weapon.name, item.name))
                        if equip_item == 'yes':
                            print("You replaced the %s with the %s" % (main_character.weapon.name, item.name))
                            main_character.unequip(main_character.weapon)
                            main_character.equip(item)

    elif 'put on' in command:

        if 'helmet' in command:
            for stuff in main_character.items:
                if type(stuff) is Helmet:
                    stuff.get_equipped(main_character)

        elif 'chestplate' in command:
            for stuff in main_character.items:
                if type(stuff) is Chestplate:
                    stuff.get_equipped(main_character)

        elif 'leggings' in command:
            for stuff in main_character.items:
                if type(stuff) is Leggings:
                    stuff.get_equipped(main_character)

        elif 'boots' in command:
            for stuff in main_character.items:
                if type(stuff) is Boots:
                    stuff.get_equipped(main_character)

        elif 'gauntlets' in command:
            for stuff in main_character.items:
                if type(stuff) is Gauntlets:
                    stuff.get_equipped(main_character)

    elif 'take off' in command:
        if 'helmet' in command:
            main_character.helmet.get_unequipped(main_character)
        elif 'chestplate' in command:
            main_character.chestplate.get_unequipped(main_character)
        elif 'leggings' in command:
            main_character.leggings.get_unequipped(main_character)
        elif 'boots' in command:
            main_character.boots.get_unequipped(main_character)
        elif 'gauntlets' in command:
            main_character.gauntlets.get_unequipped(main_character)

    elif 'drink' in command:
        for item in main_character.items:
            if isinstance(item, Bottle):
                main_character.drink(item)

    elif 'fill' in command:
        if water_bottle in main_character.items:
            if current_node == well1:
                water_bottle.fill_space = 5
            else:
                print("You can't do that here.")
        else:
            print("You have nothing to fill.")

    elif command == "oh, worm?":
        print(Fore.YELLOW + 'You Win!' + Style.RESET_ALL)
        exit(0)

    elif 'attack' in command:
        if main_character.under_attack:
            main_character.attack(attacking_char)
        else:
            print("There's nothing to fight.")

    else:
        print(Fore.RED + "Command not recognized" + Style.RESET_ALL)

    if main_character.under_attack:
        for char in current_node.characters:
            if char.attacking:
                char.attack(main_character)

    print('\n')

    if not warning1_food:
        if main_character.hunger < 51:
            print("You are starting to feel a bit hungry.")
            warning1_food = True
    else:
        if not warning2_food:
            if main_character.hunger < 26:
                print("You are pretty hungry. You should eat something soon.")
                warning2_food = True
        else:
            if not warning3_food:
                if main_character.hunger < 3:
                    print("You cannot take another step without eating.")
                    warning3_food = True

    if not warning1_water:
        if main_character.thirst < 51:
            print("You are starting to feel a bit thirsty.")
            warning1_water = True
    else:
        if not warning2_water:
            if main_character.thirst < 26:
                print("You are pretty thirsty. You should drink some water soon.")
                warning2_water = True
        else:
            if not warning3_water:
                if main_character.thirst < 6:
                    print("You cannot take another step without drinking.")
                    warning3_water = True
