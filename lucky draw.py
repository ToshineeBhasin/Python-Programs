'''
program to play lucky draw if your number is matched with computer
generated number then you will win the lucky draw otherwise you loose 
it should be between 1 to 6
'''

import random
from random import randint
num=randint(1,6)    
n=int(input("guess the number :"))  
if n>6:         
    print("guess is too high")  
else:
    if num==n:                 
        print("You won the lucky draw...")
    else:
        print("You loss")

'''
output:
guess the number :6
You loss

or
guess the number :6
You won the lucky draw...

'''
