import copy
shuf_list = input().split()
for i in range(len(shuf_list)):
    shuf_list[i] = int(shuf_list[i])
def  sort1(l):
    l2=l.copy()
    for i in range(len(l2)):
        for j in range(len(l)):
            if l[j] <= l2[i]:
                l2[i] = l[j]
        l.remove(l2[i])
    return l2

print(sort1(shuf_list))
input()
                

