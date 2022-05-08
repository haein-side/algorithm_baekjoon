import sys
input = sys.stdin.readline

n = int(input())
cost = [[] for _ in range(n)]
for i in range(n):
    cost[i] = list(map(int, input().split()))

visited = [-1 for _ in range(n)] # 방문 아직 안됐음 -1로 
minCost = 9999999

def dfs(city, price, depth):
    global minCost
    # 시간초과를 막을 수 있음!
    # 현재 비용이 minCost보다 클 경우 바로 return해줌
    if price > minCost:
        return
    
    if depth == n and city == 0: # 순환이므로 다시 시작했던 곳으로 돌아왔을 때
        minCost = min(minCost, price)
        return

    for i in range(n):
        # city -> i 방문 시
        if cost[city][i] != 0 and visited[i] == -1:
            visited[i] = 0
            dfs(i, price + cost[city][i], depth+1)
            visited[i] = -1
    
dfs(0,0,0)
print(minCost)