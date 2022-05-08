import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split()) # m: 세로 크기, n: 가로 크기
road = [[] for _ in range(m)]
for i in range(m):
    road[i] = list(map(int, input().split()))
visited = [[-1 for _ in range(n)] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y): # 현재 위치 x, y
    # 목적지에 도달했을 때
    if x == m-1 and y == n-1:
        return 1
    
    # 이미 방문했을 때는 dfs를 돌지 않고 해당 점에서 목적지까지 갈 수 있는 경로 수 리턴
    if visited[x][y] != -1:
        return visited[x][y]
    
    # 방문처리 겸 갈 수 있는 경로를 0으로 초기화
    visited[x][y] = 0
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if road[x][y] > road[nx][ny]: # 이동할 값이 더 작을 때
                visited[x][y] += dfs(nx, ny)
    
    return visited[x][y]
    


dfs(0, 0) # 시작지점
print(visited[0][0])
