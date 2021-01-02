#list all mutablethe
#each element in list has its own dictinct place
#the list may have contain differnet data types like,integers,string as well as object

l1=[]
print(l1)

l2=["india is my country"]
print(l2)

l3=['india','is','my','country']
print(l3[0])
print(l3[-1])

l4=['hello',"how",['are','you'],(12,10),{"key":"value","key1":"value1","vilas":"patil"}]
print(l4)
print(l4[3][-1])
print(l4[4]["vilas"])
l4.append(12)
print(l4)

l6=["hi",12,12.5,"num"]
l6.insert(2,10)
l6.insert(4,"vilas")
l6.extend([99])
print(l6)
print("intial list: ",l6)
a=l6.pop()
print(a)
print(l6)


list10=[12,10,{"key":"value","key1":"value1"}]
print(list10)
b=list10.pop()
print(b)

list11=[14,10,47,78,98]
list11.remove(10)
print(list11)

list12=[(12,14,45),(78,1),{"key":"value","key2":"value2"}]
list12[2].pop("key2")
print(list12)




ll=[12,45,7,98,74,54,745]
lll=ll.pop(2)
print(ll)
print(lll)

ll.clear()
print()
print(ll)

list13=[12,45,78,98]
list13=[]
print(list13)




















