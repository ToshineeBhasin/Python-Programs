# Python program to display the Fibonacci sequence

def fibo_recur(num):
    if num <= 1:
        return num
    else:
        return(fibo_recur(num-1) + fibo_recur(num-2))

maxterms=int(input("Enter maximum terms or max range :"))


# check if the number of terms is valid
if maxterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(maxterms):
        print(fibo_recur(i),end=" ")
        
'''        
output:
Enter maximum terms or max range :10
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34 
'''
