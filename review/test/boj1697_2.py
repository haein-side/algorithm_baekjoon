import sys
from collections import deque
input = sys.stdin.readline
INF = int(10e9)

start, end = map(int, input().split())
visited = [INF for i in range(100001)]

dx = [-1, 1]

def bfs():
    q = deque()
    q.append(start) # 시간, 수빈이 위치
    visited[start] = 0 # visited 인덱스가 위치, 값이 시간

    while q:
        now = q.popleft() # now 는 위치
        
        if now == end:
            print(visited[now])
            break
        
        for i in range(3):
            nx = 0
            if i == 0 or i == 1:
                nx = now + dx[i]
            else:
                nx = now * dx[i]
            if 0 <= nx <= 100000 and visited[nx] == False:
                visited[nx] = visited[now] + 1
                q.append(nx)

bfs() # 시간, 수빈이 위치