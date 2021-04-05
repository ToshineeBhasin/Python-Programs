class Mobile:
    def __init__(self):
        print("Inside the mobile constructor")
        self.brand = None
        brand = "Apple"
    '''
    This is a local variable.variables without self are local and thet dont affect the attributes.

    Local variables cannot be accessed outside
    the init using self creates attributes which are
    accessible in other methods as well.
    '''

mob1 = Mobile()
print(mob1.brand)

'''
This does not print Apple. This prints None because brand=Apple creates a local variable and it does not affect the attribute.
'''




'''
Output:
Inside the mobile constructor
None
'''