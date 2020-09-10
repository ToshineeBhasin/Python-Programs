'''
Created on 09-Sep-2020

@author: Toshinee Bhasin
'''
string1 = input("Enter first string :")
s=int(len(string1)/2)
s1 = string1[0]+string1[s]+string1[-1]

  
string2 = input("Enter second string :")
s=int(len(string2)/2)
s2 = string2[0]+string2[s]+string2[-1]

print("first ,middle and last character of given two strigs :")
print(string1[0]+string2[0]+string1[s]+string2[s]+string1[-1]+string2[-1])
'''
output:
Enter first string :toshi
Enter second string :bhasin
first ,middle and last character of given two strigs :
tbhsin
'''