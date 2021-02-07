import random
roll = 0
count = 0
print('First person to roll a 5 Wins!')
while roll !=5:
    name = input('Enter a name, or \'q\' to quit: ')

    if name.strip() == '':
        continue
    if name.strip() == 'q':
        break

    count = count + 1
    roll = random.randint(1,5)
    print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')
'''
First person to roll a 5 Wins!
Enter a name, or 'q' to quit: toshi
toshi rolled 4
Enter a name, or 'q' to quit: abhi
abhi rolled 4
Enter a name, or 'q' to quit: deee
deee rolled 4
Enter a name, or 'q' to quit: ban
ban rolled 2
Enter a name, or 'q' to quit: aman
aman rolled 3
Enter a name, or 'q' to quit: sunny
sunny rolled 2
Enter a name, or 'q' to quit: tina
tina rolled 3
Enter a name, or 'q' to quit: abhishek
abhishek rolled 4
Enter a name, or 'q' to quit: dhanno
dhanno rolled 1
Enter a name, or 'q' to quit: amit
amit rolled 1
Enter a name, or 'q' to quit: arpita
arpita rolled 2
Enter a name, or 'q' to quit: jaggu
jaggu rolled 1
Enter a name, or 'q' to quit: jaya
jaya rolled 2
Enter a name, or 'q' to quit: amruta
amruta rolled 3
Enter a name, or 'q' to quit: divya
divya rolled 4
Enter a name, or 'q' to quit: jyoti
jyoti rolled 2
Enter a name, or 'q' to quit: kamla
kamla rolled 5
kamla Wins!!!
You rolled the dice 17 times.
'''