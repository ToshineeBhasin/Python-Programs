# Python program to find the sum of natural using recursive function

def recur_sum(num):
    if num <= 1:
        return num
    else:
        return num + recur_sum(num-1)

# change this value for a different result
term=int(input("Enter maximum term :"))

if term < 0:
    print("Enter a positive number")
else:
    print("The sum is",recur_sum(term))
  
'''    
output:
Enter maximum term :10
The sum is 55
'''
