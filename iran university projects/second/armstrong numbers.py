def  armstrong(n): 
    i=len(n)
    a=0
    for j in n:
        a+=int(j)**i
    if int(n)==a :
        return (int(n))
    return     
def  asli(a,b):
    count=0
    for i in range(a,b+1):
        c=str(i)
        if armstrong(c)!=None:
            print(armstrong(c))
            count+=1
    if count==0:
        print('')
a=int(input())
b=(int(input()))
asli(a,b)

