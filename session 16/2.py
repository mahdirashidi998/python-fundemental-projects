class point:
    def  __init__(self,x,y):
        self.x=x
        self.y=y
class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    def  area(self):
        return (self.width * self.height)
    def  perimeter(self):
        return (self.width * 2 + self.height * 2)
    def flip(self):
        self.height,self.width = self.width,self.height
abbas=Rectangle(point(3,3),5,3)
print(abbas.area())
print(abbas.perimeter())