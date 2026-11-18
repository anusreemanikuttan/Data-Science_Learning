

# ##  Temperature Conversion
# ------------------------------------------------------------------------
# Create a class Temperature whose constructor receives a value in Celsius.
# Add a method to convert it into Fahrenheit using:
#
# F = (C × 9/5) + 32
# ------------------------------------------------------------------------
class Temp:

    def __init__(self,c):
        self.c = c
    def convert(self):
        f = (self.c * 9/5) + 32
        return f

t1 = Temp(45)
print("Temperature in Fahrenheit:",t1.convert())