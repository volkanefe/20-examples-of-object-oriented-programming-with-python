# Base class definitions
class A:
    def display(self):
        print("Class A display method")

class B(A):
    def display(self):
        print("Class B display method")

class C(A):
    def display(self):
        print("Class C display method")

# Multiple inheritance class definition
class D(B, C):
    pass

# Object creation
d = D()

# Method Resolution Order behavior
d.display() # Output: Class B display method
