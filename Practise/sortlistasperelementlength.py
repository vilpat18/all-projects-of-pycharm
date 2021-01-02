a=[]
l=int(input("enter the no. of element: "))
for i in range(1,l+1):
    b=input("enter the element: ")
    a.append(b)
a.sort(key=len)
print("the list sorted by length: ",a)







