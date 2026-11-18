

# ##  Laptop Specifications
# --------------------------------------------------------------
# Create a class Laptop with constructor attributes:
#
#  brand
#  RAM
#  price
#
# Create three laptop objects and print the details of each laptop.
# -------------------------------------------------------------------
class Laptop:

    def __init__(self,brand,ram,price):
        self.brand = brand
        self.ram = ram
        self.price = price

l1 = Laptop("HP",512,65000)
print(l1.brand)
print(l1.ram)
print(l1.price)
print("="*25)
l2 = Laptop("MAC",512,100000)
print(l2.brand)
print(l2.ram)
print(l2.price)
print("="*25)
l3 = Laptop("Torque",512,120000)
print(l3.brand)
print(l3.ram)
print(l3.price)