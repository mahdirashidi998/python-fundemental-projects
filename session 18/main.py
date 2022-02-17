
def  koch(t,order,size):
    if order == 0 :
        t.forward(size)
    else:
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)
        t.right(120)
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)
def  count(lis):
    sum = 0
    for i in lis:
        if type(i) == type([]):
            sum+=count(i)
        else:
            sum += i
    return sum
def  r_max(lis):
    tot = 0
    for i in lis:
        if type(i) == type([]):
            if r_max(i) > tot:
                tot = r_max(i)
        else :
            if i > tot:
                tot = i
    return tot
print(r_max([1,2,[3,[4,9],6],7]))