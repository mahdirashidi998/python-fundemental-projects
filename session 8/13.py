def  test(a,b):
    import sys
    lineno=sys._getframe(1).f_lineno
    if a==b:
        print('the test in line {0} passed'.format(lineno))
    else :
        print('the test in line {0} failed.we expected {2} but we got {1}'.format(lineno,a,b))
def test_suite():
    test(remove_all('an', 'banana'), 'ba')
    test(remove_all('cyc', 'bicycle'), 'bile')
    test(remove_all('iss', 'Mississippi'), 'Mippi')
    test(remove_all('eggs', 'bicycle'), 'bicycle')
def  count_letters(str,letter,loc=0):
    count=0
    str=str[loc:]
    while str.find(letter)!=-1:
        count+=1
        str=str[str.find(letter)+1:]
    return count
def text_anal(text):
    punc=':;][\].,)(!@#$%^&*()\'"_-/?<>+='
    count1=0
    count2=0
    list1=list(text.split())
    for i in list1:
        for j in list1[count1]:
            if j in punc:
                list1[count1]=list1[count1].replace(j,'')
        count1+=1

        if 'e' in i:
            count2+=1
    etimep=(count2*100)/len(list1)
    etimep='%.1f'%etimep
    print('Your text contains {0} words, of which {1} ({2}) contain an \'e\'.'.format(len(list1),count2,etimep))
def  multiplication_list(range1):
    list1=[]
    string=''
    for i in range(range1+1):
        string=string+str(i)+' '
    list1.append(string)
    string=''
    for i in range(range1):
        string=string+str(i+1)+' '+str(i+1)+' '
        for j in range(2,range1+1):
            string=string+str((i+1)*(j))+' '
        list1.append(string)
        string=''
    return list1
def  multiplication_print(list1):
    for i in list1:
        list2=list(i.split())
        for j in list2:
            print('\t',j,end='')
        print('\n')
def reverse(string):
    string2=''
    for i in range(len(string)-1,-1,-1):
        string2=string2+string[i]
    return string2
def  mirror(string):
    a=string+reverse(string)
    return a
def  remove_letter(rem,string):
    a=''.join(string.split(rem))
    return a
def  is_palindrome(string):
    return string==reverse(string)
def  count(sub,string):
    count=0
    for i in range(len(string)-len(sub)+1):
        if sub==string[i:i+len(sub)]:
            count+=1
    return count
def  remove(sub,string):
    a=string.find(sub)
    if a!=-1:
        string=string[0:a]+string[a+len(sub):]
        return string
    return string
def  remove_all(sub,string):
    a=string.find(sub)
    while a!=-1:
        string=string[0:a]+string[a+len(sub):]
        a=string.find(sub)
    return string
    
test_suite()



