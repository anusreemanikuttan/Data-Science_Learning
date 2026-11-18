from tkinter.messagebox import RETRY


# Pefect square in the given range

def perfect_sq(start,end):
    for num in range(start,end+1):
        for i in range(1,num+1):
            if i * i == num:
                print(num,end=" ")
perfect_sq(1,100)