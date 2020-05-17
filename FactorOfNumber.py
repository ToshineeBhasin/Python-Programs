#Program to find factors of a number 
x=int(input("Enter the number : "))
print("Factors of", x," are ")
for i in range(1,x+1):
    if x%i==0:
        print(i)

'''
output:
Enter the number : 21
Factors of 21  are 
1
3
7
21
'''
























