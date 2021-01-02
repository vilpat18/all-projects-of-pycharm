a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(i)
c=list(map(int,input().split()))
d=[]
for j in c:
    d.append(j)

new=b+d
new.sort()
print("the merge list" ,new)


