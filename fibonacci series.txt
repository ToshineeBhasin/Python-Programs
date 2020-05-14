'''
The Fibonacci Sequence is the series of numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers before it:
'''
# Program to display the Fibonacci sequence up to n-th term

maxlimit=int(input("Enter maximum limit to print fibonacci numbers :"))
num1=0
num2=1
count=0
print("Fibonacci series")
print(num1,end=" ")
print(num2,end=" ")
while maxlimit>count:
    
    num=num1+num2
    print(num,end=" ")
    num1=num2
    num2=num
    count=count+1
'''    
output:
Enter maximum limit to print fibonacci numbers :10
Fibonacci series
0 1 1 2 3 5 8 13 21 34 55 89 
'''
