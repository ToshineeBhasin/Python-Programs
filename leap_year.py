'''
Created on 25-Jul-2020

@author: Toshinee Bhasin
'''
year = eval(input("Enter a year :"))
if year%4 ==0 or (year%400==0 and year%100!=0):
    print(year," is leap year")
else:
    print(year," is not leap year")
    
'''
output:
Enter a year :2021
2021  is not leap year
or 
Enter a year :2016
2016  is leap year

'''