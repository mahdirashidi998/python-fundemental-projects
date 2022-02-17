def  test(a,b):
    import sys
    line_number=sys._getframe(1).f_lineno
    if a==b:
        print('the test in line {0} passed'.format(line_number))
    else:
        print('the tet in line {0} failed. we expected {1} but we got {2}'.format(line_number,b,a))
def  test_suite():
    test(scalar_mult(5, [1, 2]), [5, 10])
    test(scalar_mult(3, [1, 0, -1]), [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]), [21, 0, 35, 77, 14])
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

    
test_suite()
