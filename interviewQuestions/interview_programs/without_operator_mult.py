def multiply(a,b):
    if b < 0:
        return -multiply(a,-b)
    elif b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a+multiply(a,b-1)


print(multiply(10,20))


str1 = 'vilas'
print(str1[::-1])
print(str1[::-2])
print(str1[::-3])
