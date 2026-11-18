

# ## Car Details
# -------------------------------------------------------------
# Create a class Car with constructor values:
#
#  company
#  model
#  mileage
#
# Add a method to display all car details clearly.
# -------------------------------------------------------------
class Car:

    def __init__(self,company,model,mileage):
        self.company = company
        self.model = model
        self.mileage = mileage
    def display(self):
        print("Company:",self.company)
        print("Model:",self.model)
        print("Mileage:",self.mileage)

c = Car("General Motors","Cadillac Escalade","14 kmpl")
c.display()