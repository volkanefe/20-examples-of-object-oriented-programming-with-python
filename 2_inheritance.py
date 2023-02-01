
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Some generic animal sound")

# Derived class definition
class Dog(Animal):
    def make_sound(self):
        print("Woof woof")

# Object creation
dog = Dog("Max")

# Polymorphic behavior
dog.make_sound() # Output : Woof woof