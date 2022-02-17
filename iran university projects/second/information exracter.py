alfabet='abcdefghijklmnopqrstuvwxyz.0123456789'
ALFABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def  email(syntax):
    '''it has bug when the letter before email gets . or numbers'''
    global alfabet , ALFABET
    count=0
    com=syntax.find('.com')
    for i in range(com-1,0,-1):
        if syntax[i] not in (alfabet or ALFABET) and count<=1:
            if syntax[i]=='@' :
                count+=1
                continue
            print(syntax[i+1:com+4])
            break
def number(syntax):
    a09=syntax.find('09')
    print(syntax[a09:a09+11])
def ID(syntax):
    num='0123456789'
    ID=syntax.find('ID')
    for i in range(ID,len(syntax)):
        if syntax[i] in num :
            for s in range(i,len(syntax)):
                if syntax[s] not in num :
                    print(syntax[ID:s])
                    return
syntax=input()                
email(syntax)
number(syntax)
ID(syntax)
