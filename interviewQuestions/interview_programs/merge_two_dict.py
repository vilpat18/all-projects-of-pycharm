dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5,'f':6}

merge_dict = dict1.copy()
for key,values in dict2.items():
    merge_dict[key] = values

print(merge_dict)

# Using unpacking operator
print('Using unpacking operator:-')
merge_dict2 = {**dict1,**dict2}
print(merge_dict2)

print('using collection chain maps: ')
from collections import ChainMap
merge_dict3 = ChainMap(dict1,dict2)
print(merge_dict3)

print("Unpacking the second Dictionary: ")
merge_dict4 = dict(dict1,**dict2)
print(merge_dict4)
