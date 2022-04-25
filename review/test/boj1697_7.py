import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = []

dx = [-1, 1]

def bfs(cnt, x):
    q = deque()
    q.append((cnt, x)) # 시간, 수빈이 위치
    visited.append(x)

    while q:
        cnt, x = q.popleft()
        
        if x == K:
            print(cnt)
            break
        
        if x <= K // 2: 
            nx = x*2       
            q.append((cnt+1, nx))
        else:
            for i in range(2):
                nx = x + dx[i]
                q.append((cnt+1, nx))
    

bfs(-1, N) # 시간, 수빈이 위치
