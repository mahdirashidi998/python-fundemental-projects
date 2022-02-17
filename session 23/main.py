def  wordlist(filepath):
    book = open(filepath)
    string = book.read()
    book.close()
    string = string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ,.!?"-*+/>()0123456789[]:;\'','abcdefghijklmnopqrstuvwxyz                              ')
    list1=string.split()
    list1.sort()
    set1 = set(list1)
    return (list1,set1)
def  count(word,l):
    ind = l.index(word)
    for i in l[ind:]:
        if i == word:
            con += 1
        else :
            return con
def  saver(filepath2,string):
    file1 = open(filepath2,'w')
    file1.write(string)
    file1.close()

def  main(filepath,filepath2):
    list1,set1 = wordlist(filepath)
    for i in set1:
        b= count(i,list1)
        s = '{0}    {1}'.format(i,b)
        saver(filepath2,s)
main('C:\\Users\\sepehr\\OneDrive\\datas\\python programing\\book\\questions\\session 20\\11-0.txt','C:\\Users\\sepehr\\OneDrive\\datas\\python programing\\book\\questions\\session 20\\alice.txt')


    


