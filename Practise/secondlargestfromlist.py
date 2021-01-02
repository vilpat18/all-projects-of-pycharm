#find second largest number
'''lst1=[45,41,25,47,45,87,54,45,74,84,87]
lst1.remove(max(lst1))
print("the second largest element in a list",max(lst1))'''
max1=[]
n=int(input("enter no of element: "))
for ele in range(1,n+1):
    b=int(input("enter elements: "))
    if b not in max1:

        max1.append(b)

max1.sort()
print(max1)
print("the second largest num in list is",max1[-2])
























