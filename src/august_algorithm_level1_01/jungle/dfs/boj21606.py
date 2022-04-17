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

result = 0

def dfs(i):
    global result
    queue = deque()
    queue.append(i)
    visited[i] = True
    
    while queue:
        v = queue.popleft()
        pl = place[v]
        cnt = 1 # 방문 노드의 수
        print(v, end = " ")
        for k in range(len(node[v])): # v 노드의 인접 노드
            if cnt == 1 and visited[k] == False and place[k] == 1 and pl == 1 : # 실내 - 실내 케이스 탐색
                visited[k] = True
                cnt += 1
                result += 1
                break
            elif cnt == 1 and visited[k] == False and place[k] == 0 and pl == 1: # 실내 - 실외 ...
                queue.append(k)
                visited[k] = True
                cnt += 1
            elif cnt > 1 and visited[k] == False and place[k] == 0 and pl == 0: # (실내 - )실외 - 실외 ...
                queue.append(k)
                visited[k] = True
                cnt += 1
    
    return result
                
            

for j in range(N+1):
    if place[j] == 1 and visited[j] == False: # 실내일 때만 처음 start 노드로 bfs 돎
        dfs(j)
        # print(dfs(j))
