'''
Created on 31-May-2020

@author: Toshinee Bhasin
'''
'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
1)  "r" - Read - Default value. Opens a file for reading, error if the file does not exist
2)  "a" - Append - Opens a file for appending, creates the file if it does not exist
3)  "w" - Write - Opens a file for writing, creates the file if it does not exist
4)  "x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

#To open the file, use the built-in open() function.
#The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("toshi.txt", "r")
print(f.read())
'''
output:
Hello Everyone!!!!!!!
This is text file for python.
'''

#Return the 5 first characters of the file:

f = open("toshi.txt", "r")
print(f.read(5))

#output:Hello

#Read two lines of the file:

f = open("toshi.txt", "r")
print(f.readline())
print(f.readline())

'''
output:
Hello Everyone!!!!!!!

This is text file for python.
'''

#Loop through the file line by line:

f = open("toshi.txt", "r")
for x in f:
    print(x)
'''
output:
Hello Everyone!!!!!!!

This is text file for python.
'''
    
#Close the file when you are finish with it:

f = open("toshi.txt", "r")
print(f.readline())
f.close()

#output : Hello Everyone!!!!!!!





































