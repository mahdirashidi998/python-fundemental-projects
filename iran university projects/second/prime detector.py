def is_prime(n):
    count=0
    if n==1:
        return 'nope'
    for i in range(1,n+1):
        if n%i==0 :
            count+=1
    if count>2 :
        return 'nope'
    else :
        return 'yup'
def  asli(n):
    if is_prime(n)=='yup':
        print('yup')
    if n==1:
        print(3)
        return
    else:
        for i in range(n-1,0,-1):
            if is_prime(i)=='yup':
                b=i
                print(b,end=',')
                break
        for i in range(n,n+100000):
            if is_prime(i)=='yup':
                a=i
                print(a)
                break


n=int(input())
asli(n)


