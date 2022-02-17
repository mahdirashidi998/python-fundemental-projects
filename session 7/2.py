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
print(sum_negetive_numbers([-12,-12,23,24]))