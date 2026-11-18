

# Student Information
# ---------------------------------------------------------------
# Create a class Student with a constructor that takes:
#   student name
#   age
# Create an object and print the name and age using the object
# ----------------------------------------------------------------
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Anu", 22)
print(s1.name)
print(s1.age)