first_num = 5
second_num = 0
true_value = True
false_value = False

if first_num > 1 and first_num < 10:
    print("The value is between 1 and 10 : ")

if first_num > 1 or second_num > 1:
    print("At least one value is greater than 1")

print(not true_value)
print(not false_value)

if not first_num > 1 and second_num < 10:
    print("Both values pass the test")
else:
    print("Both values do not pass the test ")

'''
The value is between 1 and 10 :
At least one value is greater than 1
False
True
Both values do not pass the test
'''