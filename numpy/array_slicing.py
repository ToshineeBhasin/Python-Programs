import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("Slicing from 1 to 5 : ",arr[1:5])
'''
Slicing from 1 to 5 :  [2 3 4 5]
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("Slicing array from index 4 to last : ",arr[4:])
'''
Slicing array from index 4 to last :  [5 6 7]
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Negative Slicing : ",arr[-3:-1])
'''
Negative Slicing :  [5 6]
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Steps : ",arr[1:5:2])
'''
Steps :  [2 4]
'''
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Slicing 2-D array : ",arr[1, 1:4])
'''
Slicing 2-D array :  [7 8 9]
'''