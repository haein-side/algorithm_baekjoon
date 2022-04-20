import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())

flag = False
def dfs(i):
    global flag 
    for j in graph[i]:
        if visited[j] == 0: # 인접노드에 방문한 적 없을 때
           visited[j] = -visited[i] 
           dfs(j)
        else: # 인접노드에 방문한 적 있을 때
            if visited[j] == visited[i]: # 두 인접노드가 같은 색깔일 때
                flag = True
    


for i in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for j in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1, V+1):
        if visited[k] == 0: # 방문한 적 없을 때
            visited[k] = 1
            dfs(k)
    if not flag:
        print('YES')
    else:
        print('NO')
    flag = False