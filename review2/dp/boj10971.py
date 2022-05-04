import sys
input = sys.stdin.readline

n = int(input())
cost = [[0 for _ in range(n)] for _ in range(n+1)]
# [[0, 0, 0, 0], [0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]

for i in range(1, n+1):
    cost[i] = list(map(int, input().split()))
visited = [0] + [-1 for _ in range(n-1)] # -1 방문 아직 안 함, 0 방문 함
comp = []

def dfs(x, depth): # x: 현재위치, depth: 방문한 도시 갯수
    total = 0
    
    if depth == n-1:
        return cost[x][1] # 여기 시작한 위치로 돌아가는 비용을 어떻게 구해야 할지..?
    
    for i in range(1, n+1):
        if cost[x][i] != 0 and visited[i] == -1:
            print(x, i)
            visited[i] = 0
            total += dfs(i, depth + 1)
            comp.append(total)
            visited[i] = -1
    
dfs(1, 0)
print(min(comp))