import sys
import itertools
n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

perm = list(itertools.permutations(nlist, n))

result = []
for i in range(len(perm)):
    s = 0
    for j in range(0, len(perm[i])-1):
        s += abs(perm[i][j]- perm[i][j+1])
    result.append(s)

print(max(result))