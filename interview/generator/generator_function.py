def numbers():
    yield 1
    yield 2
    yield 3


for num in numbers():
    print(num)

print('creating generator object')
# Creating object and next function

def simple_generator():
    yield 1
    yield 2
    yield 3


g = simple_generator()

print(g.__next__())
print(g.__next__())