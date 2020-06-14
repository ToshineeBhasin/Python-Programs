'''
Created on 13-Jun-2020

@author: Toshinee Bhasin
'''
#data stored in file
shopping_list = ["banana", "orange", "apple","shirts","utensils","curtains","stationary"]

stock = { "banana": 24,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "utensils":56,
    "stationary":45,
    "curtains":33,
    "shirts":52
}

prices = { "banana": 4,
    "apple": 2,
    "orange": 4,
    "pear": 3,
    "utensils":50,
    "stationary":25,
    "curtains":670,
    "shirts":500
}

f=open('grocerylist.txt','w')
for ele in shopping_list:
    f.write(ele+'\n')

for x in stock.items():
    f.write(str(x)+'\n')

for y in prices.items():
    f.write(str(y)+'\n')
f.close()


print("*********  Welcome to Wallmart Store **********")
#print("Available items in stock :")
#print(shopping_list)
#print(stock)
#print(prices)

def shop():
#while True:
    item = input("Enter the item you want to buy : ")
    i = item
    
    if i in shopping_list:
            print("Yes!!! It is available")
            quantity = int(input("How  much quantity you want :"))
            ans=input("Do you want to purchase it (yes/no)?")
            if quantity < stock.get(i):
                    y=stock.get(i)
                    if ans == "yes":
                        print(quantity,"has been purchased.")
                        avail=y-quantity
                        print("Available Quantity is ",avail)       
                        rate= quantity * prices.get(i)
                        print("Price for purchased item is ",rate)
                        exit()
              
            else:
                    print("Available quantity is",stock.get(i))  
                    ans=input("Do you want to purchase it (yes/no)?")
                    if ans == "yes":
                        quantity = int(input("How  much quantity you want :"))
                        print(quantity,"has been purchased.")
                        
                        rate= quantity * prices.get(i)
                        print("Price for purchased item is ",rate)
                        
                            #exit()
                        avail=stock.get(i) - quantity 
                        print("Available Quantity is ",avail)
                        exit()
    else:
            print("Sorry not available.")           
      
      
shop()

  
ans1=input("Any new item you want to buy(yes/no) ???")
if ans1 == "yes":
    shop()

 
