def  f_way(tuple):
    import itertools
    s=''
    st=''
    if tuple[0]+tuple[1]>8:
        print('Unreachable destination')
        return
    for i in range(tuple[0]):
        s=s+'R'
    for i in range(tuple[1]):
        s=s+'U'
    for i in set(itertools.permutations(s,tuple[0]+tuple[1])):
        for j in i:
            st=st+j+'-'
        st=st[0:len(st)-1]
        print(st)
        st=''
imp1,imp2=map(int,input().lstrip('(').rstrip(')').split(','))    
f_way((imp1,imp2))


