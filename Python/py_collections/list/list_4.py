

# wap to find the sum of odd numbers in the range of 1 to 20
list = []
for i in range(1,21):
    if i % 2 != 0:
        list.append(i)
print(list)
print(sum(list))