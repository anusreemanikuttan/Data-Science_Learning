

# ## Employee Experience
# ------------------------------------------------------------
# Create a class EmployeeExperience with constructor values:
#
#  employee name
#  joining year
#  current year
#
# Add a method to calculate the number of years of experience.
# -------------------------------------------------------------
class EmployeeExperience:

    def __init__(self,name,join_yr,curr_yr):
        self.name = name
        self.join_yr = join_yr
        self.curr_yr = curr_yr
    def exp(self):
        exp = self.curr_yr - self.join_yr
        return exp

e = EmployeeExperience("Anusree",2003,2026)
print("Number of years of experience:",e.exp())
