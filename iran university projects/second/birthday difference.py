def days_in_month(DayName) :
    if DayName=='January':
        return 31
    elif DayName =='February' :
        return 31
    elif DayName =='March' :
        return 31        
    elif DayName =='April' :
        return 31
    elif DayName =='May' :
        return 31
    elif DayName =='June' :
        return 31
    elif DayName =='July' :
        return 30
    elif DayName =='Augest' :
        return 30
    elif DayName =='September' :
        return 30
    elif DayName =='October' :
        return 30
    elif DayName =='November' :
        return 30
    elif DayName =='December' :
        return 30
def days_in_monthNum(DayName) :
    if DayName==1:
        return 31
    elif DayName ==2 :
        return 31
    elif DayName ==3 :
        return 31        
    elif DayName ==4 :
        return 31
    elif DayName ==5 :
        return 31
    elif DayName ==6 :
        return 31
    elif DayName ==7 :
        return 30
    elif DayName ==8 :
        return 30
    elif DayName ==9 :
        return 30
    elif DayName ==10 :
        return 30
    elif DayName ==11 :
        return 30
    elif DayName ==12 :
        return 30
def BDays(FDate,LDate):
    AllDay=0
    for i in range(FDate[0],LDate[0]+1):
        AllDay=AllDay+days_in_monthNum(i)
    AllDay=AllDay-FDate[1]-(days_in_monthNum(LDate[0])-LDate[1])
    print(AllDay)
FDate=list(map(int,input().split()))
LDate=list(map(int,input().split()))
BDays(FDate,LDate)