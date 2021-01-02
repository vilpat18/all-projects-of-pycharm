import functools
l1=[1,2,4,5,75,10]
l2=['india','is','awesome','country']
#for addition
print(functools.reduce(lambda a,b:a+b,l1))
#for largest number in list
print(functools.reduce(lambda a,b: a if a>b else b,l1))

import operator
print(functools.reduce(operator.add,l1))
print(functools.reduce(operator.mul,l1))
print(functools.reduce(operator.add,l2))

#sum inbuilt function
list2=[1,5,4,7,4,5,6,2,3,4]
sum1=(sum(list2))
print(sum1)
avg=sum1/len(list2)
print(avg)

#inicode value ord()
print(ord('a'))

#cmp  comparing two list
lst=[1,2,4,5,4,8,5]
lst1=[12,45,7,8,45,45,45]
lst.remove(max(lst))
print(lst)

print("the largest element in a list",max(lst))
print(len(lst1))

#using filter
def fun(variable):
    letter=['a','e','i','o','u']
    if (variable in letter):
        return True
    else:
        return False
sequence=['i','n','d','i','a']

#using inbuilt function filter
filtered = filter(fun,sequence)
for words in filtered:
    print(words)

#filter is generally used with lambda function
#list,tuple,set

list10=[10,12,14,16,1,8,19,17,20]
print(list(filter(lambda a:a%2==0,list10)))
print(list(filter(lambda a:a%2!=0,list10)))
print(functools.reduce(lambda a,b: a if a>b else b,list10))


#we can doubled the all numbers in list by using a map
def addition(n):
    return n+n

numbers=(1,2,3,4,5)
sum1=map(addition,numbers)
print(list(sum1))

#we can make element value doubles by using lambda function with map
re=map(lambda a:a+a,list10)
print(list(re))

list11=[4,5,6]
list12=[4,5,6]
res=map(lambda x,y:x+y,list11,list12)
print(list(res))


list14=["hello","name","now","get"]
rest=list(map(list,list14))
print(rest)

#lambda function we can call it anonymous function
def cube(n):
    return n*n*n

c=cube(5)
print(c)


ressult=(lambda a:a*a*a)
print(ressult(5))


l15=[10,12,10,11,14,18]
de=(list(map(lambda a:a**5,l15)))
print(list(de))

de1=list(filter(lambda a:  a%2!=0,l15))
print(de1)

from functools import reduce
de2=reduce(lambda a,b:a*b,l15)
print(de2)



















































