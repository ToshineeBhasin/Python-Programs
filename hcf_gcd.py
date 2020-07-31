'''
Created on 30-Jul-2020

@author: Toshinee Bhasin
'''
# Python program to find H.C.F of two numbers

def hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("The H.C.F. is", hcf(num1, num2))
'''
output:
Enter first number : 12
Enter second number : 26
The H.C.F. is 2
'''