import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
miro = [[] for _ in range(N)]

for i in range(N):
    miro[i] = list(map(int, list(input().rstrip())))
    
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global cnt
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        a, b = q.popleft()
        exist = miro[a][b] # 기존 미로 값

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if miro[nx][ny] == 1: # 이동할 수 있는 칸
                    if not visited[nx][ny]:
                        q.append((nx, ny))
                        miro[nx][ny] = exist + 1

bfs(0,0)

print(miro[N-1][M-1])