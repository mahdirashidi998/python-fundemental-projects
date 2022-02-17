a,b=input().split('-')
duz={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
if a=='X':
    turn1='XOXOXOXOXOXOXOXOXO'
if a=='O':
    turn1='OXOXOXOXOXOXOXOXOXOX'
for i in range(8):
        duz[b]=turn1[i]
        #print(duz['1'],duz['2'],duz['3'],end=' ')
        #print('\n')
        #print(duz['4'],duz['5'],duz['6'],end=' ')
        #print('\n')
        #print(duz['7'],duz['8'],duz['9'],end=' ')
        #print('\n')
        if (duz['1']=='O'and duz['2']=='O' and duz['3']=='O') or (duz['4']=='O'and duz['5']=='O' and duz['6']=='O') or  (duz['7']=='O'and duz['8']=='O' and duz['9']=='O') or (duz['1']=='O'and duz['4']=='O' and duz['7']=='O') or (duz['2']=='O'and duz['5']=='O' and duz['8']=='O') or (duz['3']=='O'and duz['6']=='O' and duz['9']=='O') or (duz['1']=='O'and duz['5']=='O' and duz['9']=='O') or (duz['3']=='O'and duz['5']=='O' and duz['7']=='O') :
            print('O')
            break
        if (duz['1']=='X'and duz['2']=='X' and duz['3']=='X') or (duz['4']=='X'and duz['5']=='X' and duz['6']=='X') or  (duz['7']=='X'and duz['8']=='X' and duz['9']=='X') or (duz['1']=='X'and duz['4']=='X' and duz['7']=='X') or (duz['2']=='X'and duz['5']=='X' and duz['8']=='X') or (duz['3']=='X'and duz['6']=='X' and duz['9']=='X') or (duz['1']=='X'and duz['5']=='X' and duz['9']=='X') or (duz['3']=='X'and duz['5']=='X' and duz['7']=='X') :
            print('X')
            break
        if i>=8:
            print('No Winner')
            break
        b=input()



