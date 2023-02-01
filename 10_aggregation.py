# Component class definition
class Wheel:
    def __init__(self, radius):
        self.radius = radius
    
    def display(self):
        print(f"Wheel of radius {self.radius}")

# Composite class definition
class Car:
    def __init__(self, wheels):
        self.wheels = wheels
    
    def display(self):
        print("Car with wheels:")
        for wheel in self.wheels:
            wheel.display()

# Object creation
wheels = [Wheel(15), Wheel(15), Wheel(16), Wheel(16)]
car = Car(wheels)

# Aggregation behavior
car.display()
# Output:
# Car with wheels:
# Wheel of radius 15
# Wheel of radius 15
# Wheel of radius 16
# Wheel of radius 16
