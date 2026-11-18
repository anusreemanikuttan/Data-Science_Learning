

# CONSTRUCTOR
# ========================================================================
# It is a special method
# represented by --> __init__()
# using constructor we can pass values whenever we create objects
# runs automatically when an object is created
# only one constructor can be passed in one class
# but more than one method can be passed into one class
# ----------------------------------------------------------------------
# normally without constructor -->

# class Person:
#
#     def setname(self,name):
#         self.name = name
#
#     def printb(self):
#         print(self.name)
#
# p1 = Person()
# p1.setname("Anu")
# p1.printb()

# using constructor --->

# class Person:
#
#     def __init__(self,name):
#         self.name = name
#
#     def printb(self):
#         print(self.name)
#
# p1 = Person("Anu")    # values can be passed within the obj
# p1.printb()


# using single method, without a method for printing --->

class Person:

    def __init__(self,name,age):
        self.age = age
        self.name = name

p1 = Person("Anu",25)
print(p1.name)          # it can print it seperately
print(p1.age)