from base64 import main
from os import name

address_dict = {'add_name': {'name': 'new_name', 'phone': 'new_phone', 'address': 'new_address', 'sex': 'gender'}}


def add_person():
    nick_name = input('enter the nickname of the person: ')
    name = input('enter the name: ')
    phone = input('enter the phone number: ')
    address = input('enter the address: ')
    sex_type = input('enter the gender: ')
    add = False
    for i in address_dict:
        if i.lower() == name.lower():
            print('Name alredy exsists')
        elif address_dict[i]['name'].lower() == name.lower():
            print('name alredy there')
        else:
            add = True
    if add:
        address_dict.update({nick_name: {'name': name, 'phone': phone, 'address': address, 'sex': sex_type}})


def indexperson():
    name = input("type the person's name or nickname: ")
    for i in address_dict:
        if i.lower() == name.lower() or address_dict[i]['name'].lower() == name.lower():
            print('\nName: %s\nPhone: %s\nAddress: %s\nSex: %s\n' \
                  % (address_dict[i]['name'], address_dict[i]['phone'], address_dict[i]['address'],
                     address_dict[i]['sex']))

        else:
            print('user not found')


def YesNo():
    yesno = input('would you like to add new contact y/n \n : ')
    if yesno == 'y':
        add_person()
    elif yesno == 'n':
        indexperson()
    else:
        print('pls choose valid option')

YesNo()
print(address_dict)
# main()
# quit()
#
# my_dict = {
#     "Don": {
#         "name": "Donald Jones",
#         "address": "1 Rue Rivoli Paris ",
#         "phone": "9444444411",
#         'sex': 'male'
#     },
#     "Joseph": {
#         "name": "Joseph Boy",
#         "address": "3 Tivoli Paris",
#         "phone": "0800838383",
#         'sex': 'male'
#     },
#     "Bilbo": {
#         "name": "Bilbo Baggin",
#         "address": "4 White House Washington",
#         "phone": "08055550838383",
#         'sex': 'female'
#     }
# }
#
# def fetch_details():
#     print(f'\nWhat we know about{name} ')
#     for key , value in my_dict[name].items():
#         print(f'{key}:{value}')
#
# fetch_details()