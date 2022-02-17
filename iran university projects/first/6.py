def  cos2a(a,b,x,y) :
    import math
    pi=math.pi
    if a==0 :
        first_angle=(pi)/2
    else :
        first_angle=math.atan(b/a)
    if x==0 :
        second_angle=(pi)/2
    else :
        second_angle = math.atan(y/x)
    deg=abs(first_angle-second_angle)
    cos=math.cos(2*deg)
    print('%.2f'% cos)
    
a,b = input().split()
x,y = input().split()
a=int(a)
x=int(x)
b=int(b)
y=int(y)
cos2a(a,b,x,y)