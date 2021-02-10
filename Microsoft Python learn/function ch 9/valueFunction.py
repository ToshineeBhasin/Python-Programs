value = 1
def func():
    value = 10
    print('Value inside function : ',value)
    #return 10

print('Value outside function : ',value)
func()

'''
Value outside function :  1
Value inside function :  10
'''
