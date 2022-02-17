import turtle
t = turtle.Turtle()
def  draw(t,order,size):
    if order == 0:
        t.forward(size)
    else:
        draw(t,order-1,size/3)
        t.left(60)
        draw(t, order-1, size/3)
        t.right(120)
        draw(t, order-1, size/3)
        t.left(60)
        draw(t, order-1, size/3)
for i in range(3):
    draw(t,2,400)
    t.right(120)