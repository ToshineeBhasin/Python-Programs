print("Simple Calculator !")

first = input("Enter first number : ")

if first.isnumeric() == False:
    print("Please input a number.")
    exit()

op = input("Operation ?  ")

second = input("Enter second number : ")
if second.isnumeric() == False:
    print("Please input a number.")
    exit()

first = int(first)
second = int(second)

res = 0
if op == '+':
    res = first + second
    label = 'Sum'
elif op == '-':
    res = first - second
    label = 'Difference'
elif op == '*':
    res = first * second
    label = 'Multiplication'
elif op == '/':
    res = first / second
    label = 'Quotient'
elif op == '%':
    res = first % second
    label = 'Modulus'
elif op == '**':
    res = first ** second
    label = 'Exponent'
else:
    print("Operation not recognised.")
    exit()

print(label + ' of ' + str(first) + ' ' + op +' '+str(second)+  ' equals ' + str(res))

'''
Simple Calculator !
Enter first number : 2
Operation ?  +
Enter second number : 2
Sum of 2 + 2 equals 4
or
Simple Calculator !
Enter first number : tosh
Please input a number.
'''
