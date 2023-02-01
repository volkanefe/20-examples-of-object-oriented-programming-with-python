# Base class definition
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Derived class definition
class Dog(Animal):
    def make_sound(self):
        print("Woof woof")

# Object creation
dog = Dog()

# Method overriding behavior
dog.make_sound() # Output : Woof woof