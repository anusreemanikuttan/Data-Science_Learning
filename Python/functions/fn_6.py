# 1. Create a greeter function greet(name, language).
#
# If the language is "English" → Print: Hello, {name}!
# If the language is "Malayalam" → Print: Namaskaram, {name}!
# If the language is "Arabic" → Print: Marhaba, {name}!
# Otherwise → Print: Language not supported
# --------
# Method 2----->
# def greet(name, language):
#     if language == "English":
#         print("Hello,", name, "!")
#     elif language == "Malayalam":
#         print("Namaskaram,", name, "!")
#     elif language == "Arabic":
#         print("Marhaba,", name, "!")
#     else:
#         print("Language not supported!!")
# greet("Anu", "Malayalam")
# greet("Anu", "French")


# Method 3----->
# def greet(name, language):
#     if language == "English":
#         return f"Hello, {name}!"
#     elif language == "Malayalam":
#         return f"Namaskaram, {name}!"
#     elif language == "Arabic":
#         return f"Marhaba, {name} !"
#     else:
#         return "Language not supported!!"
# print(greet("Anu", "Arabic"))
# print(greet("Anu", "Dutch"))

#
# 2.Weather Reporter
#
# Define weatherreport(temp)
# If temp > 30 → print("It's a hot day! Stay hydrated.")
# If 20 <= temp <= 30 → print("Nice and warm outside!")
# If temp < 20 → print("It's a bit chilly today!")
# --------
#
# Method 2---->
# def weather_rep(temp):
#     if temp > 30:
#         print("It is a hot day! Stay hydrated.")
#     elif 20 <= temp <= 30:
#         print("Nice and warm outside!")
#     elif temp < 20:
#         print("It's a bit chilly today!")
# weather_rep(18)
# weather_rep(38)
# weather_rep(25)
#
#
# Method 3---->
# def weather_rep(temp):
#     if temp > 30:
#         return "It is a hot day! Stay hydrated."
#     elif 20 <= temp <= 30:
#         return "Nice and warm outside!"
#     elif temp < 20:
#         return "It's a bit chilly today!"
# print(weather_rep(38))
# print(weather_rep(23))
# print(weather_rep(7))
#

#
# 3.Grade Evaluator
#
# Define grade(mark)
# 90-100 → "A"
# 75-89 → "B"
# 50-74 → "C"
# Below 50 → "Fail"
# Print--> "Your grade is {grade}"
# --------
# Method 2---->
# def grade(mark):
#     if 90 <= mark <= 100:
#         print("Your grade is A")
#     elif 75 <= mark <= 89:
#         print("Your grade is B")
#     elif 50 <= mark <= 74:
#         print("Your grade is C")
#     elif mark < 50:
#         print("Your grade is Fail")
# grade(98)
# grade(20)
#
# Method 3--->
# def grade(mark):
#     if 90 <= mark <= 100:
#         return "A"
#     elif 75 <= mark <= 89:
#         return "B"
#     elif 50 <= mark <= 74:
#         return "C"
#     elif mark < 50:
#         return "Fail"
# print("Your grade is", grade(98))
# print("Your grade is", grade(20))
#
#
# 4.Fruit Price Checker
#
# If the fruit is "apple" → Print: Price: 100/kg
# If the fruit is "banana" → Print: Price: 50/kg
# If the fruit is "mango" → Print: Price: 120/kg
# Otherwise → Print: Not available
# --------
#
# Method 2 --->
# def price_chk(fruit):
#     if fruit == "apple":
#         print("100/kg")
#     elif fruit == "banana":
#         print("50/kg")
#     elif fruit == "mango":
#         print("120/kg")
#     else:
#         print("Not available")
# price_chk("apple")
# price_chk("banana")
#
# Method 3
# def price_chk(fruit):
#     if fruit == "apple":
#         return "100/kg"
#     elif fruit == "banana":
#         return "50/kg"
#     elif fruit == "mango":
#         return "120/kg"
#     else:
#         return "Not available"
# print(price_chk("mango"))
# print(price_chk("banana"))
#
#
# 5.Age Category
#
# Define agegroup(age)
# age < 13 → "Child"
# 13–19 → "Teenager"
# 20–59 → "Adult"
# 60+ → "Senior Citizen"
# -------
#
# Method 2 ---->
# def age_group(age):
#     if age < 13:
#         print("Child")
#     elif 13 <= age <= 19:
#         print("Teenager")
#     elif 20 <= age <= 59:
#         print("Adult")
#     elif age >= 60:
#         print("Senior Citizen")
# age_group(8)
# age_group(16)
#
# Method 3 ---->
# def age_group(age):
#     if age < 13:
#         return "Child"
#     elif 13 <= age <= 19:
#         return "Teenager"
#     elif 20 <= age <= 59:
#         return "Adult"
#     elif age >= 60:
#         return "Senior Citizen"
# print(age_group(69))
# print(age_group(45))
#

