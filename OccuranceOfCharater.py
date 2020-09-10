'''
Created on 10-Sep-2020

@author: Toshinee Bhasin
'''
#Python program to count occurrences of a given character 
  
str1 = "ToshineeBhasin"
count = {} 
  
for i in str1: 
    if i in count: 
        count[i] += 1
    else: 
        count[i] = 1
  
# printing result  
print("Count of all characters in \'ToshineeBhasin\' is :\n",  str(count)) 
'''
output:
Count of all characters in 'ToshineeBhasin' is :
 {'T': 1, 'o': 1, 's': 2, 'h': 2, 'i': 2, 'n': 2, 'e': 2, 'B': 1, 'a': 1}
 '''