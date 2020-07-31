'''
Created on 30-Jul-2020

@author: Toshinee Bhasin
'''
#python program to display number divide by another number
my_list = []
n = int(input("Enter total number of element :"))
print("Enter numbers :")
for i in range(0,n):
    ele=int(input())
    my_list.append(ele)
    
# use anonymous function to filter
result = list(filter(lambda x: (x % 12 == 0), my_list))

# display the result
print("Numbers divisible by 12 are",result)
'''
output:
Enter total number of element :5
Enter numbers :
12
64
54
39
102
Numbers divisible by 12 are [12]
'''