

# ## Product Discount
# --------------------------------------------------------------
# Create a class Product with constructor parameters:
#
#  name
#  price
#
# Add a method to apply 5% discount and show the new price.
# ----------------------------------------------------------------
class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price
    def discount(self):
        self.price -= self.price * 5/100
        return self.price

p1 = Product("Cosmetics",2650)
print("New Price:",p1.discount())
