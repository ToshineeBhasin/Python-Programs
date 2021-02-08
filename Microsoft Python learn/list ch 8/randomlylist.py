import random
numbers = [42,77,16,101,23,8,4,15,55]
selected_number = random.choice(numbers)
print(selected_number)

selected_number = random.choices(numbers, k=3)
print(selected_number)
'''
23
[77, 101, 15]
'''