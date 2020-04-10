# implement a class to hold room information
# this should have name and description attributes

from item import Item

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = [] if items is None else items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)