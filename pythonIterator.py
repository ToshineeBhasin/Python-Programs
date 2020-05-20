'''
Created on 20-May-2020

@author: Toshinee Bhasin
'''
'''
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you 
can traverse through all the values. Technically, in Python, an iterator 
is an object which implements the iterator protocol, which consist of the
methods __iter__() and __next__().

'''

mytuple = ("Toshi", "Teena", "Sunny")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
'''
output:
Toshi
Teena
Sunny
'''
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

'''
output:
b
a
n
a
n
a
'''

#Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

'''
output:
apple
banana
cherry
'''

mystr = "banana"

for x in mystr:
    print(x) 
    
'''
output:
b
a
n
a
n
a
'''
    
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))   
'''
output:
1
2
3
4
5 
'''  
    
    
    
    
    
    
    
    
    
    
       
    


