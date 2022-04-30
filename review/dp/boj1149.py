import sys
input = sys.stdin.readline

n = int(input())
cost = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    cost[i] = list(map(int, input().split()))

res = 0
for i in range(1, n):
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
    cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1])
    
    if i == n-1:
        res = min(cost[i][0], cost[i][1], cost[i][2])

print(res)