import turtle
wn=turtle.Screen()
alex=turtle.Turtle()
alex.speed(10)
a=0
for i in [160, -43, 270, -97, -43, 200, -940, 17, -86] :
    alex.left(i)
    alex.forward(100)
    a+=i

print(a)

input()
