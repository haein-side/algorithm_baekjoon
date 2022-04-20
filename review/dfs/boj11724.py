# 덩어리의 개수를 구하라는 게 핵심
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    visited[i] = True # 방문 처리 
                      # 인접 노드 방문해주면서 방문한 적 없으면 방문처리 및 재귀로 dfs()
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
    
