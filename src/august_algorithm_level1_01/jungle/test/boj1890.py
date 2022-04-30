import sys
input = sys.stdin.readline

n = int(input())
game = []

for i in range(n):
    game.append(list(map(int, input().split())))
    
# -1로 방문하지 않았을 때
cur = [[-1 for _ in range(n)] for _ in range(n)]

def dfs(x, y): # 현재 위치 x, y
    if x == n-1 and y == n-1: # x, y가 목적지에 도달했을 때
        return 1
    
    if cur[x][y] != -1: # 방문한 적 있으면 그 곳에서 목적지까지 도달했던 경로 수 리턴 받음 (더이상 탐색 안 함)
        return cur[x][y]
    
    cur[x][y] = 0
    
    a, b = x + game[x][y], y # 아래로 이동
    if 0 <= a <= n-1 and 0 <= b <= n-1:
        cur[x][y] += dfs(a, b)
        
    a, b = x, y + game[x][y] # 오른쪽으로 이동
    if 0 <= a <= n-1 and 0 <= b <= n-1:
        cur[x][y] += dfs(a, b)

    return cur[x][y]

print(dfs(0, 0)) 