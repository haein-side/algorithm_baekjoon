# dp와 bfs를 결합
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split()) # m: 세로, n: 가로

road = [[] for _ in range(m)] # [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

for i in range(m):
    road[i] = list(map(int, input().split()))

v = [[-1 for _ in range(n)] for _ in range(m)] # 아직 방문한 적 없으면 -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y): # 현재위치 x, y
    # 목적지에 도달했으면
    if x == m-1 and y == n-1:
        return 1
    # 방문한 적 있으면
    if v[x][y] != -1:
        return v[x][y] # 좌표에 기록되어 있는 경로 반환
    # 처음 방문하면 아직 갈 수 있는 경로 수가 0이므로 0으로 초기화
    v[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= m-1 and 0 <= ny <= n-1:
            if road[nx][ny] < road[x][y]: # 현재 갈 곳의 높이가 더 낮으면
                v[x][y] += dfs(nx, ny) # 현재위치에 깊이 우선으로 탐색한 것들을 더해줌 (dfs)
    return v[x][y] # 현재위치에서 갈 수 있는 경로를 날 불러준 쪽으로 리턴해줌 (재귀)
                

dfs(0, 0)
print(v[0][0])
    
