def print_kwargs(**kwargs):
    third  = kwargs.get('third',None)
    if third != None:
        print('third arg = ',third)

print_kwargs(first = 'a')
print_kwargs(first = 'b', second = 'c')
print_kwargs(first = 'd', second = 'e', third = 'f')