

# OOPS -----> Object Oriented Programming
# ==================================================

# class --- blueprint / base model of object
# object --- instance of class
# reference --- mode of operation

# class --> car
# object --> maruti, maheendra, kia
# reference --> drive, start, stop


# class A:
#         def name():     {methods}

# obj1 = A()

class A:

    def printa(self):
        print('writing')

    def printb(self):
        print('reading')

    def printc(self):
        print('walking')

obj1 = A()
obj1.printa()
print("*" * 25)

obj2 = A()
obj2.printb()
obj2.printc()
print("*" * 25)

obj3 = A()
obj3.printa()
obj3.printb()
obj3.printc()

