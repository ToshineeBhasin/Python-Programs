'''
The next technique uses the isinstance() function, which allows you to assert that you expect a value to be a certain data type.
'''

print(type('7'))
print(type(7))
print(type(7.1))
'''
<class 'str'>
<class 'int'>
<class 'float'>
'''

print(isinstance('7',str))
print(isinstance(7,int))
print(isinstance(7.1,float))
'''
True
True
True
'''

print(isinstance(7,str))
print(isinstance('7', int))
print(isinstance('7.1', float))
'''
False
False
False
'''

print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)
'''
True
True
True
False
False
False
'''

x = 'a string'
print(type(x))
x = 7
print(type(x))
x = False 
print(type(x))
'''
<class 'str'>
<class 'int'>
<class 'bool'>
'''

value = '7'
print(value.isnumeric())            #true

str_value = 'Toshi'
print(str_value.isnumeric())        #false


