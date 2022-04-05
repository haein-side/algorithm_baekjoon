import sys
import itertools

n = int(sys.stdin.readline())
clist = [i for i in range(1,n)]
minCost = 9999999
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    
perm = list(itertools.permutations(clist, len(clist)))

for i in range(len(perm)):
    cost = []
    for j in range(len(perm[i])+1):
        if j == 0:
            cost.append(matrix[0][perm[i][j]])
        elif j == n - 1:
            cost.append(matrix[perm[i][j-1]][0])
        else:
            cost.append(matrix[perm[i][j-1]][perm[i][j]])
    
    if 0 not in cost: 
        # 확실하게 cost에 0이 있는지 아는 방법은 cost를 배열로 만들고 각 배열의 원소로 cost를 넣어준 다음, 0이 존재하는지 보는 것!
        minCost = min(minCost, sum(cost))

print(minCost)