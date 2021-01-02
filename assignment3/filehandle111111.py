#f=open("virat.txt","w")
#f.write("hiii hello how are you")
#f.close()

'''f = open("virat.txt","r")
#print(f.read())

count=0
for char in f:
    for char2 in char:
        if char2.islower():
            count+=1
print(char)
print(count)'''

'''s = open("rohit.txt","w")
s.write("India is my country")
s.close()

s1 = open('rohit.txt','r')
print(s1.read())


for cap in s1:
        for up in cap:
                if up.isupper():
                        print(up)'''



m = open("dhawan.text",'w')
m.write('hiiii')

m2 = open('dhawan.text','a')
m2.write("python Devloper")
m2.close()

f2=open("received_1560427547366568.jpeg",'rb')
#print(f2.read())

for i in f2:
    print(i)

mypic=open('pic','wb')
for i in f2:
    mypic.write(i)










































