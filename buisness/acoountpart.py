#client_remain_balance = client_balance - actual_pay
               #print("the remaining balnce is",client_remain_balance)
               x=actual_pay*(2/100) #2% intrest
               total_client_amount=actual_pay+x
               print("total amount pay by client",total_client_amount)
               print()
               client_bank_ICICI=x
               print("client bank recived intrest client_bank_ICICI RS",client_bank_ICICI)
               print()
               flipcart_acount=actual_pay
               print("flipcart acount credited with RS",flipcart_acount)
               print()
               flipcart_bank_AXIS=(flipcart_acount*(2/100))
               print("flipcart bank recieved intrest AXIS bank RS",flipcart_bank_AXIS)
               print()
               total_Flipkart_balnce=flipcart_acount-flipcart_bank_AXIS
               print("total flipcart remaining balanceis",total_Flipkart_balnce)
               print()
               SBI_vendor_acount=(total_Flipkart_balnce*(85/100))
               print("vendor acount recieved money from flipcart",SBI_vendor_acount)
               print()
               flipcart_acount=total_Flipkart_balnce-SBI_vendor_acount
               print("total ramianing balance of flipcart is RS",flipcart_acount)
               print()
               HDFC_delivery_account=total_Flipkart_balnce*(5/100)
               print("total delivery acount credited amount is RS",HDFC_delivery_account)
               print()
               flipcart_bank_AXIS=total_Flipkart_balnce*(2/100)
               print("flipcart credited delivery intrest is RS",flipcart_bank_AXIS)
               print()
               vendor_transfer_intrest=flipcart_acount*(1.2/100)
               final_flipcart_acount=flipcart_acount-(vendor_transfer_intrest+HDFC_delivery_account)
               print(final_flipcart_acount)
               print()