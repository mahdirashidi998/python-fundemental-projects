import turtle # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
yess=turtle.Turtle()
uess=turtle.Turtle()
yess.hideturtle()
uess.hideturtle()
yess.penup()
uess.penup()
def draw_housing():
    ''' Draw a nice housing to hold the traffic lights '''
    tess.pensize(3)
    tess.color('black', 'darkgrey')
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
draw_housing()
tess.penup()
# Position Tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape('circle')
tess.shapesize(3)
tess.fillcolor('green')
# Position Tess onto the place where the green light should be
yess.forward(40)
yess.left(90)
yess.forward(50)
# Turn tess into a big green circle
yess.shape('circle')
yess.shapesize(3)
yess.fillcolor('green')
# Position Tess onto the place where the green light should be
uess.forward(40)
uess.left(90)
uess.forward(50)
# Turn tess into a big green circle
uess.shape('circle')
uess.shapesize(3)
uess.fillcolor('green')
# Position Tess onto the place where the green light should be
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
tess.fillcolor('black')
yess.forward(70)
yess.fillcolor('black')
uess.forward(140)
uess.fillcolor('black')
state_num = 0
def advance_state_machine():
    global state_num
    if state_num == 0: # transition from state 0 to state 1
        wn.ontimer(tess.fillcolor('green'),1000)
        tess.fillcolor('black')
        state_num = 1
        
    elif state_num == 1: # transition from state 1 to state 2
        wn.ontimer(yess.fillcolor('yellow'),1000)
        yess.fillcolor('black')
        state_num = 2
        
    else: # transition from state 2 to state 0
        wn.ontimer(uess.fillcolor('red'),1000)
        uess.fillcolor('black')
        state_num = 0
    advance_state_machine()
    

# bind the event handler to the space key.
advance_state_machine()
wn.mainloop()