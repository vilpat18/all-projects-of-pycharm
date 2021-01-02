import re

phn = input("enter phone number with - : ")

if re.search("\w{3}-\w{3}-\w{4}",phn):
    print("its valid number")
else:
    print('invalid phone number')


phn = input("enter phone number with - : ")
if re.search("\w{10}",phn):
    print("its valid number")
else:
    print('invalid phone number')
