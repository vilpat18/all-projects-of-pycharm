import functools
import time

def timer(func):
    @functools.wraps(func)
    def inner_func(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        real_time = end_time-start_time
        print('finished time in {} seconds'.format(real_time))
        return value
    return inner_func


@timer
def my_function(*args,**kwargs):
    res = sum([i**2 for i in range(*args)])
    print('sum of numbers and doubled:- ',res)
    for k,v in kwargs.items():
        print(k,v)


my_function(10,a=10,b=100,c=1000)
my_function(10000,a=10,b=100,c=1000)

