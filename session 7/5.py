
def  count_odd_numbers(list):
    count=0
    for i in list :
        if i%2==1:
            count+=1
    return count
def  sum_even_numbers(list) :
    sum=0
    for i in list :
        if i%2==0 :
            sum+=i
    return sum
def  sum_negetive_numbers(list) :
    sum=0
    for i in list :
        if i<0 :
            sum+=i
    return sum
def  count_5lengh_words(list) :
    count=0
    for i in list :
        if len(i)==5 :
            count+=1
    return count
def  test(returned,expected) :
    import sys
    line_num=sys._getframe(1).f_lineno
    if returned==expected :
        print('test in line {0} passed'.format(line_num))
    else :
        print('test in line {0} failed. we expected {1} but we got {2}'.format(line_num,expected,returned))
def  test_suite() :
    test(add_exept_first_even([1,2,3,4]),9)
    test(add_exept_first_even([2,4,6]),12)
def  add_exept_first_even(list) :
    sum=0
    a=0 
    for i in list :   
        if a!=1 and i%2==1 :
            a=1
            continue
        sum+=i
    return sum 
def  sam_count(list) :
    count1=0
    count=0
    for i in list :
        count1+=1
        if i=='sam' :
            count=len(list)-count1+1
            break
    return count
print(sam_count(['a','b','al','c','d']))

        