#
# 6.Area Calculator
#
# Define area(shape,value1=0,value2=0)
# If shape == 'circle' → area   # 3.14r2----> 3.14value*2
# If shape == 'rectangle' → area # lb  -----> value1value2
# If shape == 'square' → area  # a2 -----> value1*2
# -------
#
# Method 2 --->
# def area(shape,value1=0,value2=0):
#     if shape == "Circle":
#         print("Area of Circle -", 3.14 * (value1 ** 2))
#     elif shape == "Rectangle":
#         print("Area of Rectangle -", value1 * value2)
#     elif shape == "Square":
#         print("Area of Square -", value1 ** 2)
# area("Circle", 2)
# area("Rectangle", 4, 3)
# area("Square", 6)
#
# Method 3 ---->
# def area(shape,value1=0,value2=0):
#     if shape == "Circle":
#         return f"Area of Circle - {3.14 * (value1 ** 2)}"
#     elif shape == "Rectangle":
#         return f"Area of Rectangle - {value1 * value2}"
#     elif shape == "Square":
#         return f"Area of Square - {value1 ** 2}"
# print(area("Circle", 2))
# print(area("Rectangle", 4, 3))
# print(area("Square", 6))
#
#
# 7.Password Strength Checker
#
# Create a function check_password(password).
# -->find the length of the password using the len() function.
# If the length is less than 6 → Print: "Weak"
# If the length is between 6 and 10 (inclusive) → Print: "Medium"
# If the length is greater than 10 → Print: "Strong"
# -------
#
# Method 2
# def chk_pwd(password):
#     if len(password) < 6:
#         print("Weak")
#     elif 6 <= len(password) <= 10:
#         print("Medium")
#     elif len(password) > 10:
#         print("Strong")
# chk_pwd("abc")
# chk_pwd("abcd1234345678908")
# chk_pwd("Abghi564")
#
# Method 3 ----->
# def chk_pwd(password):
#     if len(password) < 6:
#         return "Weak"
#     elif 6 <= len(password) <= 10:
#         return "Medium"
#     elif len(password) > 10:
#         return "Strong"
# print(chk_pwd("abc"))
# print(chk_pwd("abcd1234345678908"))
# print(chk_pwd("Abghi564"))
#
#
# 8.Language Translator
#
# Define translate(word, lang)
# If word == "sun" and lang == "ml" → "സൂര്യൻ"
# If word == "sun" and lang == "fr" → "Soleil"
# Else → "Translation not available"
# -------
#
# Method 2 ---->
# def transl(word, language):
#     if word == "Sun" and language == "Malayalam":
#         print("സൂര്യൻ")
#     elif word == "Sun" and language == "French":
#         print("Soleil")
#     else:
#         print("Translation not available")
# transl("Sun", "Malayalam")
# transl("Sun", "French")

# Method 3 ---->
# def transl(word, language):
#     if word == "Sun" and language == "Malayalam":
#         return "സൂര്യൻ"
#     elif word == "Sun" and language == "French":
#         return "Soleil"
#     else:
#         return "Translation not available"
# print(transl("Sun", "Malayalam"))
# print(transl("Sun", "French"))