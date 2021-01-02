def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multi(x,y):
    return x*y
def devidation(x,y):
    return x/y

print('Select operation')
print("1. addition")
print("2. substraction")
print("3. multi")
print("4. devide")

while True:
    choice = input("enter choice 1/2/3/4: ")
    if choice in ('1','2','3','4'):
        num1 = float(input('enter the first number: '))
        num2 = float(input('enter the second number: '))

        if choice == '1' :
            print(num1,'+',num2, '=',addition(num1,num2) )
        elif choice == '2':
            print(num1,'-',num2, '=',subtraction(num1,num2))
        elif choice == '3':
            print(num1,'*',num2, '=',multi(num1,num2))
        elif choice == '4':
            print(num1,'/',num2, '=',devidation(num1,num2))
        break
    else:
       print('pls choose correct option')