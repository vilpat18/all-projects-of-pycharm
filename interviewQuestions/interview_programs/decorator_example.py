
# Calculate execution time using decorator

import functools
import time

def timer(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('finished in {} sec'.format(run_time))
        return value
    return wrapper

@timer
def doubled_and_add(num):
    res = sum([i**2 for i in range(num)])
    print(res)


doubled_and_add(100)
doubled_and_add(100000)
