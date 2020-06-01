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

'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
1)  "a" - Append - will append to the end of the file
2)  "w" - Write - will overwrite any existing content
'''

#Open the file "demofile2.txt" and append content to the file:
f = open("toshi.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("toshi.txt", "r")
print(f.read())

'''
output:
Hello Everyone!!!!!!!

This is text file for python.Now the file has more content!
'''

'''
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:
1)  "x" - Create - will create a file, returns an error if the file exist
2)  "a" - Append - will create a file if the specified file does not exist
3)  "w" - Write - will create a file if the specified file does not exist
'''
f = open("myfile.txt", "x")     #Create a file called "myfile.txt"
f = open("myfile.txt", "w")     #Create a new file if it does not exist:


#Remove the file "demofile.txt":

import os
os.remove("toshi.txt")


#Check if file exists, then delete it:

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

