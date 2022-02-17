import turtle
t = turtle.Turtle()
def  draw(t,order,size):
    if order == 0:
        t.forward(size)
    else:
        draw(t,order-1,size/3)
        t.right(85)
        draw(t, order-1, size/3)
        t.left(170)
        draw(t, order-1, size/3)
        t.right(85)
        draw(t, order-1, size/3)
draw(t,3,300)