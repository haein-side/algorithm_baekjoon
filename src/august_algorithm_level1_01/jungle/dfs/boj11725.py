# 이 풀이는 따로 부모 테이블 같은 걸 두지 않고 풀었다.
# 자식노드가 2개 이상일 때 성립하지 않는 코드..

import sys
N = int(sys.stdin.readline())
node = [[] for i in range(N+1)] # 0번째 노드는 비워두기

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a) # 2차원 행렬 이외에 리스트로 받는 방안 or 딕셔너리로 받는 방안도 구현해보기

visited = [False] * (N+1)
trace = []

def dfs(i):
    global trace
    
    visited[i] = True
    trace.append(i)
    
    for j in node[i]: # i 노드와 인접한 노드 j
        if not visited[j]:
            dfs(j)
    
for i in range(1, N+1): # 1부터 N까지 노드
    if not visited[i]:
        dfs(i)

for i in range(2, N+1):
    if i not in node[1]:
        print(trace[trace.index(i)-1])
    else:
        print(1)