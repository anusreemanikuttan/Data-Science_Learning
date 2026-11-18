

# Given number is perfect or not

def perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if sum == num:
        return "Perfect Number"
    else:
        return "Not a Perfect Number"
print(perfect(4))
print(perfect(6))