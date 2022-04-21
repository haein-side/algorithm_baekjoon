import sys
input = sys.stdin.readline

N, M = map(int, input().split())
light_g = [[] for _ in range(N+1)] # 나보다 가벼운 것들이 원소
heavy_g = [[] for _ in range(N+1)] # 나보다 무거운 것들이 원소
visited = [False for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    light_g[a].append(b)
    heavy_g[b].append(a)

cnt = 0
def dfs(i):
    global cnt
    visited[i] = True
   
    for j in light_g[i]:
        if not visited[j]:
            visited[j] = True
            cnt += 1
            dfs(j)
            
    return cnt

def dfs_2(i):
    global cnt
    visited[i] = True
   
    for j in heavy_g[i]:
        if not visited[j]:
            visited[j] = True
            cnt += 1
            dfs(j)
            
    return cnt

result = 0
for i in range(1, N+1):
    if not visited[i]:
        tmp = dfs(i)
        if tmp >= (N+1) // 2:
            result += 1
        visited = [False for _ in range(N+1)]

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        tmp = dfs_2(i)
        if tmp >= (N+1) // 2:
            result += 1
        visited = [False for _ in range(N+1)]
        
print(result)