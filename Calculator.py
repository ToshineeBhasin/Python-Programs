#Program to make a simple calculator

def add(a,b):
    print("sum of two numbers is ",a+b)

def sub(a,b):
    print("Subtraction of two numbers is ",a-b)

def mul(a,b):
    print("Multiplication of two numbers is ",a*b)

def div(a,b):
    print("Division of two numbers is ",a//b)

def mod(a,b):
    print("Modulus of two numbers is ",a%b)

def square(a):
    print("Square of a number is ",a*a)

def cube(a):
    print("Cube of a number is ",a*a*a)

num1=eval(input("Enter first number : "))
num2=eval(input("Enter second number : "))

print("****** Menu list ******")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
print("5. Modulus ")
print("6. Square of a number ")
print("7. Cube of a number ")
print("8. Exit")
ch=int(input("Enter your choice :"))

if ch==1:
    add(num1,num2)
elif ch==2:
    sub(num1,num2)
elif ch==3:
    mul(num1,num2)
elif ch==4:
    div(num1,num2)
elif ch==5:
    mod(num1,num2)
elif ch==6:
    square(num1)
elif ch==7:
    cube(num1)
else:
    print("Wrong choice.....")
  
'''
output:
Enter first number : 45
Enter second number : 23
****** Menu list ******
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division 
5. Modulus 
6. Square of a number 
7. Cube of a number 
8. Exit
Enter your choice :3
Multiplication of two numbers is  1035
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
