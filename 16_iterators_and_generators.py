# Iterators example
class SquareNumbers:
    def __init__(self, max_number):
        self.max_number = max_number
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number >= self.max_number:
            raise StopIteration
        result = self.current_number ** 2
        self.current_number += 1
        return result

# Use iterator
squared_numbers = SquareNumbers(5)
for num in squared_numbers:
    print(num)
# Output:
# 0
# 1
# 4
# 9
# 16

# Generators example
def fibonacci_sequence(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Use generator
for num in fibonacci_sequence(100):
    print(num)
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
