import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # a가 b에 도달 가능
    indegree[b] += 1 # b에 대한 진입차수 올려줌

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0: # 진입차수가 0인 노드를 큐에 넣어줌
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]: # 나보다 키가 큰 학생 (인접노드)
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

print(topology_sort())
    