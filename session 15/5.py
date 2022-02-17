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
    def  get_line_to(self,q):
        a = (self.y - q.y) / (self.x - q.x)
        b=self.y - a * self.x
        return (a,b)
p = point(2,2)
q = point(3,4)
a=p.get_line_to(q)
print(a)




