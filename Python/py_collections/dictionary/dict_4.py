

sen = "cat rat cat hat rat"

# print like word and word count

words = sen.split()
dict = {}
for i in words:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)