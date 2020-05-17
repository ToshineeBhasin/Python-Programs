'''
The least common multiple (L.C.M.) of two numbers is the 
smallest positive integer that is perfectly divisible by 
the two given numbers.

For example, the L.C.M. of 12 and 14 is 84.
'''
#program to find LCM of 2 numbers
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
if num1>num2:
    greater=num1
else:
    greater=num2
    while(True):
        if ((greater%num1==0) and (greater%num2==0)):
            lcm=greater
            break
        greater=greater+1
print("LCM of ",num1," and ",num2," is ",lcm)            

'''
output:
Enter first number :2
Enter second number :12
LCM of  2  and  12  is  12
'''

















