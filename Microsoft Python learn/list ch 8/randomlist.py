import random
numbers = []

while len(numbers)<5:
    numbers.append(random.randint(1, 100))

for number in numbers:
    print(number)
    if number >= 90:
        print('Found at least one number greater than 90 ')
        break
    else:
        print('No numbers greater than 90')

print('Complete')
'''
60
No numbers greater than 90
58
No numbers greater than 90
87
No numbers greater than 90
40
No numbers greater than 90
25
No numbers greater than 90
Complete

or  

45
No numbers greater than 90
90
Found at least one number greater than 90
Complete
'''