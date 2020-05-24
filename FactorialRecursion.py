'''
Created on 24-May-2020

@author: Toshinee Bhasin
'''
# Factorial of a number using recursion

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

num=int(input("Enter the number you find the factorial of "))

# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
    
'''    
output:
Enter the number you find the factorial of 5
The factorial of 5 is 120
''' 