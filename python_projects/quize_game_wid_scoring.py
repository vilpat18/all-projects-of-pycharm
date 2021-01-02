import time
true = ['True','t','T']
false = ['False','f','F']
correct = 0 # storing the correct answer

name = input("what's your name: ") # storing user name
print("ok," + name + ", lets get started. Remeber ,the following answers")
time.sleep(2)

print('\nmumbai is a capital of maharashtra')
choice = input(">>> ")
if choice in true:
    correct +=1
else:
    correct += 0

print('\nmumbai is a capital of india')
choice = input(">>> ")
if choice in false:
    correct +=1
else:
    correct += 0

print('\nvirat kohli hitts two double hundreds in odi cricket')
choice = input(">>> ")
if choice in false:
    correct +=1
else:
    correct += 0

print('\nrohit sharma hitts 3 double hundreds in odi cricket')
choice = input(">>> ")
if choice in true:
    correct +=1
else:
    correct += 0

print('\nsupriya ghogare from loni')
choice = input(">>> ")
if choice in true:
    correct +=1
else:
    correct += 0

print('\nmumbai indians captain is rohit sharma')
choice = input(">>> ")
if choice in true:
    correct +=1
else:
    correct += 0

print("You're Finished,"+name +"you got",correct,"out of 6")