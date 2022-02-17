class point:
    def  __init__(self,x,y):
        self.x=x
        self.y=y
    def  distance(self,p):
       a = ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) **0.5
       return a
    def  reflect(self):
        return point(self.x,-self.y)
    def  slope_from_origin(self):
        a = self.y / self.x
        return a

p = point(2,2)
q = point(0,0)
a=p.slope_from_origin()
print(a)




