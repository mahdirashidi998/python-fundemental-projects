def distance(x,y):
    a=((x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2)**0.5
    print('%.2f'%a)
x=list(map(float,input().split()))
y=list(map(float,input().split()))
distance(x,y)
