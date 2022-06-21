import sys
from collections import deque

n, m = map(int, input().split())
road = []
for i in range(n):
    road.append(list(map(int, input().rstrip())))

visited = [[False for _ in range(n)] for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y =  queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx <= n-1 and 0<= ny <= m-1:
                if road[nx][ny] == 1 and not visited[nx][ny]:
                    if nx == n-1 and ny == m-1:
                        return cnt
                    else:
                        queue.append([nx, ny])
                        cnt += 1
                        visited[nx][ny] = True

print(bfs(0, 0))