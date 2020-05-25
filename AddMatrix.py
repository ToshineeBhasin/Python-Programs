'''
Created on 25-May-2020

@author: Toshinee Bhasin
'''
# Program to add two matrices using nested loop
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

print("Sum of given matrix is ")
for r in result:
    print(r)
    
'''
output:
Sum of given matrix is 
[17, 15, 4]
[10, 12, 9]
[11, 13, 18]

'''    