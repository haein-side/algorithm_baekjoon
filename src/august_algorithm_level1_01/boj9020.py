import sys
from itertools import combinations_with_replacement

def sol(n):
    nlist = [] # 각각의 수 이하의 소수 모음
    
    for i in range(2, n):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            nlist.append(i)
    mlist = [] # nlist 중복허용 조합
    mlist = list(combinations_with_replacement(nlist, 2))
    
    alist = [] # 소수의 합이 n이 되는 것
    for i in range(len(mlist)):
            if mlist[i][0] + mlist[i][1] == n:
                alist.append([mlist[i][0], mlist[i][1]])
    flist = [] # alist 의 차
    for i in range(len(alist)):
        flist.append(alist[i][1] - alist[i][0])
    
    dict={}
    
    for i in range(len(flist)):
        dict[flist[i]] = alist[i]
    
    a = dict[min(dict.keys())][0]
    b = dict[min(dict.keys())][1]
    
    answer = str(a) + " " + str(b)
    return answer


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    print(sol(n))