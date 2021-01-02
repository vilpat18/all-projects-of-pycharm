regex ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

import re

def check_email(email):
    if re.search(regex,email):
        print('valid email')
    else:
        print('invalid email')


email_input = input("pls enter the email: ")
check_email(email_input)