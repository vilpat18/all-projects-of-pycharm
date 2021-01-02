num = 7

if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print(num,'number is not a prime number')
            break

    else:
        print(num,'number is a prime number')

else:
    print(num,'number is a not prime number')