import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
nlist = []
for i in range(n):
    a = sys.stdin.readline().strip()
    nlist.append(a)

data = list(permutations(nlist, k)) # 순열 (순서 생각)
dict = {}

for i in range(len(data)):
    add = ''
    for j in range(k):
        add = add + data[i][j]
    if add not in dict.keys():
        dict[add] = 1

print(len(dict))
