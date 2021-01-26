import numpy as np
x = np.array([1,0,0,0])
print("1st array : ",x)
print("Test whether any of the elements of a given array is non-zero :")
print(np.any(x))

x1 = np.array([0,0,0,0])
print("2nd array : ",x1)
print("Test whether any of the elements of a given array is non-zero :")
print(np.any(x1))
'''
1st array :  [1 0 0 0]
Test whether any of the elements of a given array is non-zero :
True
2nd array :  [0 0 0 0]
Test whether any of the elements of a given array is non-zero :
False
'''