def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)
def TestSuite():
    test(turn_clockwise("N"), "E")
    test(turn_clockwise("kosW"), None)
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
TestSuite()
input()



