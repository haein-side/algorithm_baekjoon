import sys
import itertools

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
mlist = list(itertools.permutations(nlist, len(nlist)))

total = []
for i in range(len(mlist)):
    sum = 0
    for j in range(n-1):
        sum += abs(mlist[i][j]-mlist[i][j+1])
    total.append(sum)   

print(max(total))