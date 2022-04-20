import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    # graph.append(list(map(int, list(input().split()))))
    graph.append(list(map(int, sys.stdin.readline().split())))
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    zarr = []
    while queue:
        a, b = queue.popleft() # pop해준 수 기준으로 동서남북 돎
        
        zcnt = 0 # 0의 개수
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < N and 0 <= ny < M: # 범위 안에 있을 때
                    if graph[nx][ny] == 0: # 0이 있으면
                        zcnt += 1
                    else:
                        if not visited[nx][ny]: # 방문해본 적이 없음
                            queue.append((nx, ny))
                            visited[nx][ny] = True 
        
        if zcnt >= graph[a][b]:
            zarr.append((a, b))
        elif zcnt < graph[x][y]:
            graph[x][y] = graph[x][y] - zcnt
        
    for c, d in zarr:
        graph[c][d] = 0
    
    print(graph)
        
year = 0        
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] != 0: # 방문한 적이 없을 때
            bfs(i, j)
            year += 1
            visited = [[False for _ in range(M)] for _ in range(N)]
            