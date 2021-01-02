import random

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = int(input('number of password:- '))
length = int(input('length of password:- '))


for i in range(number):
    password = ''

    for j in range(length):
        password += random.choice(char)

    print(password)
