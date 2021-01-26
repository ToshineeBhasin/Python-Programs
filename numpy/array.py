import numpy as np

b = np.array([1,2,3,4,5])
print("1-d array : ",b)
a = np.array([(1,2,3),(4,5,6)])
print("2-d array : ",a)

'''
why numpy over list??
1. occupy less space
2. easy to work with it
3. fast
'''
myarr =  np.array([[3,6,75,7]],np.int64)
print(myarr[0,1])       #6 is the output

# 5 ways to create numpy array
# conversion from other python structures i.e. list,tuples
listarray = np.array([[1,2,3],[5,8,5],[0,3,1]])
print(listarray)
print("List array dtype : ",listarray.dtype)
print("List array shape : ",listarray.shape)
print("List array size : ",listarray.size)
'''
List array dtype :  int32
List array shape :  (3, 3)
List array size :  9
'''
zeros = np.zeros((2,5))
print("Zeros matrix : ")
print(zeros)
print("Zero matrix dtype : ",zeros.dtype)
print("zero matrix shape : ",zeros.shape)
print("Size of zero matrix : ",zeros.size)

'''
Zeros matrix :
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
Zero matrix dtype :  float64
zero matrix shape :  (2, 5)
Size of zero matrix :  10
'''

#arange function (numpy array )
rng = np.arange(15)
print(rng)          #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

#below function print  12 equally linear space elements between 1 to 5 
lspace = np.linspace(1,5,12)
print(lspace)
'''
[1.         1.36363636 1.72727273 2.09090909 2.45454545 2.81818182
 3.18181818 3.54545455 3.90909091 4.27272727 4.63636364 5.        ]
'''

#empty array
emp = np.empty((4,6))
print("empty array : ")
print(emp)
'''
empty array :
[[6.23042070e-307 4.67296746e-307 1.69121096e-306 1.69120688e-306
  9.34605716e-307 1.06808027e-306]
 [1.33511562e-306 1.42419938e-306 7.56603881e-307 8.45603440e-307
  3.56043054e-307 1.60219306e-306]
 [6.23059726e-307 1.06811422e-306 3.56043054e-307 1.37961641e-306
  8.06613040e-308 1.24610383e-306]
 [1.69118108e-306 8.06632139e-308 1.20160711e-306 1.69119330e-306
  1.29062229e-306 3.91792476e-317]]

'''

# empty like function
emp_like = np.empty_like(lspace)
print(emp_like)
'''
[1.         1.36363636 1.72727273 2.09090909 2.45454545 2.81818182
 3.18181818 3.54545455 3.90909091 4.27272727 4.63636364 5.        ]
 '''

 #identity matrix
ide = np.identity(5)
print("Identity Matrix : ",ide)
print(ide.shape)            #(5,5)
print(ide.size)             #25
print(ide.dtype)            #float64
'''
Identity Matrix :  
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
 '''

#reshape function
arr = np.arange(99)
print(arr)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98]
 '''
#reshape given matrix
a = arr.reshape(3,33)
print(a)
'''
[[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
  24 25 26 27 28 29 30 31 32]
 [33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
  57 58 59 60 61 62 63 64 65]
 [66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89
  90 91 92 93 94 95 96 97 98]]
  '''

b = arr.reshape(9,11)
print(b)
print(b.shape)          #(9,11)
'''
[[ 0  1  2  3  4  5  6  7  8  9 10]
 [11 12 13 14 15 16 17 18 19 20 21]
 [22 23 24 25 26 27 28 29 30 31 32]
 [33 34 35 36 37 38 39 40 41 42 43]
 [44 45 46 47 48 49 50 51 52 53 54]
 [55 56 57 58 59 60 61 62 63 64 65]
 [66 67 68 69 70 71 72 73 74 75 76]
 [77 78 79 80 81 82 83 84 85 86 87]
 [88 89 90 91 92 93 94 95 96 97 98]]
 '''

#ravel function to again reshape the matrix to original one
c = b.ravel()
print(c)
print(c.shape)          #(99,)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98]
 '''

#axis
ax = [[1,2,3],[4,5,6],[7,8,9]]
axis_arr = np.array(ax)
print(axis_arr)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 '''
print(axis_arr.sum(axis=0))         #[12 15 18] addition of elements of array according to x axis
print(axis_arr.sum(axis=1))         #[ 6 15 24] addition of elements of array according to y axis

#transpose matrix
print("Transpose of matrix : ",axis_arr.T)
'''
Transpose of matrix :  [[1 4 7]
                        [2 5 8]
                        [3 6 9]]
'''
