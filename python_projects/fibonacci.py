num = int(input('How many term: '))
a = 0
b = 1
count = 0

if num <= 0:
    print('pls enter valid number')
elif num == 1:
    print("the enterd number is fibonacci number",b)
else:
    # print('fibonacci sequence')
    while count < num:
        num1 = a + b
        a = b
        b = num1
        count +=1
        print(count)
