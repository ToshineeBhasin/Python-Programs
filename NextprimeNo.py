#program to print next prime number of given number
num=int(input("Enter the number :"))

def nextPrime(num):
    while True:
        num=num+1
        for i in range(2,num):
            if num%i==0:
                        break
        else:
            return num
            
print("Next prime no is ",nextPrime(num))                    

'''
output:
Enter the number :11
Next prime no is  13
'''
