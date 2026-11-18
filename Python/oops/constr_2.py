

# Rectangle Area
# -------------------------------------------------------
# Create a class rectangle
# The constructor should accept:
#    length
#    breadth
# Add a method to calc and return the area of the rectangle
# -----------------------------------------------------------
class Rectangle:

    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b   # can use return
r1 = Rectangle(2,6)
print(r1.area())           # print the method
