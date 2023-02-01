# Class definition with property decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")
    
    @property
    def area(self):
        return 3.14 * self._radius * self._radius

# Object creation and usage
circle = Circle(5)
print(circle.radius) # Output: 5
circle.radius = 3
print(circle.area) # Output: 28.26
