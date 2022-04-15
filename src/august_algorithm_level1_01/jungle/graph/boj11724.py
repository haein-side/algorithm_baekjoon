# DFS(너비우선탐색) 방식으로 풀기
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
node = [[] for i in range(N+1)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    node[u].append(v)
    node[v].append(u)
    
# 방문 기록 (0번째 빈 노드가 visited[i] False로 되어있어 dfs를 돌지 않도록 True로 선언)
visited = [True] + [False] * (N)

# DFS
def dfs(i):
    visited[i] = True

    for ad_node in node[i]: # i 노드의 인접 노드들 DFS 탐색
        if not visited[ad_node]: # 인접 노드에 방문된 적 없을 때
            dfs(ad_node)

cnt = 0

# 정점 하나씩 돌면서 dfs 탐색 (연결된 것들 보기)
for i in range(N+1):
    if not visited[i]: # dfs() 한 번 돌 때 연결 요소들을 모두 방문하여 True 처리해주었으므로
        dfs(i)         # 이미 연결된 요소는 dfs() 또 돌 수 없음 (dfs로 한 번 다 방문했기 때문)
        cnt += 1
        
print(cnt)