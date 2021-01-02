list1=[12,14,17,15,16,18,19,12,21,23,14]
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


lst=list(map(int,input().split()))
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)