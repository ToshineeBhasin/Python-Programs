'''
Created on 10-Sep-2020

@author: Toshinee Bhasin
'''

s1 = input("Enter first string :")
s2 = input("Enter second string :")
mid = int(len(s1)/2)
s1=s1[:mid]+s2+s1[mid:]

print("Adding second string in mid of first string : ",s1)
'''
output:
Enter first string :toshinee
Enter second string :bhasin
Adding second string in mid of first string :  toshbhasininee
'''
