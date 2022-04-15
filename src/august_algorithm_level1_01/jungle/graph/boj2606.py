import sys

t = int(sys.stdin.readline())
s = int(sys.stdin.readline())
c = [[] for i in range(t+1)] # 0번 []는 비워둠

visited = [False] * (t+1)
 
for i in range(s):
    a, b = map(int, sys.stdin.readline().split())
    c[a].append(b)
    c[b].append(a)

def dfs(i):
    visited[i] = True
    
    for j in c[i]: # i 노드의 인접노드 j
        if not visited[j]:
            dfs(j)

cnt = 0
# 각각의 노드를 돌며 방문여부 확인 및 dfs 탐색
for i in range(1, t+1):
    if not visited[i]: # 방문되지 않았을 때
        dfs(i)
        if i == 1:
            cnt = visited.count(True)

print(cnt-1) # 1번 자기 자신을 제외하고 바이러스 감염되는 컴 수