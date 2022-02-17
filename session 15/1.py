class point:
    def  __init__(self,x,y):
        self.x=x
        self.y=y
    def  distance(self,p):
       a = ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) **0.5
       return a
p = point(1,1)
q = point(0,0)
print(p.distance(q))



