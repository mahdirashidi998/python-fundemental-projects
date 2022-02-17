import turtle
t = turtle.Turtle()
def  draw(t,order,size):
    if order == 0:
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
    else:
        draw(t,order-1,size/order+1)
        t.forward(size/order+1)
        draw(t,order-1,size/order+1)
        t.forward(size/order+1)
        draw(t,order-1,size/order+1)
        t.forward(size/order+1)


draw(t,2,50)

