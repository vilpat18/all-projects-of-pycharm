from itertools import count

old_list = [10,44,55,77,'vilas','ajay']

old_list.append(45)
print(old_list)

c_element=old_list.count(10)
print(c_element)

old_list.extend([10,14,55])
print(old_list)

index_element =old_list.index(77)
print(index_element)

old_list.pop(5)
print(old_list)

old_list.remove('vilas')
print(old_list)

old_list.reverse()
print(old_list)

old_list.sort()
print(old_list)
