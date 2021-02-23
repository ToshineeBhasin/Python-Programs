import random
import math#taking inputs
lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))

x = random.randint(lower,upper)
print("\n \tYou have only ",round(math.log(upper - lower +1, 2 )), "Chances to guess the integer !\n")

#initializing no of guess
count = 0

#minimum no of guess depend upon range
while count < math.log(upper - lower +1,2):
    count += 1

    #taling guessing number as input
    guess = int(input("Guess a number : "))

    #condition testing
    if x == guess:
        print("Congralutions you did it in ",count," try ")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

#if guesses is more the required guesses
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d " % x)
    print("\tBetter Luck Next Time!")

'''
Enter lower limit : 2
Enter upper limit : 20

        You have only  4 Chances to guess the integer !

Guess a number : 6
You guessed too small!
Guess a number : 10
You guessed too small!
Guess a number : 15
You guessed too small!
Guess a number : 20
Congralutions you did it in  4  try
'''