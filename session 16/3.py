
class Point:
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
    def  contains(self,point):
        self.p = point
        if (self.p.x >= self.corner.x and self.p.x < self.corner.x + self.width) and (self.p.y >= self.corner.y and self.p.y < self.height):
            return True
        return False
def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,b,a)
    print(msg)
def TestSuite():
    test(r.contains(Point(0, 0)), True)
    test(r.contains(Point(3, 3)), True)
    test(r.contains(Point(3, 7)), False)
    test(r.contains(Point(3, 5)), False)
    test(r.contains(Point(3, 4.99999)), True)
    test(r.contains(Point(-3, -3)), False)
r=Rectangle(Point(0,0),10,5)
TestSuite()