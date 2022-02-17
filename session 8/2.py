def  count_letters(str,letter):
    count=0
    for i in str:
        if i==letter:
            count+=1
    return count
print(count_letters('banana','a'))