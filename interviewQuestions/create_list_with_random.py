import random

list_rand = [random.randrange(1,50,2) for i in range(10)]
print(str(list_rand))


for i in range(10):
    print(random.randrange(10,50,2),end=',')