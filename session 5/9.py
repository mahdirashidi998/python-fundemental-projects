import turtle
def chart(height):
    t=turtle.Turtle()
    for i in height :
        t.color('red','blue')
        t.begin_fill()
        t.left(90)
        t.forward(i)
        t.right(90)
        t.write('  '+str(i))
        t.forward(40)
        t.right(90)
        t.forward(i)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()

chart([48,117,200,240,160,260,220])


