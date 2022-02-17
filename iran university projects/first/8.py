def  who_eats(n,m) :
    tavan=1
    while tavan*2<=n :
        tavan=tavan*2 
    if n-tavan<=m :
        print('Amirhossein eats kabab')
    else :
        print('Amirhossein eats parsa')
n,m=input().split()
n=int(n)
m=int(m)
who_eats(n,m)

    
