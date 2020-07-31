'''
Created on 30-Jul-2020

@author: Toshinee Bhasin
'''
# Python Program to find the factors of a number


def factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = int(input("Enter a number : "))
factors(num)
'''
output:
Enter a number : 22
The factors of 22 are:
1
2
11
22

'''