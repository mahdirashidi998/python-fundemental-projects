def  test(a,b):
    import sys
    line_number=sys._getframe(1).f_lineno
    if a==b:
        print('the test in line {0} passed'.format(line_number))
    else:
        print('the tet in line {0} failed. we expected {1} but we got {2}'.format(line_number,b,a))
def  test_suite():
    test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
    s = 'I love spom! Spom is my favorite food. Spom, spom, yum!'
    test(replace(s, 'om', 'am'),'I love spam! Spam is my favorite food. Spam, spam, yum!')
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
def  replace(s, old, new):
    s=s.replace(old,new)
    return s
def make_empty(seq): 
    seq=seq.clear()
def insert_at_end(val, seq): pass
def insert_in_front(val, seq): pass
def index_of(val, seq, start=0): pass
def remove_at(index, seq): pass
def remove_val(val, seq): pass
def remove_all(val, seq): pass
def count(val, seq): pass
def reverse(seq): pass
def sort_sequence(seq): pass
def testsuite():
    test(make_empty([1, 2, 3, 4]), [])
    test(make_empty(('a', 'b', 'c')), ())
    test(make_empty("No, not me!"), '')
    test(insert_at_end(5, [1, 3, 4, 6]), [1, 3, 4, 6, 5])
    test(insert_at_end('x', 'abc'), 'abcx')
    test(insert_at_end(5, (1, 3, 4, 6)), (1, 3, 4, 6, 5))
    test(insert_in_front(5, [1, 3, 4, 6]), [5, 1, 3, 4, 6])
    test(insert_in_front(5, (1, 3, 4, 6)), (5, 1, 3, 4, 6))
    test(insert_in_front('x', 'abc'), 'xabc')
    test(index_of(9, [1, 7, 11, 9, 10]), 3)
    test(index_of(5, (1, 2, 4, 5, 6, 10, 5, 5)), 3)
    test(index_of(5, (1, 2, 4 , 5, 6, 10, 5, 5), 4), 6)
    test(index_of('y', 'happy birthday'), 4)
    test(ndex_of('banana',['apple','banana','cherry','date']),1)
    test(index_of(5, [2, 3, 4]), -1)
    test(index_of('b', ['apple','banana','cherry','date']),-1)
    test(remove_at(3, [1, 7, 11, 9, 10]), [1, 7, 11, 10])
    test(remove_at(5, (1,4,6,7,0,9,3,5)), (1,4,6,7,0,3,5))
    test(remove_at(2, "Yomrktown"), 'Yorktown')
    test(remove_val(11, [1, 7, 11, 9, 10]), [1, 7, 9, 10])
    test(remove_val(15, (1, 15, 11, 4, 9)), (1, 11, 4, 9))
    test(remove_val('what',('who','what','when','why','how')),('who', 'when', 'why', 'how'))
    test(remove_all(11, [1,7,11,9,11,10,2,11]),[1,7,9,10,2])
    test(remove_all('i', 'Mississippi'), 'Msssspp')
    test(count(5, (1, 5, 3, 7, 5, 8, 5)), 3)
    test(count('s', 'Mississippi'), 4)
    test(count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5]), 2)
    test(reverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
    test(reverse(('shoe','my','buckle',2,1)),(1,2,'buckle','my','shoe'))
    test(reverse('Python'), 'nohtyP')
    test(sort_sequence([3, 4, 6, 7, 8, 2]), [2, 3, 4, 6, 7, 8])
    test(sort_sequence((3, 4, 6, 7, 8, 2)), (2, 3, 4, 6, 7, 8))
    test(sort_sequence("nothappy"), 'ahnoppty')


    
def swap(x, y): # incorrect version
    global a,b
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)
    a,b = x,y
a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)