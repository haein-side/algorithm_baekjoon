a = int(input())
b = int(input())

c = str(a)
d = str(b)
alist = []
blist = []

for i in range(len(str(a))):
    alist.append(int(c[i]))
    blist.append(int(d[i]))

answer = [None]*4

answer[0] = alist[2]*blist[2] + alist[1]*blist[2]*10 + alist[0]*blist[2]*100

answer[1] = alist[2]*blist[1] + alist[1]*blist[1]*10 + alist[0]*blist[1]*100

answer[2] = alist[2]*blist[0] + alist[1]*blist[0]*10 + alist[0]*blist[0]*100

answer[3] = answer[0]+ answer[1]*10 + answer[2]*100

for i in answer:
    print(i)