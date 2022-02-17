def  count_letters(str,letter,loc=0):
    count=0
    str=str[loc:]
    while str.find(letter)!=-1:
        count+=1
        str=str[str.find(letter)+1:]
    return count
print(count_letters('banana','a',2))
