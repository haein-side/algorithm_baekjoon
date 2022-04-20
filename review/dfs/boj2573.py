import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().split()))))
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

zarr = []
def dfs(x, y):
    global zarr
    visited[x][y] = True
    
    zcnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M: # 범위 안에 있을 때
            if not visited[nx][ny]: # 방문해본 적이 없음
                if graph[nx][ny] == 0:
                    zcnt += 1
    
    if zcnt >= graph[x][y]:
        zarr.append((x, y))
    elif zcnt > 0 and zcnt < graph[x][y]:
        graph[x][y] = graph[x][y] - zcnt

for i in range(1, N):
    for j in range(1, M):
        if not visited[i][j] and graph[i][j] != 0: # 방문한 적이 없고 0이 아닐 때
            dfs(i, j)
            