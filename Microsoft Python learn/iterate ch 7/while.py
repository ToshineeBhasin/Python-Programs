import random
roll = 0
count = 0
while roll != 5:
    count = count + 1
    roll = random.randint(1,5)
    print(roll)
print(f'It took {count} rolls to roll a 5!')
'''
5
It took 1 rolls to roll a 5!

or

3
2
2
3
4
3
5
It took 7 rolls to roll a 5!
'''
