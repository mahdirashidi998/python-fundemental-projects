def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)
def TestSuite():
    test(Day(3), "wednesday")
    test(Day(6), "saturday")
    test(Day(42), None)
def turn_clockwise(O):
    if O=='N' :
        return 'E'
    elif O=='E' :
        return 'S'
    elif O=='S' :
        return 'W'
    elif O=='W' :
        return 'N'
    else :
        x=0
def Day(Number):
    if Number==0 :
        return 'sunday'
    elif Number==1 :
        return 'monday'
    elif Number==1 :
        return 'teusday'    
    elif Number==3 :
        return 'wednesday'
    elif Number==4 :
        return 'thursday'    
    elif Number==5 :
        return 'friday'
    elif Number==6 :
        return 'saturday'
    else :
        x=0
TestSuite()
input()



