import copy
from pprint import pprint
product_list={"cosmo":
                        {"fcream":{"cream":"fai&lovely","price":100,"quantity":10},
                         "oil":{"hairoil":"bajaj","price":100,"quantity":10},
                        "powder":{"facepowder":"ponds","price":50,"quantity":20}}}

pprint(product_list)
print("__________________WELCOME TO FLIPKART SHOPPING__________________")
while True:
    select = input("selct the product from list: ")
    if select=="fcream" or select=="oil" or select=="powder":
        buy=(product_list["cosmo"][select])
        print(buy)
        item_price=(product_list["cosmo"][select]["price"])
        print("the price of product is",item_price)
    else:
        print("pls select from above available products")
        break

    q=int(input("entr the no of quantity you want: "))
    if q>(product_list["cosmo"][select]["quantity"]):
        print("sorry this selected quantity out of stoc ")
    else:
        product_list["cosmo"][select]["quantity"]= (product_list["cosmo"][select]["quantity"]-q)
        cost=q*item_price
        print("the total cost of selcted product is RS",cost)

        seq=int(input("select if you purchase a product /n1-yes /n2-no:"))
        if seq==1:
            print("total amount payable  ")



















