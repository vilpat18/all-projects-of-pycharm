def my_func(a,*b):
    print('first argument: ',a)
    print('second arguments: ',*b)


my_func('hello','how','are','you')


def ur_func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)


ur_func(a=10,b=20,c=30)