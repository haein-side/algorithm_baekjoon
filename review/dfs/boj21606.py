import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
place = [0] + list(map(int, list(input().strip())))
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 실외노드와 인접한 실내노드의 개수 구하기
def dfs(i):
    home_cnt = 0
    for j in graph[i]: # i 노드와 인접한 노드 j
        if place[j] == 1: # 인접노드가 실내노드일 때
            home_cnt += 1
            continue
        else: # 인접노드가 실외노드일 때
            if not visited[j]:
                visited[j] = True
                home_cnt += dfs(j)
    return home_cnt

            
cnt = 0
for i in range(1, N+1):
    if place[i] == 1: # 현재 노드가 실내일 때
        for j in graph[i]: # 인접노드
            if place[j] == 1: # 인접노드도 1일 때
                cnt += 1
    else: # 현재 노드가 실외일 때
        if not visited[i]: # 방문한 적이 없을 때
            visited[i] = True
            tmp = dfs(i)
            cnt += tmp * (tmp-1)
            
print(cnt)