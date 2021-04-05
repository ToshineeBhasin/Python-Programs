class Mobile:
    def __init__(self,brand,price):
        print("Inside constructor")
        self.brand =  brand
        self.price = price

    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand",self.brand,"and price ",self.price)

print("Mobile 1 ")
mob1 = Mobile("Apple",2000)
mob1.purchase()

print("Mobile 2 ")
mob2 = Mobile("Samsung",1500)
mob2.purchase()