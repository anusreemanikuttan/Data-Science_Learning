

# ## Bike Mileage Checker
# ----------------------------------------------------
# Create a class Bike with constructor values:
#
#  brand
#  model
#  mileage
#
# Add a method to check:
#
#  If mileage > 40, print “Good mileage”
#  Otherwise, print “Average mileage”
# ------------------------------------------------------
class Bike:

    def __init__(self,brand,model,mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage
    def check(self):
        if self.mileage > 40:
            return "Good Mileage"
        else:
            return "Average Mileage"
b1 = Bike("Hero","Splendor",75)
print(b1.check())
b2 = Bike("Honda", "Activa",35)
print(b2.check())