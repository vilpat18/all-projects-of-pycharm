'''num=[4,5,7,8,5,4,5,6]
it = iter(num)
print(it.__next__())
print(it.__next__())
print(it.__next__())'''

"""def topten():
    n=0
    while n<=10:
        sq=n*n
        yield sq
        n+=1

val=topten()
for i in val:
    print(i)"""
x=2;y=0
try:
   print(x/y)
#except ZeroDivisionError as e:
   # print("error")
except Exception as e:
    print("error",e)

finally:
     n="vilas patil"
     d={}
     for i in n.split():
          for j in i:
              d[j]=i
              break
     print(d)
     print("close resources")





