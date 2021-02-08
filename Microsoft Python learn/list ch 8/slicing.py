colors = ['red','blue','yellow','green','orange','purple','black','brown']

print('Print a slice , starting at index 2 and excluding index 5 : ')
print(colors[2:5])
print(type(colors[2:5]))
'''
Print a slice , starting at index 2 and excluding index 5 : 
['yellow', 'green', 'orange']
<class 'list'>
'''
print('Print a slice, starting at index 0 to index 3:')
print(colors[:3])

print('Print a slice, starting a index 4 to the end of the list : ')
print(colors[4:])

print('Print a slice, from the 4th from the end (but not the last item) : ')
print(colors[-4:-1])

'''
Print a slice, starting at index 0 to index 3:
['red', 'blue', 'yellow']
Print a slice, starting a index 4 to the end of the list :
['orange', 'purple', 'black', 'brown']
Print a slice, from the 4th from the end (but not the last item) :
['orange', 'purple', 'black']
'''

colors.reverse()
print(colors)
'''
['brown', 'black', 'purple', 'orange', 'green', 'yellow', 'blue', 'red'] 
'''

colors.sort()
print(colors)
'''
['black', 'blue', 'brown', 'green', 'orange', 'purple', 'red', 'yellow'] 
'''