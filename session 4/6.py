def draw_poly(t,n,sz) :
    import turtle
    t=turtle.Turtle()
    wn=turtle.Screen()
    wn.bgcolor('lightgreen')
    t.color('hotpink')
    t.pensize(4)
    Angle=180-((180*(n-2))/n)
    for i in range(n):
        t.forward(sz)
        t.left(Angle)
def draw_equitriangle(t, sz) :
    draw_poly(t,3,sz)
draw_equitriangle('x',100)
        
        









        
