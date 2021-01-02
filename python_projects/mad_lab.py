import random

print('mad libs !!!!')
print('enter a example of each . Remeber to use quotation marks')

random_name = input('random_name: ')
your_name = input('Your_name: ')
place = input('place: ')
adjective = input('Adjective: ex. wierd: ')

adjs = ["Crazy", "Nice", "Lovely", "Gross"]
verbs = ["met", "proposed to", "robbed", "pushed"]
prepositions = ["above the", "near the", "around the", "behind", "beside"]

print((random.choice(adjs)) + " " + random_name + " " + (random.choice(verbs)) + " " + your_name + " " + (
    random.choice(prepositions)) + " " + adjective + " " + place)
