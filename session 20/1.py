def  counter(s):
    s = s.lower()
    b = 'abcdefghijklmnopqrstuvwxyz'
    dic={}
    for i in b:
        dic[i] = s.count(i)
        print(i+'    ',dic[i])
counter('ThiS is String with Upper and lower case Letters')


