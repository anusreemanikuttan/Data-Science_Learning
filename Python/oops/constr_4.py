

# ##  Employee Salary Increment
# -----------------------------------------------------------------
# Create a class Employee with:
#
#  name
#  salary
#
# Initialize them using a constructor.
# Add a method to increase the salary by 10% and show the new salary.
# ----------------------------------------------------------------------
class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def inc(self):
        self.salary += self.salary * 10/100
        return self.salary

e1 = Employee("Anusree", 50000)
print("New Salary:",e1.inc())
