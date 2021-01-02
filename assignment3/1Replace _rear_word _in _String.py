'''print("enter the string: ")
s =input().split(' ')
print("this is original string: ",s)
new = "good"
res = (" ".join(s[:-1] + [new]))
print("this is new string: ",res)'''

def rep(s):
    new = "good"
    print((s[:-1]+[new]))

s = "python is awesome"
m = s.split(',')
rep(m)









