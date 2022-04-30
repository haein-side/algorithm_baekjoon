import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split()) # m이 행, n이 열

road = [[0 for _ in range(n+1)]]

for i in range(m):
    road.append([0] + list(map(int, input().split())))

cur = [[-1 for _ in range(n+1)] for _ in range(m+1)]

# 좌표 이동
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def dfs(x, y):
    # print(x, y, c)
    if x == m and y == n: 
        return 1
    if cur[x][y] != -1: 
        return cur[x][y]
    cur[x][y] = 0 
    for i in range(4):
        a, b = x + dx[i], y + dy[i] 
        if 1 <= a <= m and 1 <= b <= n: 
            if road[x][y] > road[a][b]: 
                cur[x][y] += dfs(a, b) 

    return cur[x][y]

print(dfs(1,1))
         