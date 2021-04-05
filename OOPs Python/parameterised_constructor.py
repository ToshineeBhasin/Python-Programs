#If a constructor takes parameter then it would be #called as parameterized constructor
class Mobile:
    def __init__(self,brand,price):
        print("Inside Constructor")
        self.brand = brand
        self.price = price

mob1 = Mobile("Apple",20000)
print("Mobile ! has brand",mob1.brand,"and price",mob1.price)

mob2 = Mobile("Samsung",32000)
print("mobile 2 has brand",mob2.brand,"and price",mob2.price)
'''
Output:
Inside Constructor
Mobile ! has brand Apple and price 20000  
Inside Constructor
mobile 2 has brand Samsung and price 32000
'''