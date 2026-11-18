

# Static Variable Task
# ===========================================================
# Create a class name Employee
# Details --> id, fname, lname, age, prof, loc, company_name = same company
# 5 objects
# ---------------------------------------------------------------------------
class Employee:
    comp_name = "Laennac AI"

    def details(self,id,fname,lname,age,prof,loc):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.prof = prof
        self.loc = loc

    def display_details(self):
        print("ID:",self.id)
        print("Name:",self.fname,self.lname)
        print("Age:",self.age)
        print("Profession:",self.prof)
        print("Location:",self.loc)
        print("Company Name:",Employee.comp_name)

e1 = Employee()
e1.details(101,"Anusree","Manikuttan",23,"AI Engineer","Germany")
e1.display_details()
print("*"*20)
e2 = Employee()
e2.details(102,"Abhimanyu","A",23,"AI Architect","Sweden")
e2.display_details()
print("*"*20)
e3 = Employee()
e3.details(103,"John","Brown",30,"Ml Engineer","New Jersey")
e3.display_details()
print("*"*20)
e4 = Employee()
e4.details(104,"Soe","Wick",33,"R&D","Madrid")
e4.display_details()
print("*"*20)
e5 = Employee()
e5.details(105,"Jeon","Jk",29,"Associate","Brussels")
e5.display_details()
