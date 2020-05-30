'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
# Try Catch Block(try within try block)
try:
    l=[1,2,3]
    try:
        s=input("enter any string :")
        print(s[5])
        print(s//2)
    except IndexError:
        print("Index out of bound")
    finally:
        print("Finally of inner block executed ")
        
except TypeError:
    print("Wrong string operations")
finally:
    print("Finally of outer block executed")
'''    
output:
enter any string :Toshinee
n
Finally of inner block executed 
Wrong string operations
Finally of outer block executed
'''
#try catch using function
def readdata():
    n=int(input("Enter any natural number :"))
    if n<1:
        raise Exception("Natural number start with 1...",707)
    print("Entered no is ",n)
    
try:
    readdata()
except Exception as e:
    print(e)
    print(e.args)
    print("Error Message : ",e.args[0])
    print("Error no :",e.args[1])

'''
output:
Enter any natural number :111
Entered no is  111

or 

Enter any natural number :0
('Natural number start with 1...', 707)
('Natural number start with 1...', 707)
Error Message :  Natural number start with 1...
Error no : 707
'''
#try catch using while
while True:
    try:
        n=int(input("Enter any no. between 1 and 4 :"))
        if n>=1 and n<=4:
            break
        else:
            print("No should be between 1 and 4 :")
    except Exception as e:
        print(e)
'''
output:
Enter any no. between 1 and 4 :3
or 
Enter any no. between 1 and 4 :5
No should be between 1 and 4 :
Enter any no. between 1 and 4 :3
'''
#usinf try catch block in function definition and in function calling
def divide(x,y):
    try:
        print(x/y)
        return
        print("This line will never be executed.")
    finally:
        print("finally of divide executed")
        
try:
    #divide(10,5)
    divide(10,0)
    s="abc"
    print(s[5])
except Exception as e:
    print("Exception caught : "+str(e))
    
'''
output:
2.0
finally of divide executed        #when divide(10,5) called
Exception caught : string index out of range

or 

finally of divide executed        ##when divide(10,0) called
Exception caught : division by zero

'''
