
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
    test(num_even_digits(123456), 3)
    test(num_even_digits(2468), 4)
    test(num_even_digits(1357), 0)
    test(num_even_digits(0), 1)
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
def sqrt(n):
    approx = n/2.0 # start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            break
        approx = better
    return better
def  print_triangular_numbers(n):
    store=0
    for i in range(n+1):
        if i>0:
            store=store+i
            print(i,'\t',store)
def  is_prime(n):
    count=0
    for i in range(2,int(n/2+1)):
        if (n)%(i+1)==0:
            count+=1
    return count==0
def drunk_stu(list):
    import turtle as t
    al=t.Turtle()
    for i,j in list :
        al.left(i)
        al.forward(j)
def  sum_of_squares(list) :
    sum=0
    for i in list :
        sum=sum+i**2
    return sum
def  num_even_digits(n):
    num=0
    a=1
    for i in range(n+1):
        if n==0:
            return 1
        else :
            b=n//a
            a=a*10
            if b%2==0:
                num=num+1
            if b==0 :
                break
    return num-1
test_suite()
        


        

