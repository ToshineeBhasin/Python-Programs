class Mobile:
    def __init__(self,price,brand):
        print(id(self))
        self.price= price
        self.brand=brand

    def return_product(self):
        print(id(self))
        print("Brand being returned is ",self.brand," and price is ",self.price)

mob1 = Mobile(20000,"iphone")
print("Mobile 1 has id ",id(mob1))

mob2 = Mobile(15000,"Samsung")
print("Mobile 2 has id ",id(mob2))

mob2.return_product()
Mobile.return_product(mob1)
'''
12642360
Mobile 1 has id  12642360
21890168
Mobile 2 has id  21890168
21890168
Brand being returned is  Samsung  and price is  15000
12642360
Brand being returned is  iphone  and price is  20000
'''