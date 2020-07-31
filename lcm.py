'''
Created on 30-Jul-2020

@author: Toshinee Bhasin
'''
# Python Program to find the L.C.M. of two input number

def lcm(x, y):

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("The L.C.M. is", lcm(num1, num2))
'''
output:
Enter first number : 34
Enter second number : 26
The L.C.M. is 442

'''