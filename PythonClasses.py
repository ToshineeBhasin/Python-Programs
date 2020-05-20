'''
Created on 20-May-2020

@author: Toshinee Bhasin
'''

'''
#Program to create class in python which has in-built function _init_ from where code starts
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p1=Person("Toshi",23)
print("Name :",p1.name)
print("Age :",p1.age)

Output:
Name : Toshi
Age : 23
'''

'''

#program to create class having function name myfunc

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def myfunc(self):
        print("Hello!!! My name is ",self.name)
        print("My age is ",self.age)
p1=Person("Toshi",22)
p1.myfunc()

output:
Hello!!! My name is  Toshi
My age is  22
'''
'''
#self parameter
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is",self.name)
        
p1=Person("Abhishek",24)
p1.myfunc()

output:
Hello my name is Abhishek

'''





























