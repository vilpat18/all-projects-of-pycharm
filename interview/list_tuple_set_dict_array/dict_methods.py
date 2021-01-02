old_dict = {'name':'vilas','l_name':'patil','phone':8669037262,'address':'pune'}

print(old_dict.keys())

print(old_dict.get('name'))
print(old_dict.get('phone'))

keys = {'a','b','c'}
value='ajays'
new_dict = dict.fromkeys(keys,value)
print(new_dict)

for key , value in dict.items(old_dict):
    print(key,value)

for i in enumerate(old_dict):
    print(i)

r = old_dict.keys()
print(r)

old_dict.popitem()
print(old_dict)

set_default = old_dict.setdefault('address','pune')
print(old_dict)