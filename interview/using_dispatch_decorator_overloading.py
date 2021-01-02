from multipledispatch import dispatch

@dispatch(int,int)
def product(a,b):
    result = a*b
    print(result)

@dispatch(int,int,int)
def product(a,b,c):
    result = a*b*c
    print(result)

product(10,10)
product(10,10,10)