'''
Python map() function
map() function returns a map object(which is an iterator) of the results 
after applying the given function to each item of a given 
iterable (list, tuple etc.)

Syntax :

map(fun, iter)

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
'''

#python program to demonstrate working of map
def addition(n):
    return n+n

numbers=(1,2,3,4)
result=map(addition,numbers)
print(list(result))

#output: [2, 4, 6, 8]

# Double all numbers using map and lambda 
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 

#output: [2, 4, 6, 8]

# Add two lists using map and lambda 
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 

result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 

#output: [5, 7, 9]

# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 

#output: [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]


































