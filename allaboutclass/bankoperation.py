import sys
class Customer:
    bankname = "SBI BANK"
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("balance after deposite: ",self.balance)

print("WELL COME TO",Customer.bankname)
name=input("enter customer name: ")
c=Customer(name)
while True:
    print("d=deposite\nw=withdraw\ne=exit")
    option=input("choose your option: ")
    if option=="d" or option=="D":
        amt=float(input("enter the amount: "))
        c.deposit(amt)





