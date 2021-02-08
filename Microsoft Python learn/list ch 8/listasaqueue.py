colors = ['red','blue','yellow','green','orange','purple','black','brown']

print(colors)

color = colors.pop(0)
print('popped',color)
print(colors)
'''
['red', 'blue', 'yellow', 'green', 'orange', 'purple', 'black', 'brown']    
popped red
['blue', 'yellow', 'green', 'orange', 'purple', 'black', 'brown']
'''

colors.append('red')
colors.append('white')
print(colors)
'''
['blue', 'yellow', 'green', 'orange', 'purple', 'black', 'brown', 'red', 'white']
'''