import sys
from itertools import permutations, combinations

a = []

for i in range(9):
    a.append(int(sys.stdin.readline()))
    
d = list(combinations(a, 7))

for j in d:
    if sum(j) == 100:
        j = sorted(j)
        for i in range(7):
            print(j[i])
        break



    