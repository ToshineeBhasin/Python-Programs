#program to find HCF or GCD of two numbers 
print("Enter two numbers :")
num1=int(input("Enter first number :"))
num2=int(input("Enter Second number :"))
if num1>num2:
    smaller=num2
else:
    smaller=num1
    for i in range(1,smaller+1):
        if ((num1%i==0)and(num2%i==0)):
            hcf=i
print("HCF of given numbers is ",hcf)


'''
output:
Enter two numbers :
Enter first number :22
Enter Second number :36
HCF of given numbers is  2
'''









