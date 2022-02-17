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
text='''in a function named count_letters, and generalize it so that it accepts the string and the letter
as arguments. Make the function return the number of characters, rather than print the answer.
The caller should do the printing.
4. Now rewrite the count_letters function so that instead of traversing the string, it repeatedly
calls the find method, with the optional third parameter to locate new occurences of the letter
being counted.
5. Assign to a variable in your program a triple-quoted string that contains your favourite
paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some inspirational
verses, etc.
Write a function which removes all punctuation from the string, breaks the string into a list of
words, and counts the number of words in your text that contain the letter ‘e’. Your program
should print an analysis of the text like this:'''
text_anal(text)
        

