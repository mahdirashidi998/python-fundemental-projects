def  reverse_lines(file,file_name):
    f1=open(file)
    lines=f1.readlines()
    lines[-1]=lines[-1]+'\n'
    f1.close()
    f2=open(file_name,'w')
    for i in range(len(lines)-1,-1,-1):
        f2.write(lines[i])
    f2.close()
def  snake_reader(file):
    f1=open(file)
    while True:
        line=f1.readline()
        if line=='':
            break
        if 'snake' in line :
            print(line,end='\n')
snake_reader('c:/Users/sepehr/OneDrive/datas/python programing/book/questions/session 13/text.txt')       
