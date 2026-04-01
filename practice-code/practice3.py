#Create a class Student with a display() method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

name = input("Enter name: ")
age = input("Enter age: ")
s = Student(name, age)
s.display()
