'''
Created on 10-Sep-2020

@author: Toshinee Bhasin
'''
str=""
str1 = "Toshinee#@Bhasin@123'gmail.com"
print("Given String : ",str1)
removal =[]
str2 = list(str1)
for i in str2:
    if i>='a' and i<='z':    
        pass
    elif i>='A' and i<='Z': 
        pass
    elif i>='0' and i<='9':
        pass
    else:
        removal.append(i)
        
for i in removal:
    str2.remove(i)

print("\nAfter Removing special symbols and  Punctuation from a given string : ")
for i in str2:
    str=str+i

print(str)
'''
output:
Given String :  Toshinee#@Bhasin@123'gmail.com

After Removing special symbols and  Punctuation from a given string : 
ToshineeBhasin123gmailcom
'''