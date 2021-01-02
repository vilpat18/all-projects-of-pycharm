import copy
from pprint import pprint
#add_items={}
#product_list=[]
#d=copy.deepcopy(product_list)
#n=int(input("entr the no. of product do you want to add: "))
product_list={"brand":
                  {"nokia":{"model":1600,"price":1400,"quantity":10},
                   "moto":{"model":"E3power","price":5000,"quantity":10},
                   "oppo":{"model":"prime","price":7000,"quantity":20},
                   "samsung":{"model":"j6","price":8000,"quantity":30}}}
'''for i in range(n):
    brand=input("enter the brand name: ")
    model=input("enter the model name: ")
    price=int(input("enter the price: "))
    quantity=int(input("entr the no. of quantity you want to add: "))
    add_items["brand"]=brand
    add_items["model"]=model
    add_items["price"]=price
    add_items["quantity"]=quantity
    product_list.append(add_items)

pprint(product_list)'''

select=input("enter the name of brand: ")
for select in product_list:
    if select=="nokia" or select=="oppo" or select=="moto" or select=="samsung":
        print(product_list["brand"][select])
    else:
        print("the product is not available")














