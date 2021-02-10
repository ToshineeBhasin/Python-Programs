def print_args(*args):              #tuple is passed as arguments
    for arg in args:
        print(f'arg = {arg}')
    print(type(args))

print_args('a')
print_args('a','b')
print_args('a','b','c')
'''
arg = a
<class 'tuple'>
arg = a
arg = b
<class 'tuple'>
arg = a
arg = b
arg = c
<class 'tuple'>
'''

