import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
virus = [[] for _ in range(N)]
for i in range(N):
    virus[i] = list(map(int, sys.stdin.readline().split()))

visited = [[False for _ in range(N)] for _ in range(N)]

S, X, Y = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0)) # x 좌표, y 좌표
    visited[0][0] = True
    
    while q:
        # q = deque(sorted(q))
        x, y = q.popleft()
        print(x, y)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            if virus[nx][ny] == 0 and not visited[nx][ny]: # 0일 때
                virus[nx][ny] = virus[x][y]
                q.append((nx, ny))
    
    print(virus)
    
bfs()