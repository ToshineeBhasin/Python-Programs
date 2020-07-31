'''
Created on 30-Jul-2020

@author: Toshinee Bhasin
'''
# Program make a simple calculator


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("*** Menu *** :")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice : ")

   
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
        
'''
output:
*** Menu *** :
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice : 1
Enter first number: 22
Enter second number: 17
22.0 + 17.0 = 39.0
'''