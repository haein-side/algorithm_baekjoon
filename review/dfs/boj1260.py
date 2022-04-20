import sys
input = sys.stdin.readline
from collections import deque

# N: 정점 개수, M: 간선 개수, V: 탐색 시작할 정점 번호
N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i] = sorted(graph[i])

visited = [False] * (N+1)

def dfs(i):
    visited[i] = True
    print(i, end = ' ')
    
    for j in graph[i]: # i번 노드와 인접한 노드
        if not visited[j]: # 방문된 적이 없으면
            dfs(j) # 재귀로 방문

def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        v = q.popleft()
        print(v, end = ' ')
        
        for j in graph[v]: # 현재 pop한 원소의 인접 노드
            if not visited[j]:
                q.append(j)
                visited[j] = True


dfs(V)
visited = [False] * (N+1)
print()
bfs(V)