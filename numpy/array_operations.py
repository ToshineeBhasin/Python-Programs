import numpy as np
a = np.array([[1,2],[3,4]])
print("Array 1 :",a)
b = np.array([[5,6],[7,8]])
print("Array 2 :",b)
print("Addition of 2 array : ",a+b)
'''
Array 1 : [[1 2]
            [3 4]]
Array 2 : [[5 6]
            [7 8]]
Addition of 2 array :  [[ 6  8]
                        [10 12]]
 '''

a = np.array([[5,6],[7,8]])
b = np.array([[1,2],[3,4]])
print("Subtraction of 2 array : ",a-b)
'''
Array 1 : [[1 2]
            [3 4]]
Array 2 : [[5 6]
            [7 8]]
Addition of 2 array :  [[ 6  8]
                        [10 12]]
Subtraction of 2 array :  [[4 4]
                            [4 4]]
 '''

a = np.array([[5,6],[7,8]])
b = np.array([[1,2],[3,4]])
print("Multiplication of 2 array : ",a*b)
'''
Multiplication of 2 array :  [[ 5 12]
                              [21 32]]
'''

#Addition of 2 arrays
a = np.array([[5,6],[7,8]])
b = np.array([[1,2],[3,4]])
Sum = np.add(a,b)
print("Addition of 2 arrays using add() : ")
print(Sum)
'''
Addition of 2 arrays using add() :
[[ 6  8]
 [10 12]]
 '''

#Squareroot function
Sqrt = np.sqrt(a)
print("Square root of elements of 1st array : ")
print(Sqrt)
'''
Square root of elements of 1st array :
[[2.23606798 2.44948974]
 [2.64575131 2.82842712]]
 '''