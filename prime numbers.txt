'''
Prime numbers are divisible only by the number 1 or itself.  
For example, 2, 3, 5, 7 and 11 are the first few prime numbers.
'''
#program to print first n prime number

start=int(input("Enter the mininum range :"))
end=int(input("Enter the maxium range :"))
print("Primr  umbers are: ")
for val in range(start,end,1):
    if val>1:
        for n in range(2,val):
            if val%n==0:
                break
        else:
            print(val,end=" ")
  
'''
output:
Enter the mininum range :2
Enter the maxium range :15
Primr  umbers are: 
2 3 5 7 11 13 
'''
