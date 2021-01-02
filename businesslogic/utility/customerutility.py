from utility.Flipkartutility import Flipkart
from pprint import pprint

class Customerinfo:
    def __init__(self):
        pass

    def search_product(self):
        print("__________________________WelCome To Flipkart Shopping__________________________")
        pprint(Flipkart.product_list)
        self.select=input("select the product: ")
        if self.select=="iphone" or self.select=="moto" or self.select=="nokia" or self.select=="redmi":
            print("______your selected product is below_______")
            print(Flipkart.product_list["brands"][self.select])
        else:
            print("this brand is not available at this moment pls choose amongst the above product lis")

    def choose_product(self):
            print("________the price of this product is________")
            print("Rs :",Flipkart.product_list["brands"][self.select]["price"])
            self.n=int(input("select the no. of quantity: "))
            if self.n>(Flipkart.product_list["brands"][self.select]["quantity"]):
                print("pls select some less quantity")
            else:
                self.total=self.n*(Flipkart.product_list["brands"][self.select]["price"])
                print("the total price of your product is: ",self.total)


                if self.total>=5000:
                    print("The total payable amount with delivery charge is :",self.total+100)
                else:
                    print("the total payable amount with delivery charge is",self.total+50)


    def purchase(self):

         self.p = int(input("if you want to purchase the products \nyes:[1]no:[2]"))
         if self.p=="1":
             self.client_bank_intrest = self.total * (2 / 100)
             print("total payable amount with bank charge is RS: ",self.total)



         else:
             print("insuficient balance pls check your account")
             self.balance = 50000



obj=Customerinfo()
obj.search_product()
obj.choose_product()
obj.purchase()