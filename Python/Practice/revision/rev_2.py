from ctypes import create_unicode_buffer
from traceback import print_tb


# Write a program to count the number of vowels, consonants, digits,
# and special characters in a string.
# ----------------------------------------------------------------------
# def count(s):
#     vow = 0
#     cons = 0
#     dig = 0
#     spec = 0
#     for ch in s:
#         if ch.isalpha():
#             if ch in "aeiouAEIOU":
#                 vow += 1
#             else:
#                 cons += 1
#         elif ch.isdigit():
#             dig += 1
#         else:
#             spec += 1
#     print("Vowels:",vow)
#     print("Consonants:",cons)
#     print("Digit:",dig)
#     print("Special ch:",spec)
# count("Hello@123")


# Write a program to reverse a string without using slicing.
# ------------------------------------------------------------
# def reverse(s):
#     rev = " "
#     for ch in s:
#         rev = ch + rev
#     return rev
# print(reverse("python"))


# Write a program to find the frequency of each character in a string.
# ----------------------------------------------------------------------
# def freq(s):
#     dict = {}
#     for ch in s:
#         if ch in dict:
#             dict[ch] += 1
#         else:
#             dict[ch] = 1
#     return dict
# print(freq("programming"))

# Write a program to extract only the digits from a string.
# ------------------------------------------------------------
# def extract(s):
#     digits = " "
#     for ch in s:
#         if ch.isdigit():
#             digits += ch
#     return digits
# print(extract("Py3864@3th0n"))

# Write a program to find the sum
# and average of all digits present in a string
# -----------------------------------------------
# def tot(s):
#     sum = 0
#     count = 0
#     for ch in s:
#         if ch.isdigit():
#             sum += int(ch)
#             count += 1
#     if count > 0:
#         avg = sum / count
#     else:
#         avg = 0
#     print("Sum:",sum)
#     print("Average:",avg)
# tot("ab12cd34")

# Write a program to count the number of words in a sentence.
# -------------------------------------------------------------
# def count_w(s):
#     word = len(s.split())
#     return word
# print(count_w("python is simple and easy"))

# # Write a program to find the largest and smallest element in a list.
# # --------------------------------------------------------------------
# lst = [34,26,78,66,90,12]
# larg = max(lst)
# smal = min(lst)
# print("Largest element:",larg)
# print("Smallest element:",smal)

# Write a program to find the second largest element in a list.
# -------------------------------------------------------------
# lst = [34,26,78,66,90,12]
# lst.sort()
# print("Sec largest:",lst[-2])

# Write a program to remove duplicate elements from a list
# while maintaining the original order.
# ------------------------------------------------------------
# list = [1,1,1,2,3,4,4,5,6,7,3,8,11,23,11,45]
# list1= []
# for i in list:
#     if i not in list1:
#         list1.append(i)
# print(list1)

# Write a program to merge two lists.
# -----------------------------------------
# lst1 = [2,3,4,5,8]
# lst2 = [5,6,9,7]
# lst1.extend(lst2)
# print("Merged list:",lst1)

#  Write a program
#  to separate even and odd numbers into two different lists.
# ------------------------------------------------------------
# lst = [1,2,3,4,5,6,7,8,9,12,33]
# even = []
# odd = []
# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even:",even)
# print("Odd:",odd)

#  Write a program to find the common elements between two lists.
# # ------------------------------------------------------------------
# lst1 = [1,2,3,4,5]
# lst2 = [3,4,5,6,7]
# common = [i for i in lst1 if i in lst2]
# print(common)

#  Write a program to count the frequency of each element in a list.
# ---------------------------------------------------------------------
# num = [2,3,4,5,3,2,1]
# freq = {}
# for i in num:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)

# Create a dictionary of student names and marks,
# then print the student with the highest mark.
# -----------------------------------------------------
# students = {
#     "Anu": 85,
#     "Rahul": 92,
#     "Neha": 78,
#     "Arun": 95,
#     "Meera": 88
# }
# high = max(students.values())
# for name in students:
#     if students[name] == high:
#         print(f"{name}:{high}")


# Write a function that takes a list as an argument and
# returns a new list containing only the unique elements
# while maintaining the original order.
# -----------------------------------------------------
# def unique(lst):
#     new_lst = []
#     for i in lst:
#         if i not in new_lst:
#             new_lst.append(i)
#     return new_lst
# print(unique([1,2,2,3,4,4,5,7,8,9,10]))


# Write a function to return the sum of all even numbers in a list.
# ---------------------------------------------------------------------
# def tot(lst):
#     return sum(i for i in lst if i % 2 == 0)
# print(tot([1,2,3,4,5,6]))

# Create a Student class
# with attributes name, age, and mark, and display the details.
# ---------------------------------------------------------------
# class Student:
#
#     def __init__(self,name,age,mark):
#         self.name = name
#         self.age = age
#         self.mark = mark
#
# s1 = Student("Anu", 22,98)
# print("Name:",s1.name)
# print("Age:",s1.age)
# print("Mark:",s1.mark)


# Create an Employee class with attributes name and salary, and
# calculate the annual salary.
# ---------------------------------------------------------------
# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def ann_salary(self):
#         annual_salary = self.salary * 12
#         print("Annual Salary:",annual_salary)
# e1 = Employee("Anusree",56000)
# e1.ann_salary()

# Create a Rectangle class to calculate the area and perimeter.
# --------------------------------------------------------------
# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate(self):
#         area = self.length * self.width
#         perimeter = 2 * (self.length + self.width)
#         print("Area =", area)
#         print("Perimeter =", perimeter)
#
# r1 = Rectangle(10, 5)
# r1.calculate()

# Create an Item class with item name, quantity, and
# price per unit, and calculate the total bill.
# -------------------------------------------------------
class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def bill(self):
        total = self.quantity * self.price
        print("Item Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price per Unit:", self.price)
        print("Total Bill:", total)

i1 = Item("Pen", 10, 15)
i1.bill()