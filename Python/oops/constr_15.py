

# ## Shopping Bill
# ------------------------------------------------
# Create a class Item with constructor inputs:
#
#  item name
#  quantity
#  price per unit
#
# Add a method to calculate:
#
# Total bill = quantity × price per unit
# ------------------------------------------------
class Item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def calc(self):
        total = self.quantity * self.price
        return total

i1 = Item("Sprite",50,5000)
print("Total Bill:",i1.calc())