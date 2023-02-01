'''
In this example, the greet function is a decorator that adds a "Hello, World!" 
greeting to a function. The greet function returns a wrapper function 
that prints the greeting and then calls the original function. 
The @greet decorator is used to apply the greet decorator to the say_hello function. 
When the say_hello function is called, the greeting is printed before 
the original function is executed. This allows you to add behavior to a function, 
without modifying its implementation. 
Decorators are a powerful tool for writing reusable and modular code.

'''

# Decorator example
def greet(func):
    def wrapper(*args, **kwargs):
        print("Hello, World!")
        return func(*args, **kwargs)
    return wrapper

@greet
def say_hello():
    print("Hello!")

# Use decorator
say_hello()
# Output:
# Hello, World!
# Hello!
