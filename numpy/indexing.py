import numpy as np
arr =  np.array([1,2,3,4])
print("Value at index 0 : ",arr[0])
'''
Value at index 0 :  1
'''

arr = np.array([1,2,3,4])
print("Addition of 2 array using their indexes (i.e., 2 and 3): ",arr[2] + arr[3])
'''
Addition of 2 array using their indexes (i.e., 2 and 3):  7
'''
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])
'''
2nd element on 1st dim:  2
'''
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd dim: ', arr[1, 4])
'''
5th element on 2nd dim:  10
'''
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])         #arr[0, 1, 2] prints the value 6
