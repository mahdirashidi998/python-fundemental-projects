def  nice_sym(n):
    if int(n[0])+int(n[2])==int(n[1]):
        return True
    else :
        return False
def  reverse(a):
    s=''
    for i in range(len(a)):
        s=s+a[-i-1]
    return s
def  half1_sym(m):
    m=str(m)
    for i in range(len(m)-2):
        if nice_sym(m[i:i+3]) :
            return True
    return False
def  half2_sym(l):
    l=str(l)
    if len(l)%2==0:
        if l[:int((len(l)/2))]==reverse(l[int((len(l)/2)):]):
            return True
    elif len(l)%2==1:
        a=int(((len(l)-1)/2))
        b=int((len(l)+1)/2)
        if l[:a]==reverse(l[b:]):
            return True
    return False
def full_sym(p):
    if half1_sym(p) and half2_sym(p) :
        return True
    return False
def  asli(F,L):
    count1=0
    count2=0
    for i in range(int(F),int(L)+1):
        if half1_sym(i):
            count1+=1
        if full_sym(i) :
            count2+=1
    print(count1)
    print(count2)
F=input()
L=input()
asli(F,L)
