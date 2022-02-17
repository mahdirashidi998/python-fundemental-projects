
def grade(Number):
    for i in  Number :
        if i>=75 :
            a= 'First'
        elif i>=70 and i<75 :
            a= 'Upper second'
        elif i>=60 and i<70 :
            a= 'second'    
        elif i>=50 and i<60 :
            a= 'third'
        elif i>=45 and i<50 :
            a= 'F1 supp'    
        elif i>=40 and i<45 :
            a= 'F2'
        elif i<40 :
            a= 'F3'
        print(a) 
b=[83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0] 
grade(b)    
 
input()