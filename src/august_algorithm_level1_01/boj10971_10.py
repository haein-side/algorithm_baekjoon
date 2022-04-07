import sys
import itertools

n = int(sys.stdin.readline())
clist = [i for i in range(1, n)]
# print(clist)
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
total = []
v = list(itertools.permutations(clist, len(clist)))
minCost = 99999999

for i in range(len(v)):
    cost = [] 
    for j in range(len(v[i])+1):
        if j == 0:
           cost.append(matrix[0][v[i][j]])
        elif j == len(v[i]):
           cost.append(matrix[v[i][j-1]][0])
        else:
           cost.append(matrix[v[i][j-1]][v[i][j]])
            
    if 0 not in cost:
        minCost = min(minCost, sum(cost))

print(minCost)