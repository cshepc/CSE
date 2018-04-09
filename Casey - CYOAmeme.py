from colorama import Fore, Style
import random


class Item(object):
    def __init__(self, name, description, inventory_space):
        self.name = name
        self.description = description
        self.inventory_space = inventory_space

    def get_picked_up(self, consumer, room):
        if consumer.inventory_space >= self.inventory_space:
            room.items.remove(self)
            consumer.items.append(self)
            consumer.inventory_space -= self.inventory_space
        else:
            print("You don't have room")

    def get_put_down(self, consumer):
        consumer.items.remove(self)
        consumer.inventory_space += self.inventory_space


class Consumable(Item):
    def __init__(self, name, description, inventory_space):
        super(Consumable, self).__init__(name, description, inventory_space)

    def get_consumed(self, consumer):
        print("%s consumed the %s" % consumer, self.name)
        consumer.items.remove(self)


class Food(Consumable):
    def __init__(self, name, description, inventory_space, hunger_restoration):
        super(Food, self).__init__(name, description, inventory_space)
        self.hunger_restore = hunger_restoration

    def get_consumed(self, consumer):
        print("%s ate the %s" % consumer.name, self.name)
        consumer.hunger += self.hunger_restore
        consumer.items.remove(self)


class HealthPack(Consumable):
    def __init__(self, name, description, inventory_space, health_boost):
        super(HealthPack, self).__init__(name, description, inventory_space)
        self.health_boost = health_boost

    def get_consumed(self, consumer):
        print("%s ate the %s. Their health was restored by %i" % consumer.name, self.name, self.health_boost)
        consumer.health += self.health_boost
        consumer.items.remove(self)


class Ammo(Consumable):
    def __init__(self, name, description, inventory_space, ammo):
        super(Ammo, self).__init__(name, description, inventory_space)
        self.ammo = ammo

    def reload(self, gun, char):
        gun.ammo += self.ammo
        char.items.remove(self)


class Weapon(Item):
    def __init__(self, name, description, inventory_space, damage, accuracy):
        super(Weapon, self).__init__(name, description, inventory_space)
        self.damage = damage
        self.accuracy = accuracy

    def get_picked_up(self, consumer, room):
        if consumer.inventory_space >= self.inventory_space:
            room.items.remove(self)
            consumer.items.append(self)
            consumer.inventory_space -= self.inventory_space
            consumer.damage += self.damage
            consumer.accuracy += self.accuracy
            consumer.accuracy = consumer.accuracy / 2
        else:
            print("You don't have room")

    def get_put_down(self, consumer):
        consumer.items.remove(self)
        consumer.inventory_space += self.inventory_space
        consumer.damage -= self.damage
        consumer.accuracy = consumer.accuracy * 2
        consumer.accuracy -= self.accuracy

    def attack(self, attacker, target):
        target.take_damage(attacker, self)


class Knife(Weapon):
    def __init__(self, name, description, inventory_space, damage, accuracy):
        super(Knife, self).__init__(name, description, inventory_space, damage, accuracy)


class Gun(Weapon):
    def __init__(self, name, description, inventory_space, damage, accuracy, ammunition):
        super(Gun, self).__init__(name, description, inventory_space, damage, accuracy)
        self.ammo = ammunition

    def attack(self, attacker, target):
        if self.ammo > 0:
            target.take_damage(attacker, self)
            self.ammo -= 1
        else:
            print("You are out of ammo.")


class Key(Item):
    def __init__(self, name, description, inventory_space, door, next_room):
        super(Key, self).__init__(name, description, inventory_space)
        self.door = door
        self.next_room = next_room

    def unlock(self, room,):
        room.door = self.next_room


class Wearable(Item):
    def __init__(self, name, description, inventory_space, clothing_type):
        super(Wearable, self).__init__(name, description, inventory_space)
        self.clothing_type = clothing_type

    def get_equipped(self, player):
        if None in player.armor.values(self.clothing_type):
            player.armor.append(self.clothing_type)
        else:
            print("You can't do that right now.")


