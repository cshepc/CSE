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
        if player.armor_equipped < 1:
            player.armor_equipped = 1
            player.armor += self.armor
        else:
            print("You can't do that right now.")


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, items: None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Character(object):
    def __init__(self, name, health, accuracy, base_damage, armor):
        self.name = name
        self.health = health
        self.items = []
        self.inventory_space = 100
        self.accuracy = accuracy
        self.base_damage = base_damage
        self.armor = armor
        self.alive = True

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
        damage_taken = attacker.base_damage - self.armor
        self.health -= damage_taken
        if self.health <= 0:
            print('%s died.' % self.name)
            self.alive = False


knife = Knife('Small Knife', 'A small hunting knife', 20, 15, 90)
shotgun = Gun("Shotgun", "A medium sized shotgun.", 40, 80, 60, 5)

staircase_key = Key('Staircase Key', '', 5, staircase.up, stair2)
guard_key = Key('Guard Room Key', '', 5, hall2.north, armory)
