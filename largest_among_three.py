'''
Created on 25-Jul-2020

@author: Toshinee Bhasin
'''
num1 = eval(input("Enter First number :"))
num2 = eval(input("Enter Second number :"))
num3 = eval(input("Enter Third number :"))
if num1>num2 and num1>num3:
    print(num1," is greater")
elif num2>num3:
    print(num2," is greater") 
else:
    print(num3," is greater")
''' 
output:
Enter First number :1
Enter Second number :2
Enter Third number :1
2  is greater
'''