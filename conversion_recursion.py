'''
Created on 30-Jul-2020

@author: Toshinee Bhasin
'''
# Function to print binary number using recursion
def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2,end = '')

dec = int(input("Enter a decimal number : "))

convertToBinary(dec)
print()
'''
output:
Enter a decimal number : 24
11000
'''