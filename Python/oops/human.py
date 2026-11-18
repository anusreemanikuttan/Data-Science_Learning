

# class Human:
#
#     def speak(self):
#         print('Human can speak')
#
#     def run(self):
#         print('Human can run')
#
#     def walk(self):
#         print("Human can walk")
#
#     def hear(self):
#         print("Human can hear")
#
# anu = Human()
# anu.speak()
# anu.run()
# print("*" * 25)
#
# arjun = Human()
# arjun.walk()
# arjun.hear()
# print("*" * 25)
#
# vishnu = Human()
# vishnu.speak()
# vishnu.run()
# vishnu.walk()
# vishnu.hear()


# Task 1 – Car
#
# Create a class Car with the following methods:
#
#  start() → "Car started."
#  drive() → "Car is moving."
#  stop() → "Car stopped."
#
# Requirements:
#
#  Create an object car1 and call all the methods in order.
#  Create another object car2 and call only the drive() method.
# =================================================================

# class Car:
#
#     def start(self):
#         print("Car started.")
#     def drive(self):
#         print("Car is moving.")
#     def stop(self):
#         print("Car stopped.")
#
# car1 = Car()
# car1.start()
# car1.drive()
# car1.stop()
# print("*"*25)
#
# car2 = Car()
# car2.drive()



# Task 2 – Mobile Phone
#
# Create a class Mobile with the following methods:
#
#  call() → "Calling someone..."
#  message() → "Sending a message."
#  camera() → "Taking a photo."
#
# Requirements:
#
#  Create an object phone1 and call all three methods.
#  Create another object phone2 and call only camera().
# ==============================================================
#
# class Mobile:
#
#     def call(self):
#         print("Calling someone...")
#     def message(self):
#         print("Sending a message.")
#     def camera(self):
#         print("Taking a photo.")
#
# phone1 = Mobile()
# phone1.call()
# phone1.message()
# phone1.camera()
# print("*"*25)
# phone2 = Mobile()
# phone2.camera()


# Task 3 – Animal
#
# Create a class Animal with the following methods:
#
#  eat() → "Animal is eating."
#  sleep() → "Animal is sleeping."
#  make_sound() → "Animal is making a sound."
#
# Requirements:
#
#  Create an object dog and call all methods.
#  Create another object cat and call only eat() and make_sound().
# ===================================================================
#
# class Animal:
#
#     def eat(self):
#         print("Animal is eating.")
#     def sleep(self):
#         print("Animal is sleeping.")
#     def make_sound(self):
#         print("Animal is making a sound.")
#
# dog = Animal()
# dog.eat()
# dog.sleep()
# dog.make_sound()
# print('*'*25)
# cat = Animal()
# cat.eat()
# cat.make_sound()



# Task 4 – Teacher
#
# Create a class Teacher with the following methods:
#
#  teach() → "Teaching the class."
#  check_homework() → "Checking homework."
#  conduct_exam() → "Conducting an exam."
#
# Requirements:
#
#  Create an object teacher1 and call teach() and conduct_exam().
#  Create another object teacher2 and call all three methods.
# ===================================================================
#
# class Teacher():
#
#     def teach(self):
#         print("Teaching the class.")
#     def check_homework(self):
#         print("Checking homework.")
#     def conduct_exam(self):
#         print("Conducting an exam.")
#
# teacher1 = Teacher()
# teacher1.teach()
# teacher1.conduct_exam()
# print("*"*25)
#
# teacher2 = Teacher()
# teacher2.teach()
# teacher2.check_homework()
# teacher2.conduct_exam()


# Task 5 – Robot
#
# Create a class Robot with the following methods:
#
#  greet() → "Hello, human!"
#  dance() → "Robot is dancing."
#  sing() → "Robot is singing."
#
# Requirements:
#
#  Create an object robot1 and call all methods.
# * Create another object robot2 and call only greet() and sing().
# ===================================================================

class Robot:

    def greet(self):
        print("Hello, human!")
    def dance(self):
        print("Robot is dancing.")
    def sing(self):
        print("Robot is singing.")

robo1 = Robot()
robo1.greet()
robo1.dance()
robo1.sing()
print("*"*25)

robo2 = Robot()
robo2.greet()
robo2.sing()