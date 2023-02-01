# Class definition with class methods and static methods
class Circle:
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    @staticmethod
    def circumference_ratio():
        return 2 * Circle.pi
    
    @property
    def diameter(self):
        return 2 * self.radius
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return Circle.pi * self.radius * self.radius

# Object creation and usage with class method
circle = Circle.from_diameter(10)
print(circle.radius) # Output: 5.0

# Static method usage
print(Circle.circumference_ratio()) # Output: 6.28

# Object property usage
circle.diameter = 20
print(circle.radius) # Output: 10.0
print(circle.area) # Output:314.0
