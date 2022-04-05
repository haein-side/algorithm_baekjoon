import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
arr = []

num = list(map(int, sys.stdin.readline().split()))

result = list(itertools.combinations(sorted(num),3))

result.append(M)
mid = []
for i in range(len(result)-1):
    mid.append(sum(result[i]))
    
mid.append(M)
mid = sorted(mid)

if mid.count(M) > 1:
    print(M)
else:
    print(mid[mid.index(M)-1])