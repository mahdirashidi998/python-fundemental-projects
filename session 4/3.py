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
draw_poly('tess',8,50)
        
        









        
