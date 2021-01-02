num = int(input('enter the number: '))

a = 0
b = 1

if num < 0:
    print('pls enter valid ,positive integer')
elif num == 1:
    print(b)
else:
    for i in range(2,num):
        c = a + b
        a = b
        b = c
print(b)

