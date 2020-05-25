'''
Created on 25-May-2020

@author: Toshinee Bhasin
'''
# Program to transpose a matrix using a nested loop

X = [[1,4],
    [2 ,5],
    [3 ,6]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
    #iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

print("Transpose of matrix :")
for r in result:
    print(r)
    
'''
output:
Transpose of matrix :
[1, 2, 3]
[4, 5, 6]
'''
