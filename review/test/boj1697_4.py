import sys
from collections import deque
from turtle import xcor
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False for _ in range(100001)]
location = [0 for _ in range(100001)]

# print(visited)

dx = [-1, 1, 2]

def bfs(x):
    q = deque()
    q.append(x) # 시간, 수빈이 위치
    visited[x] = True

    while q:
        x = q.popleft()
        exist = location[x] # 기존 위치 값
        
        if exist < K // 2:
            nx = x * 2
        else:
            for i in range(2):
                nx = x + dx[i]
                
        if 0 <= nx <= 100000:
            if not visited[nx]:
                q.append(nx)
                location[nx] = exist+1
        
        # for i in range(3):
        #     nx = 0
        #     if i == 0 or i == 1 :
        #         nx = x + dx[i]
        #     else:
        #         nx = x * dx[i]
        #     if 0 <= nx <= 100000:
        #         if not visited[nx]:
        #             q.append(nx)
        #             location[nx] = exist+1

bfs(N) # 시간, 수빈이 위치
print(location[K])