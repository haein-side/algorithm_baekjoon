import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n : 행, m : 열
miro = [[] for _ in range(n)]

for i in range(n):
    miro[i] = list(map(int, list(input().rstrip())))

q = deque()
q.append((0, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

while q:
    x, y = q.popleft()

    if x == n-1 and y == m-1:
        answer = miro[n-1][m-1]
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1 and miro[nx][ny] == 1:
            miro[nx][ny] += miro[x][y]
            q.append((nx, ny))

print(answer)
