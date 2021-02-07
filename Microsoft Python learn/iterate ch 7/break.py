import random 
roll = 0
count = 0
print('First person to roll a 5 wins!')
while roll !=5:
    name = input('Enter a name, or \'q\'to quit:')
    if name =='q':
        break
    count = count+1
    roll = random.randint(1,5)
    print(f'{name} rolled {roll}')
else:
    print(f'{name} wins!!!')
    
print(f'You rolled the die {count} times.')
'''
First person to roll a 5 wins!
Enter a name, or 'q'to quit:toshu
toshu rolled 1
Enter a name, or 'q'to quit:tosss
tosss rolled 3
Enter a name, or 'q'to quit:tina
tina rolled 5
tina wins!!!
You rolled the die 3 times.

or

First person to roll a 5 wins!
Enter a name, or 'q'to quit:q
You rolled the die 0 times.

or

First person to roll a 5 wins!
Enter a name, or 'q'to quit:sunny
sunny rolled 3
Enter a name, or 'q'to quit:abhi
abhi rolled 1
Enter a name, or 'q'to quit:watson
watson rolled 3
Enter a name, or 'q'to quit:hina
hina rolled 5
hina wins!!!
You rolled the die 4 times.
'''