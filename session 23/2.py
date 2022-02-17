import turtle
class TurtleGTX(turtle.Turtle):
    def  jump(self,distance):
        self.penup()
        self.forward(distance)
        self.pendown()
    def  distance(self): 
        
        return (self.pos())
t = TurtleGTX()
t.forward(100)
t.jump(50)
t.forward(100)
print(t.distance())
