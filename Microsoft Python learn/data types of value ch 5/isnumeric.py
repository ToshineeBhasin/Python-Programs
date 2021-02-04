first_value = input('First number :')
if first_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

second_value = input('Second number :')
if second_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum : ' + str(sum))
'''
First number :3
Second number :3
Sum : 6
'''