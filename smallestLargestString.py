'''
Created on 09-Sep-2020

@author: Toshinee Bhasin
'''
str = "This is an umbrella";  
word = "";  
words = [];  
   
#Add extra space after string to get the last word in the given string  
str = str + " ";  
   
for i in range(0, len(str)):  
    #Split the string into words  
    if(str[i] != ' '):  
        word = word + str[i];  
    else:  
        #Add word to array words  
        words.append(word);  
        #Make word an empty string  
        word = "";  
          
#Initialize small and large with first word in the string  
small = large = words[0];  
   
#Determine smallest and largest word in the string  
for k in range(0, len(words)):  
      
    #If length of small is greater than any word present in the string  
    #Store value of word into small  
    if(len(small) > len(words[k])):  
        small = words[k];  
          
    #If length of large is less than any word present in the string  
    #Store value of word into large  
    if(len(large) < len(words[k])):  
        large = words[k];  
   
print("Smallest word: " + small);  
print("Largest word: " + large);  

'''
output:
Smallest word: is
Largest word: umbrella
'''