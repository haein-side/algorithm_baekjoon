from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
dict = {}

for i in range(m+1):
    dict[i] = 0

a = list(combinations(nlist, 3))

for i in range(len(a)):
    num = sum(a[i])
    if dict.get(num) is not None:
        dict[num] = dict.get(num) + 1

for i in range(m, 0, -1):
    if dict.get(i) > 0:
        print(i)
        break