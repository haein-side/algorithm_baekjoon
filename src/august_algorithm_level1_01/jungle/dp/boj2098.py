import sys
input = sys.stdin.readline

n = int(input())
matrix = [[0,0] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
visited = [False for _ in range(n)]
minCost = 1e9

def dfs(cur, cost):
    global minCost
    
    if cost > minCost:
        return
    if cur == 0 and visited.count(False) == 0: # 다 방문했을 때
        minCost = min(minCost, cost)
        return minCost
    
    for i in range(n): # 현재 매트릭스에 인접한 노드들 방문
        if not visited[i]: # i번째 방문한 적 없으면 방문하기
            visited[i] = True
            dfs(i, cost + matrix[cur][i]) # cur에서 i로 이동하면 비용이 이미 가지고 있던 비용(cost) + matrix[cur][i] 가 됨!
            visited[i] = False
            
dfs(0, 0)
print(minCost)
