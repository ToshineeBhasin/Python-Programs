# Python program to check if the number is an Armstrong number or not

'''
An Armstrong number of three digits is an integer such that the sum of
the cubes of its digits is equal to the number itself. For example, 371 
is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.
'''

num=int(input("Enter a number :"))
sum=0
temp=num
while temp>0:
    n=temp%10
    sum=sum+n**3
    temp=temp//10
    
if num==sum:
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")
'''
output:
Enter a number :153
153 is armstrong
or
Enter a number :121
121 is not armstrong
'''
