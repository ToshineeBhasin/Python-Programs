import numpy as np
x = np.array([1,2,3,4])
print("1st array : ",x)
print("Test if none of the elements of the 1st array is zero :  ")
print(np.all(x))

x = np.array([0,1,2,3])
print("2nd array : ",x)
print("Test if none of the elements of the 2nd array is zero :  ")
print(np.all(x))
'''
1st array :  [1 2 3 4]
Test if none of the elements of the 1st array is zero :
True
2nd array :  [0 1 2 3]
Test if none of the elements of the 2nd array is zero :
False
'''