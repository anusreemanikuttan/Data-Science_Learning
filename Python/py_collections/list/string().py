


# Find the average of all numeric digits in a string.
# eg: "15abc42" ---> total ----> 12, avg = 12/4

# s = input("Enter a string: ")
# count = 0
# total = 0
# for i in s:
#     if i.isdigit():
#         total += int(i)
#         count += 1
# print("Total:",total)
# print("Count:", count)
# print("Average:",total/count)


# when reading a text:
# if it is digit 123 , read only digit
# abc123 ---> alph and num
# abc ---> only alph
# abc@123 ---> it has spaces or spcl characters

text = input("Enter a text: ")
if text.isalpha():
    print("Alphabets")
elif text.isdigit():
    print("Numbers")
elif text.isalnum():
    print("Aplhabets and Numbers")
else:
    print("Has spaces or special characters")