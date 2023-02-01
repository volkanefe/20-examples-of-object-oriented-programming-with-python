# Base class definitions
class Person:
    def person_info(self, name, age):
        self.name = name
        self.age = age
        print(f"Name: {self.name}, Age: {self.age}")
    
class Student:
    def student_info(self, roll_no, course):
        self.roll_no = roll_no
        self.course = course
        print(f"Roll No: {self.roll_no}, Course: {self.course}")
    

# Derived class definition
class Scholar(Person, Student):
    pass

# Object creation
scholar = Scholar()

# Multiple inheritance behavior
scholar.person_info("John Doe",25)
scholar.student_info("CS101","Computer Science")
# Output:
# Name: John Doe, Age: 25
# Roll No: CS101, Course: Computer Science
