def  test(a,b):
    import sys
    line_number=sys._getframe(1).f_lineno
    if a==b:
        print('the test in line {0} passed'.format(line_number))
    else:
        print('the tet in line {0} failed. we expected {1} but we got {2}'.format(line_number,b,a))
def  test_suite():
    test(add_vectors([1, 1], [1, 1]), [2, 2])
    test(add_vectors([1, 2], [1, 4]), [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]), [2, 6, 4])
def add_vectors(a,b):
    sum_l=[]
    for i in range(len(a)):
        sum_l.append(a[i]+b[i])
    return sum_l
test_suite()
