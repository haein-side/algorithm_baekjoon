import sys
input = sys.stdin.readline

n = int(input())
cost = [[0 for _ in range(n)] for _ in range(n)]
# [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]

for i in range(n):
    cost[i] = list(map(int, input().split()))
visited = [-1 for _ in range(n)] # -1 방문 아직 안 함, 0 방문 함
comp = []

def dfs(x, depth, cur): # x: 현재위치, depth: 방문한 도시 갯수
    
    if depth == n and x == 0: # 시작한 위치로 돌아왔을 때 (순회라 어디서 시작하든 동일함)
        return cur # 여기 시작한 위치로 돌아가는 비용을 어떻게 구해야 할지..?
    
    for i in range(n):
        if cost[x][i] != 0 and visited[i] == -1:
            # print(x, i)
            visited[i] = 0
            tmp = dfs(i, depth + 1, cur + cost[x][i])
            if tmp != None:
                comp.append(tmp)
            visited[i] = -1
    
dfs(0, 0, 0)
print(min(comp))