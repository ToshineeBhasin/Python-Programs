'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
#The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("An exception occurred")
#output:An exception occurred


#Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#output:Variable x is not defined


#In this example, the try block does not generate any error:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
'''
output:
Hello
Nothing went wrong
'''

#The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
'''
output:
Something went wrong
The 'try except' is finished
'''

#Try to open and write to a file that is not writable:
try:
    f = open("demo.txt")
    f.write("Toshinee Bhasin")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
'''
output:
Something went wrong when writing to the file
Traceback (most recent call last):
  File "C:\Users\Toshinee Bhasin\eclipse-workspace\DemoPython\Abhishek\TryCatch.py", line 64, in <module>
    f.close()
NameError: name 'f' is not defined
'''


#Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
'''
output:
 raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero
'''

#Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
'''
output:
raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed
'''
