

# to call a variale in different method ,
# we use instance variable with instance keywrod - "self"
# -------------------------------------------------------------------------------------------------
# class Person:
#     def setvalue(self,name):   # name is local variable
#         self.name = name
#
#     def display_name(self):
#         print(self.name)
#
# s = Person()
# s.setvalue("Anju")
# s.display_name()


# Create a class person and collect the details of 5 persons -->
# fname, lname, age
# ----------------------------------------------------
class Person:

    def setvalue(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def display_details(self):
        print("Fname:",self.fname)
        print("Lname:",self.lname)
        print("Age:",self.age)

p1 = Person()
p1.setvalue("Anusree","Manikuttan", 23)
p1.display_details()
print("-"* 20)
p2 = Person()
p2.setvalue("Abhinav","M",14)
p2.display_details()
print("-"* 20)
p3 = Person()
p3.setvalue("Maya","Manikuttan",48)
p3.display_details()
print("-"* 20)
p4 = Person()
p4.setvalue("Manikuttan","V",56)
p4.display_details()
print("-"* 20)
p5 = Person()
p5.setvalue("Abhimanyu","A","23")
p5.display_details()