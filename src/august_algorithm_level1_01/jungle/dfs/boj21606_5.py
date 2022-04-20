# 73점 맞춘 풀이
import sys
from collections import deque

N = int(sys.stdin.readline())
node = [[] for _ in range(N+1)]
visited = [False] * (N+1)
plist = [-2] + list(map(int, sys.stdin.readline().strip())) # 맨 앞 빈 노드는 -2라는 임의의 값 
place = {} # {0: -2, 1: 1, 2: 0, 3: 1, 4: 1, 5: 1} 각각의 위치 좌표
for i in range(N+1):
    if plist[i] == 1: # 실내
        place[i] = 1
    elif plist[i] == 0: # 실외
        place[i] = 0
    else: # 빈 노드
        place[i] = -2

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
cnt = 0
def bfs(i):
    global cnt
    queue = deque()
    queue.append(i)
    visited[i] = True
    
    while queue:
        v = queue.popleft() # 1
        p = place[v]
        for k in node[v]: # v 노드의 인접 노드를 다 돎
            if visited[k] == False: # 2
                q = place[k]
                visited[k] = True
                if q == 1:
                    cnt += 1
                else:
                    queue.append(k)

            
for j in range(1, N+1):
    if place[j] == 1: # 실내일 때만 처음 start 노드로 bfs 돎
        bfs(j)
        visited = [False] * (N+1)

print(cnt)