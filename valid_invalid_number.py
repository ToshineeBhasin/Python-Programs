#program to check whether a number is valid or invalid
valid=0
invalid=0
for i in range(5):
    try:
        n=int(input("Enter any number :"))
        valid+=1
    except Exception:
        invalid+=1
        
print("Entered valid numbers :",valid)
print("Entered invalid numbers :",invalid)
'''
output:
Enter any number :0
Enter any number :-7
Enter any number :5
Enter any number :9
Enter any number :j
Entered valid numbers : 4
Entered invalid numbers : 1
'''
