'''
Created on 25-Jul-2020

@author: Toshinee Bhasin
'''
u = eval(input("Enter upper limit :"))
l = eval(input("Enter lower limit :"))

print("Prime numbers between", u, "and", l, "are:")

for num in range(u, l + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
                
'''
output:
Enter upper limit :20
Enter lower limit :40
Prime numbers between 20 and 40 are:
23
29
31
37
'''