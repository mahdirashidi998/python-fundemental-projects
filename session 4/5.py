import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('lightgreen')
t.color('blue')
t.pensize(1)
def draw_poly(sz) :
    a=0
    while True :
        for i in ['blue','red','brown','white','hotpink'] :
                wn.bgcolor(i)
                t.color(i)
                t.forward(sz+a)
                t.left(90)
                t.forward(sz+a)
                a=a+2


draw_poly(1)

        
        









        
