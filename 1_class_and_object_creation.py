# Class definition

class Dog:
    # Class attribute
    species = "Canis familiars"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Object creation
dog1 = Dog("Max", 5)
dog2 = Dog("Rocky", 3)

#Accessing object attributes
print(dog1.name) # Output : Max
print(dog2.age) # Output : 3
