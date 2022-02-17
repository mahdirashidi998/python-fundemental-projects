def rel_prime(s,n):
    s=int(s)
    n=int(n)
    count=0
    for i in range(2,max(s,n)+1):
        if s%i==0 and n%i==0 :
            count=1
        if count==0 :
            return str(s)
def asli(string,num):
    ls=''
    for i in string :
        if rel_prime(i,num)!=None and rel_prime(i,num)!='1':
            ab=rel_prime(i,num)
            ls=ls+ab
    print(ls,end='')
list=input()
num=input()
asli(list,num)

