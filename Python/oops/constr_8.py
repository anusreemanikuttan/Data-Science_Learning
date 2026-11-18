

# ##  Circle Area
# --------------------------------------------------------------
# Create a class Circle.
# The constructor should take radius as input.
# Add a method to calculate the area using:
#
# Area = 3.14 × radius × radius
# --------------------------------------------------------------
class Circle:

    def __init__(self,r):
        self.r = r
    def area(self):
        area = 3.14 * self.r **2
        return area
c = Circle(6)
print("Area =",c.area())