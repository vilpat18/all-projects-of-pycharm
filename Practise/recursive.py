'''def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(7)
print(result)


f = lambda a: a*a
result=f(5)
print(result)'''


#filter,map,reduce using lambda function
'''nums = [4,3,4,6,5,3,1,8,4,2]
even=list(filter(lambda n : n%2==0,nums))
print(even)

double=list(map(lambda n :n*2,even))
print(double)

from functools import reduce
xyz=reduce(lambda a,b:a+b,nums)
print(xyz)'''


hash=[4,2,4,7,89,63,4,4,7,8,9,6,4,1,2,3,]
odd1=list(filter(lambda a:a%2!=0,hash))
print(odd1)

odd2=[1,2,4,4,7]
print(odd2)
map1=list(map(lambda n:n*2,odd2))
print(map1)

from functools import reduce
add=reduce(lambda a,b:a+b,map1)
print(add)



