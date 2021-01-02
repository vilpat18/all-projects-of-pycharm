import re

NameAge = """ Mahesh is 22 Sachin is 25
              Akshay is 27 Ajay is 24 """


ages = re.findall(r'\d{1,3}',NameAge)
names = re.findall(r'[A-Z][a-z]*',NameAge)

d = {}
x = 0
for i in names:
    d[i] = ages[x]
    x +=1

print(d)
