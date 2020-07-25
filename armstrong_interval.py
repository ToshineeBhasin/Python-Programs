'''
Created on 25-Jul-2020

@author: Toshinee Bhasin
'''
# Program to check Armstrong numbers in a certain interval

lower = eval(input("Enter lower limit :"))
upper = eval(input("Enter upper limit :"))


for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
        
'''
output:
Enter lower limit :1
Enter upper limit :1000
1
2
3
4
5
6
7
8
9
153
370
371
407
'''