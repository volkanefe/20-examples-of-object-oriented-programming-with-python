class Rectangle:
    def area(self, width=None, height=None):
        if width and height:
            return width * height
        elif width:
            return width * width
        elif height:
            return height * height
        else:
            raise ValueError("Either width or height must be provided")

# Overloaded method usage
rect = Rectangle()
print(rect.area(5, 10)) # Output: 50
print(rect.area(5)) # Output: 25
print(rect.area(height=10)) # Output: 100
