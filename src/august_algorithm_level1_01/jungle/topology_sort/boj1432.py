import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1) # 모든 노드에 대한 진입차수를 0으로 초기화

for i in range(1,N+1):
    arr = [0] + list(map(int, list(sys.stdin.readline().strip())))
    for j in range(1,N+1):
        if arr[j] == 1:
            graph[i].append(j)
            indegree[j] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    dic = dict()
    for i in range(len(result)):
        dic[result[i]] = i+1
    
    if len(dic) > 0:
        for i in range(len(result)):
            print(dic[i+1], end = " ")
    else:
        print(-1)

            
topology_sort()