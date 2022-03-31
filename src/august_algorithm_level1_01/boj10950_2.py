import sys

T = int(sys.stdin.readline())

nlist = []
alist = []

for i in range(T):
    nlist.append(list(map(int,sys.stdin.readline().split())))
    print(nlist[i][0]+nlist[i][1])