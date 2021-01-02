str1 = str(input('enter comma seperate values: '))

lst = str1.split(',')

print(lst)

lst1 =[]
for i in lst:
    lst1.append(int(i))

print(lst1)
