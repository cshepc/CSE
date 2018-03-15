class Item(object):
    def __init__(self, name, description, inventory_space):
        self.name = name
        self.description = description
        self.inventory_space = inventory_space

    def get_picked_up(self, consumer):
        if consumer.inventory_space >= self.inventory_space:
            consumer.items.append(self)
            consumer.inventory_space -= self.inventory_space
        elif


class Consumable(Item):
    def __init__(self, name, description, inventory_space):
        super(Consumable, self).__init__(name, description, inventory_space)

    def get_consumed(self, consumer):

