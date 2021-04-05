class Mobile:
    def __init__(self,price,brand):
        print("Id of self in constructor",id(self))
        self.price = price
        self.brand = brand

mob1 = Mobile(10000,"iphone")
print("Id of mob1 in driver code ",id(mob1))

mob2 = Mobile(20000,"Samsung")
print("Id of mob2 in driver code ",id(mob2))
'''
output:
Id of self in constructor 28371000
Id of mob1 in driver code  28371000
Id of self in constructor 28967840 
Id of mob2 in driver code  28967840
'''