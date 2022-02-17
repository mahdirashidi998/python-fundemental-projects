def test(a,b):
    import sys
    linenum=sys._getframe(1).f_lineno
    if a==b :
        msg='the function in line {0} passed '.format(linenum)
    else :
        msg='the function in line {0} failed. we expected "{1}" but we got "{2}"'.format(linenum,a,b)
    print(msg)
def TestSuite():
    test(is_factor(3, 12), True)
    test(is_factor(5, 12), False)
    test(is_factor(7, 14), True)
    test(is_factor(7, 15), False)
    test(is_factor(1, 15), True)
    test(is_factor(15, 15), True)
    test(is_factor(25, 15), False)
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
def days_in_monthNum(DayName) :
    if DayName==1:
        return 31
    elif DayName ==2 :
        return 28
    elif DayName ==3 :
        return 31        
    elif DayName ==4 :
        return 30
    elif DayName ==5 :
        return 31
    elif DayName ==6 :
        return 30
    elif DayName ==7 :
        return 31
    elif DayName ==8 :
        return 31
    elif DayName ==9 :
        return 30
    elif DayName ==10 :
        return 31
    elif DayName ==11 :
        return 30
    elif DayName ==12 :
        return 31
def to_secs(Hours,Minutes,Secs):
    Total=Hours*3600+Minutes*60+Secs
    Total=int(Total)
    return Total
def hours_in(secs):
    a=int(secs/3600)
    return a
def minutes_in(secs):
    a=int((secs%3600)/60)
    return a
def seconds_in(secs):
    a=secs%60
    return a
def compare(a,b) :
    if a>b :
        return 1
    elif a==b :
        return 0
    elif a<b :
        return -1
def hypotenuse(a,b):
    c=(a**2+b**2)**0.5
    return c
def slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
def is_even(n):
    return n%2==0
def BDays(FDate,LDate):
    AllDay=0
    for i in range(FDate[0],LDate[0]+1):
        AllDay=AllDay+days_in_monthNum(i)
    AllDay=AllDay-FDate[1]-(days_in_monthNum(LDate[0])-LDate[1])
    print('your gross days: ',AllDay)
    AllWeek=AllDay/7
    print('your gross weeks: ',AllWeek)
def is_odd(n):
    return not is_even(n)
def is_factor(a,b):
    return b%a==0
TestSuite()
input()



