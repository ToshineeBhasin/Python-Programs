#pythno program to print factorial of a given number
num=int(input("Enter a number :"))
fact=1
while num>1:
    fact=fact*num
    num=num-1
print("Factorial of a given number is ",fact)

'''
output:
Enter a number :5
Factorial of a given number is  120
'''
