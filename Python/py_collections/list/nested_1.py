

# 7 sublist
# id, name, age, profession, loc

list = [[101, "Anu", 22, "DS", "PTA", 20000],
        [102, "Meera", 23, "Python", "PLKD", 25000],
        [103, "Abhi", 20, "Analyst", "PDLM", 30000],
        [104, "Maya", 28, "QA", "NRD", 35000],
        [105, "Chinju", 29, "Java", "SRD", 40000],
        [106, "Manu", 43, "MD", "BNGLR", 40000],
        [107, "Arun",35, "Testing","TVM", 45000]]

# for i in list:
#     print(i)

# print whose age > 25 -- full details
# for i in list:
#     age = i[2]    # index i , list[2] gives full line of index 2
#     if age > 25:
#         print(i)

#  age = 28
# fname, age , profession should return

# for i in list:
#     if i[2] == 28:
#         print(i[1:4])   # slicing applied, returns index 1 to 4

# profession --> python
# return --> fname and age

# for i in list:
#     if i[3] == "Python":
#         print(i[1:3])

# age > 25 and profession - java
# return name , prof, salary
#
# for i in list:
#     if i[3] == "Java":
#         print(i[1::2])  # i[1:6:2]

# find the total salary from the given data

sum = 0
for i in list:
    sum += i[5]
print(sum)

