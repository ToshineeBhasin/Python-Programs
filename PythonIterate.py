'''
Created on 25-May-2020

@author: Toshinee Bhasin
'''
'''
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you
can traverse through all the values.Technically, in Python, an iterator
is an object which implements the iterator protocol, which consist of the 
methods __iter__() and __next__().
'''
#Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
'''
output:
apple
banana
cherry
'''
#Strings are also iterable objects, containing a sequence of characters:

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
#Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
'''
output:
apple
banana
cherry
'''
#Iterate the characters of a string:

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
#Create an iterator that returns numbers, starting with 1, 
#and each sequence will increase by one (returning 1,2,3,4,5 etc.):

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
#Stop after 20 iterations:

class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers1()
myiter = iter(myclass)

for x in myiter:
    print(x)
'''
output:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''


















