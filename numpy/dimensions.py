# 0 - Dimensional array
import numpy as np
arr =  np.array(42)
print("0 - Dimensional array : ",arr)
'''
0 - Dimensional array :  42
'''
arr = np.array([1,2,3,4,5])
print("1 -  Dimenionsal array : ",arr)
'''
1 -  Dimenionsal array :  [1 2 3 4 5]
'''
arr = np.array(([1,2,3],[4,5,6]))
print("2 - Dimensional array : ",arr)
'''
2 - Dimensional array :  [[1 2 3]
                         [4 5 6]]
 '''
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("creating a 3-D array with two 2-d array,both containing two arrays with the values 1,2,3 and 4,5,6 :",arr)
'''
creating a 3-D array with two 2-d array,both containing two arrays with the values 1,2,3 and 4,5,6 : [[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
  '''