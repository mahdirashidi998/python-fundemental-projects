import sys
import os
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
def  pathlist(path):
    lis1 = os.listdir(path)
    lis2=[]
    for i in lis1:
        if os.path.isdir(path + '\\'+i):
            lis2.append(path+'\\'+i)
            path2 = path + '\\' + i
            lis2.extend(pathlist(path2))
            lis2.sort()
    return lis2
def  litter(path):
    lis = pathlist(path)
    for i in lis:
        a = open(i +'\\'+ 'trash.txt','w')
        a.close()

def  remove(path):
    lis = pathlist(path)
    for i in lis:
        try:
            os.remove(i +'\\'+ 'trash.txt')
        except:
            pass
        
remove('C:\\Users\\sepehr\\OneDrive\\datas\\python programing\\book\\questions')


