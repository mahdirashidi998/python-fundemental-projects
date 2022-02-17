def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)
def TestSuite():
    test(day_num("friday"), 5)
    test(day_num("sunday"), 0)
    test(day_num(day_name(3)), 3)
    test(day_name(day_num("thursday")), "thursday")
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
def day_name(Number):
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
def day_num(Number):
    if Number=='sunday' :
        return 0
    elif Number=='monday' :
        return 1
    elif Number=='teusday' :
        return   2  
    elif Number=='wednesday' :
        return 3
    elif Number=='thursday' :
        return     4
    elif Number=='friday' :
        return 5
    elif Number=='saturday' :
        return 6
    else :
        x=0
        
TestSuite()
input()



