s1='''vilas patil 
       karla bk'''
print(type(s1))
print("\n name and hometown of student",s1 )

s2="vilas patil"
print(s2[0:4])
print(s2[-5])

#deleting or updating a string
s3="you must \"have\""
print(s3)
s4= "I'm a boy "
print(s4)

s5="c: python server"
print(s5)

vittal=(R"\x47\x78\x45\x98")
print(vittal)

s6=("\t vilas \t")
print(s6)

s7=("\t vikas")
print(s7)

s8=("vilas\t")
print(s8)

s9="{} {} {}".format("python","is","awesome")
print(s9)

s10="{} {} {} {}".format("india","is","my","country")
print(s10)

s11="{0} {2} {3} {1}".format("india","is","my","country")
print(s11)

s12="{a} {b} {c}".format(b='awesome',a='python',c='is')
print(s12)

s13="{0:b}".format(10)
print(s13)

s14="{0:e}".format(16.5)
print(s14)

#rounding of integers
s15="{0:.2f}".format(10/20)
print(s15)

#split
s16="python \nis \nawesome"
s16.split()
print(s16)

s17="GeeksforGeeks, is an-awesome! website"
s17.split()
s18=[]
for char in s17:
    if char not in s18:
        s18.append(char)
print(s18)

#replace() and split()
data="lets, try_this now"
recode=data.replace('_',' ').replace(',',' ').split()
print(recode)

s20="go to hell"
s21=[ i for j in s20.split() for i in (j, '_')][:-1]
print(s21)

from itertools import chain,cycle
s22="god is great"
s23=list(chain(*zip(s22.split(),cycle(' '))))[:-1]
print(s23)