class Armor(Wearable):
    def __init__(self, name, description, inventory_space, clothing_type, armor_boost):
        super(Armor, self).__init__(name, description, inventory_space, clothing_type)
        self.armor = armor_boost

    def get_equipped(self, player):
        if player.helmet_equipped < 1:
            player.helmet_equipped = 1
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Helmet(Armor):
    def __init__(self, name, description, inventory_space, clothing_type, armor_boost):
        super(Helmet, self).__init__(name, description, inventory_space, clothing_type)
        self.armor = armor_boost

    def get_equipped(self, player):
        if not player.helmet_equipped:
            player.helmet_equipped = True
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Chestplate(Armor):
    def __init__(self, name, description, inventory_space, clothing_type, armor_boost):
        super(Chestplate, self).__init__(name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.chestplate_equipped:
            player.chestplate_equipped = True
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Leggings(Armor):
    def __init__(self, name, description, inventory_space, clothing_type, armor_boost):
        super(Leggings, self).__init__(name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.leggings_equipped:
            player.leggings_equipped = True
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Boots(Armor):
    def __init__(self, name, description, inventory_space, clothing_type, armor_boost):
        super(Boots, self).__init__(name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.boots_equipped:
            player.boots_equipped = True
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Gauntlets(Armor):
    def __init__(self, name, description, inventory_space, clothing_type, armor_boost):
        super(Gauntlets, self).__init__(name, description, inventory_space, clothing_type, armor_boost)

    def get_equipped(self, player):
        if not player.gauntlets_equipped:
            player.gauntlets_equipped = True
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Bag(Item):
    def __init__(self, name, description, inventory_space, items, bag_space):
        super(Bag, self).__init__(name, description, inventory_space)
        self.items = items
        self.bag_space = bag_space

    def put_in(self, item, character):
        if self.bag_space >= item.inventory_space:
            character.items.remove(item)
            self.items.append(item)
            self.bag_space -= item.inventory_space
        else:
            print("The %s is full" % self.name)

    def take_out(self, item, character):
        if item in self.items:
            self.items.remove(item)
            character.items.append(item)
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Character(object):
    def __init__(self, name, health, evasiveness, accuracy, base_damage, armor, helmet, chestplate, leggings, boots,
                 gauntlets):
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

    def pick_up(self, item, room):
        if item in self.items:
            print("You are already carrying the item")
        elif self.inventory_space < item.inventory_space:
            print("Your inventory is full.")
        else:
            item.get_picked_up(self, room)

    def put_down(self, item, room):
        item.get_put_down(self, room)

    def attack(self, target):
        chance_of_succeeding = self.accuracy + target.evasiveness
        chance_of_succeeding = chance_of_succeeding / 2
        succeed_num = random.randint(1, 100)
        if chance_of_succeeding >= succeed_num:
            target.take_damage(self)
        else:
            print("%s missed." % self)

    def take_damage(self, attacker):
        damage_taken = attacker.base_damage - self.armor * 0.8
        self.health -= damage_taken
        if self.health <= 0:
            print('%s died.' % self.name)
            self.alive = False


# Items

# Cell2
knife = Knife('Small Knife', 'A small hunting knife', 20, 15, 90)
# Shotgun
shotgun = Gun("Shotgun", "A medium sized shotgun.", 40, 80, 60, 5)
# Armory
kevlar_helmet = Helmet('Kevlar Helmet', 'A black kevlar helmet', 10, 'armor', 10)
kevlar_chestplate = Chestplate('Kevlar Chestplate', 'A black kevlar chestplate', 30, 'armor', 20)
kevlar_leggings = Leggings('Kevlar Leggings', 'A pair of black kevlar leggings', 20, 'armor', 15)
steel_toed_boots = Boots('Steel Toed Boots', 'A pair of black steel toed boots', 10, 'armor', 10)
# Cafeteria
apple = Food('Apple', 'A delicious looking apple', 5, 20)
sandwich = Food('Sandwich', 'A turkey sandwich', 5, 40)
lunchbag = Bag("Lunchbag", 'a paper bag', 20, [apple, sandwich], 10)
# Guard House
pistol = Gun(name, description, inventory_space, damage, accuracy, ammunition)

# Rooms
cell1 = Room("Cell", 'You are in a dimly lit prison cell. There is a single bed and a toilet in the corner. A door '
                     'hangs slightly ajar to the north.', 'hall1', None, None, None, None, None, [])
hall1 = Room('Hallway', 'You walk in to a relatively long hallway. At the north end there is a door. There is a door to'
                        ' the south, and two doors to the east and west.', 'shotgun', 'cell1', 'staircase1', 'cell2',
             None, None, [], [])
cell2 = Room('Formerly Occupied Cell', 'You are in a cell. There is a skeleton lying on the bed, and a light bulb is '
             'flickering above your head. There is a door behind you to the east', None, None, 'hall1', None, None,
             None, [knife], [])
staircase1 = Room('Staircase', 'You are in a room with a staircase leading up to a door. The door appears locked. '
                               'There is a door to the west.', None, None, None, 'hall1', None, None, [], [])
shotgun = Room('Shotgun Room', 'You are in a room with a table in the center. There are doors to the north, south, east'
                               ', and west.', 'hall2', 'hall1', 'well1', 'guardroom', None, None, [shotgun], [])
well1 = Room('Bottom of Well', 'You are at the bottom of a well. There is a door to the west.', None, None, None,
             'shotgun', None, None, [], [])
guardroom = Room('Guard Room', 'You are in a room with several computer monitors and bright harsh lights. There is a '
                               'door to the east and o the west.', None, None, 'shotgun', 'key1', None, None, [])
key1 = Room('Key Room', 'You are in a room with a small table in the center. There is a door to the east.',
            None, None, 'guardroom', None, None, None, [], [])
hall2 = Room('North/South Hallway', 'You are in a hallway with a door to the north and a door to the south. The north '
                                    'door appears locked', 'armory', 'shotgun', None, None, None, None, [], [])
armory = Room('Armory', 'You are in the armory. There are doors to the north, south, east and west.',
              'guardhouse', 'hall2', 'cafeteria', 'key2', None, None, [kevlar_helmet, kevlar_chestplate,
                                                                       kevlar_leggings, steel_toed_boots], [])
key2 = Room('Staircase Key Room', 'You are in a very dimly lit room.  There is a door to the east.', None, None,
            'armory', None, None, None, [], [])
cafeteria = Room('Cafeteria', 'You walk in to what appears to be the former prison cafeteria. There is a door to the '
                              'west.', None, None, None, 'armory', None, None, [lunchbag], [])
guardhouse = Room('Guards\' Quarters', 'You are in a room that seems to be the old guard\'s quarters. There is a bed on'
                                       ' the wall with a backpack on it. There are doors to the south, north, and '
                                       'east.', 'gameroom', 'armory', 'tunnel', None, None, None)
tunnel = Room('Secret Tunnel', 'You are in a secret tunnel that starts going east, slopes down south, and then curves '
              'back west. There is a door to the north and to the south.', 'guardhouse', 'staircase1', None, None, None,
              None, [], [])
gameroom = Room('Game Room', 'You are in a game room. There are arcade games on the wall, and in the middle there is a '
                'pool table with some pool balls and cues on it. There is a door to the south.', None, 'guardhouse',
                None, None, None, None)

# Keys
staircase_key = Key('Staircase Key', '', 5, staircase1.up, staircase2)
key2.items.append(staircase_key)
guard_key = Key('Guard Room Key', '', 5, hall2.north, armory)
key1.items.append(guard_key)
