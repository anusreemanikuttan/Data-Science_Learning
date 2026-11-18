

# the total marks of students out of 500
# ask the user for 5 subjects(100)
# calc the total mark
# find the total percentage
# print the percentage

# if percentage

# 80 and above ---> Grade A
# 70 and below 80 --> Grade B
# 60 and below 70 ---> Grade C
# 50 and below 60 ---> Grade D
# below 50 ---> Fail

m1 = int(input("Enter mark of Physics: "))
m2 = int(input("Enter mark of Maths: "))
m3 = int(input("Enter mark of Chemistry: "))
m4 = int(input("Enter mark of Malayalam: "))
m5 = int(input("Enter mark of French: "))
sum = m1+m2+m3+m4+m5
print("Total Mark:",sum)
per = sum/500*100
print("Total Percentage:",per)
if per >= 80:
    print("Grade A")
elif per >= 70:
    print("Grade B")
elif per >= 60:
    print("Grade C")
elif per >= 50:
    print("Grade D")
else:
    print("Failed")