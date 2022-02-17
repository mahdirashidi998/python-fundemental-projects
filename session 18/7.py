def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)

def TestSuite():
    test(flatten([2,9,[2,1,13,2],8,[2,6]]),[2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]),[9,7,1,13,2,8,7,6])
    test(flatten([[9,[7,1,13,2],8],[2,6]]),[9,7,1,13,2,8,2,6])
    test(flatten([['this',['a',['thing'],'a'],'is'],['a','easy']]),['this','a','thing','a','is','a','easy'])
    test(flatten([]), [])

def  count(val,lis):
    tot = 0
    for i in lis:
        if type(i) == type([]):
            tot +=count(val,i)
        elif type(i) ==type(''):
            for j in i:
                if j == val:
                    tot+=1
        else : 
            if i == val :
                tot +=1
    return tot
def  flatten(lis):
    l=[]
    for i in lis:
        if type(i) == type([]):
            l.extend(flatten(i))
        else:
            l.append(i)
    return l 


TestSuite()
