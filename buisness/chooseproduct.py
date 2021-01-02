import copy
from pprint import pprint
product_list={"mobile_brands":
                  {"nokia":{"model":1600,"price":100,"quantity":10},
                   "moto":{"model":"E3power","price":100,"quantity":10},
                   "iphone":{"model":"prime","price":200,"quantity":20},
                   "oppo":{"model":"j6","price":100,"quantity":30}}}

print(".................WelCome To FlipKart Shopping..................")
pprint(product_list)


while True:
    select = input("enter the name of brand: ")
    if select=="nokia" or select=="moto" or select=="iphone" or select=="oppo":
        buy=(product_list["mobile_brands"][select])
        item_price=product_list["mobile_brands"][select]['price']
        print("The Price Of This Mobile Is RS",item_price)

    else:
        print("this product is not available")
        break

    items=int(input("enter the quantity: "))
    if items>(product_list["mobile_brands"][select]["quantity"]):
        print("sorry selcted quantity not available")
    else:
        product_list["mobile_brands"][select]["quantity"]=product_list["mobile_brands"][select]["quantity"]-items
        total_pay_amount=items*item_price
        if total_pay_amount>=500:
           delivery_charge=20
        elif total_pay_amount<500:
           delivery_charge=40

           print("the total cost of product:{} and delivery charges:{}".format(total_pay_amount,delivery_charge))
           print("the payable amount is",total_pay_amount+delivery_charge)
           actual_pay=total_pay_amount + delivery_charge
           #client_balance = 1000
           #print("Your Account balance is",client_balance)
           seq = int(input("if you want to purchase- \n1-yes \n2-no: "))
           if seq == 1:
               client_bank_SBI_intrest=actual_pay*(2/100)
               print("actual client paying intrest to his SBI BANK RS",[client_bank_SBI_intrest])
               print()
               print("the total amount client is paying bank intrest {} and to flipkart {}:".format(client_bank_SBI_intrest,actual_pay))
               print("total money deducted from client acoount is RS",[actual_pay+client_bank_SBI_intrest])
               print()
               print("money recieved by FLIPKART from client is RS",[actual_pay])
               print()
               vendor_money=(actual_pay*(80/100))
               transfer_charge=actual_pay*(2/100)
               print("vendor recieved money from flipkart is RS",[vendor_money])
               print("for vendors trasaction flipcart pying charge to his bank is RS",[transfer_charge])
               delivery_account=actual_pay*(5/100)
               print("Ekart getting 5% money from Flipcart is RS",[delivery_account])
               transfer_charge_delivery=actual_pay*(1.2/100)
               print("for delivery transaction flikart paying 1.2% charge to his bank is RS",[transfer_charge_delivery])
               flipkart_profit_amount=actual_pay-(vendor_money+transfer_charge+delivery_account+transfer_charge_delivery)
               print()
               print("flipkart profitable amount is RS",[f"{flipkart_profit_amount:.2f}"])
               print("___________________THANK YOU FOR CHOSING FLIPCART PLS VISIT AGAIN________________________")
               break
           elif seq == 2:
               print("thank you for visiting FlipKart")
           else:
               print("Enter Valid input")




























