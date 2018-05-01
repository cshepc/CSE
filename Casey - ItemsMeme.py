class Item(object):
    def __init__(self, name, description, inventory_space):
        self.name = name
        self.description = description
        self.inventory_space = inventory_space

    def get_picked_up(self, consumer):
        if consumer.inventory_space >= self.inventory_space:
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


class Weapon(Item):
    def __init__(self, name, description, inventory_space, damage, accuracy):
        super(Weapon, self).__init__(name, description, inventory_space)
        self.damage = damage
        self.accuracy = accuracy

    def get_picked_up(self, consumer):
        if consumer.inventory_space >= self.inventory_space:
            consumer.items.append(self)
            consumer.inventory_space -= self.inventory_space
            consumer.damage += self.damage
            consumer.accuracy += self.accuracy
            consumer.accuracy = consumer.accuracy / 2
        else:
            print("You don't have room")

    def get_put_down(self, consumer, room):
        consumer.items.remove(self)
        room.items.append(self)
        consumer.inventory_space += self.inventory_space
        consumer.damage -= self.damage
        consumer.accuracy = consumer.accuracy * 2
        consumer.accuracy -= self.accuracy

    def attack(self, attacker, target):
        target.take_damage(attacker, self)


class Knife(Weapon):
    def __init__(self, name, description, inventory_space, damage, accuracy):
        super(Knife, self).__init__(name, description, inventory_space, damage, accuracy)


class Key(Item):
    def __init__(self, name, description, inventory_space):
        super(Key, self).__init__(name, description, inventory_space)

    def unlock(self):


class Wearable(Item):
    def __init__(self, name, description, inventory_space, clothing_type):
        super(Wearable, self).__init__(name, description, inventory_space)
        self.clothing_type = clothing_type

    def get_equipped(self, player):
        if None in player.armor.values(self.clothing_type):
            player.armor.(self.clothing_type)
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

