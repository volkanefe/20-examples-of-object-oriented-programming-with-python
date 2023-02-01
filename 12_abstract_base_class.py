# Abstract base class definition
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class definitions
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Object creation and usage
square = Square(5)
circle = Circle(3)

print(square.area()) # Output: 25
print(circle.area()) # Output: 28.26
