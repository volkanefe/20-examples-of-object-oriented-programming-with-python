# Base class definition

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this abstract method")

# Derived class definitions
class Dog(Animal):
    def make_sound(self):
        print("Woof woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow meow")

# Polymorphic list of objects
animals = [Dog("Max"), Cat("Tom")]

# Polymorphic behavior
for animal in animals:
    animal.make_sound()

# Output:
# Woof woof
# Meow meow