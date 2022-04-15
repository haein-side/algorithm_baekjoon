import sys
from collections import deque

# N: 정점 개수, M: 간선 개수, V: 탐색 시작 정점 번호
N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]

# 각 노드가 연결된 정보를 2차원 리스트 자료형으로 표현
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점 여러 개일 때 정점 번호가 작은 걸 먼저 방문 위해 sort
for i in range(N+1):
    graph[i] = sorted(graph[i])

# print(graph)

# 각 노드가 방문된 정보를 1차원 리스트 자료형으로 표현
# 0번 노드는 취급 안해서 N + 1개
visited = [False] * (N+1)

# DFS 메서드 정리
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
# BFS 메서드 정리
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
    
dfs(graph, V, visited)
visited = [False] * (N+1)
print()
bfs(graph, V, visited)