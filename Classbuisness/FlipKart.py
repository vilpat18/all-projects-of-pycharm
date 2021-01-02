import copy
from pprint import pprint
class Flipkart:

    product_list ={"mobiles":{"motorola": {"model": "Moto g3", "price": 1000, "quantity": 10},
                      "apple": {"model": "iphone X", "price": 4000, "quantity": 10},
                      " oneplus": {"model": "1+7T", "price": 3500, "quantity": 10},
                      "redmi": {"model": "Note 8 Pro", "price": 2500, "quantity": 10}}}
    def __init__(self):
        pass

    print("____________Wel-Come To Flipcart Shopping____________")
    def vendor_buyer(self):
            while True:
                start_s = input("enter the c if you are customer or v if you are vendor:  ")
                if start_s == "v":
                    print("_______________add product______________")
                    d = copy.deepcopy(Flipkart.product_list)
                    add_new = int(input("entr the no.of product you want to add: "))
                    for i in range(add_new):
                        self.vendor_list = {}
                        self.brand = input("add new brand: ")
                        model = input("enter the model name: ")
                        price = int(input("enter the price: "))
                        quantity = int(input("enter the no of quantity: "))
                        self.vendor_list["model"] = model
                        self.vendor_list["price"] = price
                        self.vendor_list["quantity"] = quantity
                        d[self.brand] = [self.vendor_list]
                        pprint(d)
                        pprint(Flipkart.product_list)

                elif start_s == "c":
                    print("______________Select the item from above product list____________ ")
                    select = ("select the brand name: ")


                else:
                    print("pls enter valid input")










obj=Flipkart()
obj.vendor_buyer()