

# Create a class name Student
# Collect their id, name, age, loc, college name = AEC
# Create 5 subjects ----> 5 student details
# ========================================================
# class Student:

#     def details(self, id, name, age, loc, coll_name="AEC"):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.loc = loc
#         self.coll_name = coll_name
#
#     def display_details(self):
#         print("ID:",self.id)
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Location:",self.loc)
#         print("College Name:",self.coll_name)
#
# s1 = Student()
# s1.details(12,"Anusree",22,"Pdlm")
# s1.display_details()
# print("-"* 20)
# s2 = Student()
# s2.details(2,"Abhimanyu",22,"Klnd")
# s2.display_details()
# print("-"* 20)
# s3 = Student()
# s3.details(2,"Jithu",13,"Mdyk")
# s3.display_details()
# print("-"* 20)
# s4 = Student()
# s4.details(34,"Soe",26,"Ny")
# s4.display_details()
# print("-"* 20)
# s5 = Student()
# s5.details(28,"Joe",30,"US")
# s5.display_details()


# college name is constant , so it can be a static variable,
# then no need to add as instant variable
# ===========================================================
class Student:
    coll_name = ("AEC")
    def details(self, id, name, age, loc):
        self.id = id
        self.name = name
        self.age = age
        self.loc = loc

    def display_details(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Location:",self.loc)
        print("College Name:",Student.coll_name)

s1 = Student()
s1.details(12,"Anusree",22,"Pdlm")
s1.display_details()
print("-"* 20)
s2 = Student()
s2.details(2,"Abhimanyu",22,"Klnd")
s2.display_details()
print("-"* 20)
s3 = Student()
s3.details(2,"Jithu",13,"Mdyk")
s3.display_details()
print("-"* 20)
s4 = Student()
s4.details(34,"Soe",26,"Ny")
s4.display_details()
print("-"* 20)
s5 = Student()
s5.details(28,"Joe",30,"US")
s5.display_details()
