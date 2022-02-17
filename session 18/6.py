def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)

def TestSuite():
    test(count(2, []), 0)
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]), 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]), 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]), 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]), 6)
    test(count('a',[['this',['a',['thing','a'],'a'],'is'], ['a','easy']]), 5)

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
TestSuite()
