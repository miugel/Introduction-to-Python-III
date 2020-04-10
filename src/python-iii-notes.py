class Animal:
    # constructor, called when a new instance is created
    # self refers to the instance being created
    def __init__(self, leg_count):
        # second leg_count refers to the argument being passed in
        self.leg_count = leg_count
        self.likes_food = True

    # getters and setters facilitate encapsulation
    def set_leg_count(self, leg_count):
        self.leg_count = leg_count

    def get_leg_count(self):
        return self.leg_count

# constructing new animals, instantiating new animals
cat = Animal(4)
dog = Animal(4)

# ^ objects
# cat is an instance of an Animal
# cat is an Animal

print(type(cat))
print(cat)
print(cat.leg_count)

rabbits = [Animal(4), Animal(4), Animal(4)]
rabbits[1].leg_count = 3

print(rabbits[0].__dict__)

'''
A store can have multiple departments.
A department can hold multiple products.
The store has a name.
Departments have names.
Products have names and prices.
Nouns tend to be classes.
If a noun has something, that something tends to be an attribute.
Verbs tend to be methods.
'''

class Store:
    def __init__(self, name):
        self.name = name
        self.departments = []

class Department:
    def __init__(self, name):
        self.name = name
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

soccer_ball = Product('soccer ball', 42.99)
sporting_goods = Department('Sporting goods')

# sporting_goods.products.append(soccer_ball)
sporting_goods.add_product(soccer_ball)