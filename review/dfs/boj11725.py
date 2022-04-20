import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

dic = dict()

def dfs(i):
    visited[i] = True
    
    for j in graph[i]:
        if not visited[j]:
           dic[j] = [i] # 자식노드별로 부모노드 하나를 가짐
           visited[j] = True
           dfs(j)

dfs(1)

for i in range(2, N+1):
    print(dic[i][0])