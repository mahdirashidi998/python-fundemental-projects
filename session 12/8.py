def  test(a,b):
    import sys
    line_number=sys._getframe(1).f_lineno
    if a==b:
        print('the test in line {0} passed'.format(line_number))
    else:
        print('the tet in line {0} failed. we expected {1} but we got {2}'.format(line_number,b,a))
def  test_suite():
    test(cleanword('what?'), 'what')
    test(cleanword('"now!"'), 'now')
    test(cleanword('?+="w-o-r-d!,@$()"'), 'word')
    test(has_dashdash('distance--but'), True)
    test(has_dashdash('several'), False)
    test(has_dashdash('spoke--'), True)
    test(has_dashdash('distance--but'), True)
    test(has_dashdash('-yo-yo-'), False)
    test(extract_words('Now is the time! "Now", is the time? Yes, now.'),['now','is','the','time','now','is','the','time','yes','now'])
    test(extract_words('she tried to curtsey as she spoke--fancy'),['she','tried','to','curtsey','as','she','spoke','fancy'])
    test(wordcount('now', ['now','is','time','is','now','is','is']), 2)
    test(wordcount('is', ['now','is','time','is','now','the','is']), 3)
    test(wordcount('time', ['now','is','time','is','now','is','is']), 1)
    test(wordcount('frog', ['now','is','time','is','now','is','is']), 0)
    test(wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is']),['is', 'now', 'time'])
    test(wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am']),['I', 'a', 'am', 'is'])
    test(wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am']),['a', 'am', 'are', 'be', 'but', 'is', 'or'])
    test(longestword(['a', 'apple', 'pear', 'grape']), 5)
    test(longestword(['a', 'am', 'I', 'be']), 2)
punctuations='!@#$%^&*()_+-><?":;\'=.,'
def  cleanword(st):
    for i in st:
        if i in punctuations:
            st=''.join(st.split(i))
    return st
def  has_dashdash(st):
    return ('--' in st)
def  extract_words(st):
    if has_dashdash(st):
        st=' '.join(st.split('--'))
    list2=[]
    st=cleanword(st)
    list=st.split()
    for i in list:
        list2.append(i.lower())
    return list2
def  wordcount(word,words):
    count=0
    for i in words:
        if i == word:
         count += 1
    return count
def  wordset(lis):
    lis2=[]
    for i in lis:
        if i in lis2:
            continue
        lis2.append(i)
        lis2=sorted(lis2)
    return lis2
def  longestword(list1):
    lend=0
    for i in list1:
        if len(i)>lend :
            lend=len(i)
    return lend
test_suite()