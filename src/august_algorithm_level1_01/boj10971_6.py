import sys
n = int(sys.stdin.readline())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split()))) # 인덱스가 각 도시에서 다른 도시로 가는 것 // 값은 비용

minCost = 9999999
visited = [False for _ in range(n)] # 방문 안 된 상태를 False
  
def dfs(start, cur, cost):
    global matrix, minCost, visited
    
    # 다시 그 도시로 돌아온 것 (끝난 것)
    if start == cur and visited.count(False) == 0:
        minCost = min(minCost, cost)
    
    for i in range(n):
        if matrix[cur][i] != 0 and visited[i] == False: # 방문할 수 있다면
            visited[i] = True
            dfs(start, i, cost + matrix[cur][i]) # 현위치를 i로, cost + matrix[cur][i]에 계속 비용 쌓임
            visited[i] = False
            

dfs(0, 0, 0)
print(minCost)