import random

guess = 0
num = 0
count = 0

guess = random.randint(1,5)

while num!=guess:
    count+=1
    num = input('Guess a number between 1 and 5 : ') 
    if num.isnumeric():
        num = int(num)

else:
    print(f'You guessed it in {count} tries!')

'''
Guess a number between 1 and 5 : 5
Guess a number between 1 and 5 : 4
Guess a number between 1 and 5 : 3
You guessed it in 3 tries!
'''




