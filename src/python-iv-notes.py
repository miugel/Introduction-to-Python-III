# inheritance and association
# class composition and class aggregation
# has a relationship, inheritance
# is a relationship

# inheritance
# pass parent class into child class, is a relationship

# class Animal:
#     def __init__(self, leg_count=4):
#         self.leg_count = leg_count

#     def make_sound(self):
#         print('REEEEE')

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     def __init__(self, tail_length):
#         super().__init__()
#         self.tail_length = tail_length

# dog = Dog()
# cat = Cat(8)

# print(dog.__dict__)
# print(cat.__dict__)
# dog.make_sound()
# cat.make_sound()

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

class SoccerBall(Product):
    def __init__(self, size):
        super().__init__('Soccer ball', 20)
        self.size = size