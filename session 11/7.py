def  test(a,b):
    import sys
    line_number=sys._getframe(1).f_lineno
    if a==b:
        print('the test in line {0} passed'.format(line_number))
    else:
        print('the tet in line {0} failed. we expected {1} but we got {2}'.format(line_number,b,a))
def  test_suite():
    test(dot_product([1, 1], [1, 1]), 2)
    test(dot_product([1, 2], [1, 4]), 9)
    test(dot_product([1, 2, 1], [1, 4, 3]), 12)
def add_vectors(a,b):
    sum_l=[]
    for i in range(len(a)):
        sum_l.append(a[i]+b[i])
    return sum_l
def  scalar_mult(s, v):
    sum_l=[]
    for i in range(len(v)):
        sum_l.append(s*v[i])
    return sum_l
def  dot_product(a, b):
    sum_l=0
    for i in range(len(a)):
        sum_l=sum_l + a[i]*b[i]
    return sum_l


    
test_suite()
