old_set = {10,44,55,88,77,99}
old_set1 = {22,44,55,88,77,99}
print(old_set)

old_dict = {'name':'vilas','l_name':'patil'}

print('--------------------------------------------------------------')

frozen_set = frozenset(old_dict)
print('dict of frozenset is:>>',frozen_set)

old_set.add(100)
print(old_set)

new_set_copy=old_set.copy()
print(id(old_set))
print(id(new_set_copy))

set_diff = old_set.difference(old_set1)
print(set_diff)

set_dif_update = old_set.difference_update(old_set1)
print(set_dif_update)

print('-------------------------------')

old_set.discard(10)
print(old_set)

old_set8 = {10,44,55,88,77,99}
old_set9 = {22,44,55,88,77,99}

int_set=old_set8.intersection(old_set9)
print(int_set)

old_set10 = {44,55,88,77,99}
old_set11 = {44,55,88,77,99}

print(old_set10.issubset(old_set11))











