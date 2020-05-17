import turtle
#to print square without functiom

toshi=turtle.Screen()
toshi_turtle=turtle.Turtle()
toshi_turtle.forward(100)
toshi_turtle.right(90)
toshi_turtle.forward(100)
toshi_turtle.right(90)
toshi_turtle.forward(100)
toshi_turtle.right(90)
toshi_turtle.forward(100)
toshi_turtle.right(90)

#to print star without function

star = turtle.Turtle() 
star.forward(50) 
star.right(144) 
star.forward(50) 
star.right(144) 
star.forward(50) 
star.right(144) 
star.forward(50) 
star.right(144) 
star.forward(50) 
star.right(144) 


#Square with function
toshi=turtle.Turtle()
def square():
    toshi.forward(100)
    toshi.right(90)
    toshi.forward(100)
    toshi.right(90)
    toshi.forward(100)
    toshi.right(90)
    toshi.forward(100)
    #toshi.right(90)
    
square()
toshi.forward(50)
square()
toshi.forward(50)
square()
toshi.forward(50)
square()
    
