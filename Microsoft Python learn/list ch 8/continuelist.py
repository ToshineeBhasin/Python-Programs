values = ["laptop", 7, "phone", 3 ,"dslr", 5]
equipment = []

for value in values:
    if isinstance(value, str) == False:
        continue
    equipment.append(value)

print(equipment)
'''
['laptop', 'phone', 'dslr']
'''