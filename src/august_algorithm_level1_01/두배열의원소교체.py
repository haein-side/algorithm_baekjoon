import sys

n, k = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
blist = list(map(int, sys.stdin.readline().split()))

alist = sorted(alist)
blist = sorted(blist, reverse = True)

j = 0

for i in range(n):
    if alist[i] < blist[i]:
        alist[i], blist[i] = blist[i], alist[i]
        j += 1
    if j == k:
        break

print(sum(alist))
    