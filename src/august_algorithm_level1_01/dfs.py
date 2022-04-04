
# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    # v 노드에서 인접한 노드인 i 노드를 매개변수로 받음
    # 해당 노드를 방문처리 해줌!
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: 
            # v 노드에서 인접한 노드인 i에 더이상 F(방문하지 않은 노드)가 없을 때는 
            # 재귀호출을 더이상 진행하지 않음!
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)