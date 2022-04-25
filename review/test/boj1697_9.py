import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(start):
    queue = deque()
    queue.append(start) # 큐엔 거리를 넣어줌
    
    while queue:
        v = queue.popleft()
        
        if v == K: # 현재까지 거리가 K에 도달 시
            print(visited[v])
            break
        
        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and not visited[i]: # i의 크기로 먼저 거르고 not visited[i] 처리를 해줘야 index error가 나지 않음!
                queue.append(i)
                visited[i] = visited[v] + 1
                
bfs(N)