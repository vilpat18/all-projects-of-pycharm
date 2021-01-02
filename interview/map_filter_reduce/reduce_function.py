from functools import reduce
def addition(a,b):
    return a+b


my_list = [11,11,11,11,11]
result = reduce(addition,my_list)
print(result)


use_lambda = reduce(lambda x,y:x+y,my_list)
print(use_lambda)