
def Fibo(limit):
    a , b = 0 , 1

    while a<limit:
        yield a
        a,b = b,a+b

print('using generator object')
x = Fibo(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print('----------------------------------------')
print('using for loop')
for f in Fibo(10):
    print(f)