#python program to check whether a number is armstrong or not
num = int(input("Enter a number: "))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
    
'''
output:
Enter a number: 153
153 is an Armstrong number
or 
Enter a number: 123
123 is not an Armstrong number
'''
