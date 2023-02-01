# Component class definition
class Engine:
    def start(self):
        print("Engine started")

# Composite class definition
class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        print("Car started")
        self.engine.start()

# Object creation
car = Car()

# Composition behavior
car.start()
# Output:
# Car started
# Engine started
