l1 = ['a','b','c','d']
l2 = [50,60,70,80]
print("Using for loop:-")
d = {}
for key in l1:
    for value in l2:
        d[key]=value
        l2.remove(value)
        break

print(str(d))

l3 = ['a','b','c','d']
l4 = [50,60,70,80]
print("Using zip function:-")
d1 = dict(zip(l3,l4))
print(str(d1))


l5 = ['a','b','c','d']
l6 = [50,60,70,80]
print("Using dictionary comprehension:- ")
dict3 = {l5[key]:l6[key] for key in range(len(l5))}
print(dict3)

