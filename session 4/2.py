import turtle 
wn=turtle.Screen()
alex=turtle.Turtle() 
a=20
b=20
wn.bgcolor('lightgreen')
alex.color('hotpink')
alex.pensize(3)
def square(sz) :
    for i in range (4) :
        alex.forward(sz)
        alex.left(90)
    alex.penup()
    alex.forward(-20)
    alex.right(90)
    alex.forward(20)
    alex.left(90)
    alex.pendown()
for i in [1,2,3,4,5] :
    square(b)
    b=(2*i+1)*a







        
