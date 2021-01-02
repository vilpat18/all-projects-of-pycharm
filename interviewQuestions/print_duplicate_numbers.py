list1 = [10,10,20,30,10,40,40]

dup = []
dup2 = []
for i in list1:
    if i not in dup:
        dup.append(i)

print(dup)


dup1 = set(list1)
print(dup1)


