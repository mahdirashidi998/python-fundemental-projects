def Day(Number,Dayspend):
    Number=(Number+Dayspend%7)%7
    if Number==0 :
        return 'sunday'
    elif Number==1 :
        return 'monday'
    elif Number==1 :
        return 'teusday'    
    elif Number==3 :
        return 'wednesday'
    elif Number==4 :
        return 'thursday'    
    elif Number==5 :
        return 'friday'
    elif Number==6 :
        return 'saturday'    
print(Day(3,138))
input()