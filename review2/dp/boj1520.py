# 기본적인 dfs 풀이
# 시간초과 
# dp와 bfs를 결합하여 풀어야
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split()) # m: 세로, n: 가로

road = [[] for _ in range(m)] # [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

for i in range(m):
    road[i] = list(map(int, input().split()))

v = [[-1 for _ in range(n)] for _ in range(m)] # 아직 방문한 적 없으면 -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

def dfs(x, y): # 현재위치 x, y
    global cnt
    if x == m-1 and y == n-1:
        cnt += 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx <= m-1 and 0 <= ny <= n-1 and road[nx][ny] < road[x][y]:
            if v[nx][ny] == -1:
                v[nx][ny] = 0
                dfs(nx, ny)
                v[nx][ny] = -1
    

dfs(0, 0)

print(cnt)
    
