import itertools
import sys

n, s = map(int, sys.stdin.readline().split())

nlist = list(map(int, sys.stdin.readline().split()))

count = 0

for k in range(1, n+1): # 1개부터 n개까지
    clist = list(itertools.combinations(nlist, k))
    print(clist)
    for i in range(len(clist)):
        sum = 0
        for j in range(len(clist[i])):
            sum += clist[i][j]
            
        if sum == s:
            count += 1

print(count)

# 4 0
# -3 -2 3 2
# [(-3,), (-2,), (3,), (2,)]
# [(-3, -2), (-3, 3), (-3, 2), (-2, 3), (-2, 2), (3, 2)]
# [(-3, -2, 3), (-3, -2, 2), (-3, 3, 2), (-2, 3, 2)]
# [(-3, -2, 3, 2)]
# 3