import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001 # visited 거리 인덱스, 시간 값

def bfs(x):
    q = deque()
    q.append(x) # 시간, 수빈이 위치

    while q:
        v = q.popleft()
        
        if v == K:
            print(visited[v])
            break
        
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]: # 0이 false이므로 방문한 적 없을 때
                q.append(i)
                visited[i] = visited[v] + 1

bfs(N) # 수빈이 위치
