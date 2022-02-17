def alarmy(CT,WT) :
    remained=WT%24
    result=(CT+remained)%24
    print(result)
a=input('what time is it? ')
a=int(a)
b=int(input('how much you want to wait? '))
alarmy(a,b)
input()
