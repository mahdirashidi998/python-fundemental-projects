import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('lightgreen')
t.color('blue')
t.pensize(4)
def draw_poly(n,sz) :
    Angle=180-((180*(n-2))/n)
    for i in range(n):
        t.forward(sz)
        t.left(Angle)
    t.left(360/20)
for i in range (20) :
    draw_poly(4,200)

        
        









        
