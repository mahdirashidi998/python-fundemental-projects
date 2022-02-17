def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)
test(5,6)
input()

def TestSuite():
    test(1,1)
