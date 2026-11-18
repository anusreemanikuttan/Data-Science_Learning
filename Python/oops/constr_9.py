

# ##  Student Marks & Percentage
# -------------------------------------------------------------
# Create a class StudentMarks whose constructor accepts:
#
#  mark1
#  mark2
#  mark3
#
# Add a method to calculate the percentage using:
#
# Percentage = (total / 300) × 100
# --------------------------------------------------------------
class Mark:

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def per(self):
        total = self.m1 + self.m2 + self.m3
        per = (total / 300) * 100
        return per

s1 = Mark(80,75,98)
print("Percentage =",s1.per())