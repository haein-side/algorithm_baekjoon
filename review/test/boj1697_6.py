import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = []

# print(visited)

dx = [-1, 1]

def bfs(cnt, x):
    q = deque()
    q.append((cnt, x)) # 시간, 수빈이 위치
    visited.append(x)

    while q:
        cnt, x = q.popleft()
        print(cnt, x)
        if x == K:
            print(cnt)
            break
        
        if x <= K // 2:
            nx = x * 2
            if nx < 0 or nx > 100000:
                continue
            if nx not in visited:
                q.append((cnt+1, nx))
        else:
            for i in range(2):
                nx = x + dx[i]
            if nx < 0 or nx > 100000:
                continue
            if nx not in visited:
                q.append((cnt+1, nx))

bfs(0, N) # 시간, 수빈이 위치
