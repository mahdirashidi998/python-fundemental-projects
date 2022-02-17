def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)
def TestSuite():
    
    test(days_in_month("February"), 28)
    test(days_in_month("December"), 31)
def day_name(Number):
    if Number==0 :
        return 'sunday'
    elif Number==1 :
        return 'monday'
    elif Number==2 :
        return 'tuesday'    
    elif Number==3 :
        return 'wednesday'
    elif Number==4 :
        return 'thursday'    
    elif Number==5 :
        return 'friday'
    elif Number==6 :
        return 'saturday'
    else :
        x=0
def day_num(Number):
    if Number=='sunday' :
        return 0
    elif Number=='monday' :
        return 1
    elif Number=='tuesday' :
        return   2  
    elif Number=='wednesday' :
        return 3
    elif Number=='thursday' :
        return     4
    elif Number=='friday' :
        return 5
    elif Number=='saturday' :
        return 6
    else :
        x=0
def day_add(DayName,DayAdd) :
    FirstDay=day_num(DayName)
    LastDay=(FirstDay+DayAdd)%7
    Dayname=day_name(LastDay)
    return Dayname
def days_in_month(DayName) :
    if DayName=='January':
        return 31
    elif DayName =='February' :
        return 28
    elif DayName =='March' :
        return 31        
    elif DayName =='April' :
        return 30
    elif DayName =='May' :
        return 31
    elif DayName =='June' :
        return 30
    elif DayName =='July' :
        return 31
    elif DayName =='Augest' :
        return 31
    elif DayName =='September' :
        return 30
    elif DayName =='October' :
        return 31
    elif DayName =='November' :
        return 30
    elif DayName =='December' :
        return 31
TestSuite()
input()



