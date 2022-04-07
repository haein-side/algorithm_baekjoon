import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
minCost = 9999999
visited = [False] * n # False가 아직 방문하지 않은 상태

def dfs(cur, cost):
    global minCost, visited
    
    # 이미 최솟값 아니라면 바로 리턴
    if cost > minCost :
        return
    
    # 다 돌았을 때
    if cur == 0 and visited.count(False) == 0:
        minCost = min(minCost, cost)
        return
    
    for i in range(n):
        if matrix[cur][i] != 0 and visited[i] == False:
            visited[i] = True
            dfs(i, cost + matrix[cur][i])
            visited[i] = False


dfs(0, 0)
print(minCost)