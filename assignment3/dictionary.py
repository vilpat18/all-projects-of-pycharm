l=['a','b','c']
s=[1,2,3]
d={k:v for (k,v) in zip(l,s) }
print(d)

m = [1,2,3,4,5,6]
di = {i:i**2 for i in range(1,len(m))}
print(di)

d2 ={"a":1,"b":2,"c":3}
for k,v in d.items():
    print(k,v)

str = "aabbcc"
d4={}
for i in str.split():
    for j in i:
        d4[j]=i

print(d4)



