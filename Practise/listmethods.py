'''#list methods
l=[12,10,87,78,45,{"key":"val","key1":"val1"}]
l.append("vilas")
print(l)

l.extend([[12,10],10,0])
print(l)

l.insert(0,"vilas")
print(l)

l.remove("vilas")
print(l)

l1=l.pop()
print(l)

l[5].pop("key1")
print(l)

l=[12,10,10,87,78,45,{"key":"val","key1":"val1"}]
print(l.count(10))
print(l)

l.reverse()
print(l)


print(l.index(10))'''

l=[12,10,87,78,45,{"key":"val","key1":"val1"}]
del l[0]
print(l)


