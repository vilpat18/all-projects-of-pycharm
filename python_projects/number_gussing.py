import random
hidden = random.randrange(1,201)
# print(hidden)
guess = int(input('enter the number: '))
if guess == hidden :
    print('hit!!!!')
elif guess < hidden:
    print('your guess is too low')