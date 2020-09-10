'''
Created on 10-Sep-2020

@author: Toshinee Bhasin
'''
lst = [" ", "Toshinee", " ", "is", "awesome", " "] 
 
print ("Entered list is  " + str(lst)) 
while(" " in lst) : 
    lst.remove(" ") 
        
print ("Modified list is : " + str(lst)) 
'''
output:
Entered list is  [' ', 'Toshinee', ' ', 'is', 'awesome', ' ']
Modified list is : ['Toshinee', 'is', 'awesome']
'''