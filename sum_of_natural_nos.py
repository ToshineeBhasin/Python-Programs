
# Sum of natural numbers up to num

num = eval(input("Enter the number :"))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)
    
'''
output:
Enter the number :12
The sum is 78
'''
