def  readposint(n):
    myerror = ValueError('ridi amu avaz kon')
    try:
        if type(n) != type(3) or n < 0 :
            raise myerror
        print('ahsant')
    except :
        print('ridi amu avaz kon')
readposint(4.5)
        
