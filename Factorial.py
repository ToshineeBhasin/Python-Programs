'''
Created on 15-May-2020

@author: Toshinee Bhasin
'''
#Program to find factorial of a number
num=int(input("Enter a number :"))
fact=1
while num>1:
    fact=fact*num
    num=num-1
print("Factorial of a given number is ",fact)

'''
output:
Enter a number :5
Factorial of a given number is  120
'''