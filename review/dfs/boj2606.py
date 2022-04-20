import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(i):
    global cnt
    visited[i] = True
    
    for j in graph[i]:
        if visited[j] == False:
            visited[j] = True
            dfs(j)
            cnt += 1
    
    return cnt

print(dfs(1))