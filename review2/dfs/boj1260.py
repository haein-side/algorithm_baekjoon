import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점 여러 개일 때 정점 번호가 작은 걸 먼저 방문 위해 sort
for i in range(n+1):
    graph[i] = sorted(graph[i])

# visited = [False * (n+1)] # 이렇게 하면 안 됨
visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)

print()

visited = [False] * (n+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ') # 뽑아냈을 때 방문한 것
        for i in graph[v]: # 뽑아낸 것 (방문한 것) 기준으로 for문 돌기
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, v, visited)
