import random

guess = 0
num = 0
count = 0

guess = random.randint(1,10)

while num!=guess:
    count+=1
    num = input('Guess a number between 1 and 10 : ') 
    print(f'Enter guess #{count} :',num)
    if num.isnumeric() or num > guess:
        num = int(num)
    else:
        print('Numbers only, please!')
        continue

    if num > guess:
        print('Your guess is too high, try again! ')
    elif num < guess:
        print('Your guess is too low, try again! ')
    
else:
    print(f'You guessed it in {count} tries!')

'''
Guess a number between 1 and 10 : 10
Enter guess #1 : 10
Your guess is too high, try again!
Guess a number between 1 and 10 : 4
Enter guess #2 : 4
Your guess is too low, try again!
Guess a number between 1 and 10 : 5
Enter guess #3 : 5
Your guess is too low, try again!
Guess a number between 1 and 10 : 6
Enter guess #4 : 6
Your guess is too low, try again!
Guess a number between 1 and 10 : 7
Enter guess #5 : 7
Your guess is too low, try again!
Guess a number between 1 and 10 : 8
Enter guess #6 : 8
You guessed it in 6 tries!
'''