import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
road = [[] for _ in range(m)]

for i in range(m):
    road[i] = list(map(int, input().split()))
    
# -1은 한 번도 방문한 적 없을 때
# 0은 처음 한 번 방문했을 때 방문 체크 겸 아직 목적지까지 도달한 경로 없는 경우
# 그 이상의 숫자들도 해당 도착점에서 목적지까지 도달한 경로의 수
checked = [[-1 for _ in range(n)] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if checked[x][y] != -1: # 방문한 적 있을 때 dfs 또 못 돌도록 visited 처리해준 것
        return checked[x][y] # 해당 경로에서 목적지까지 도달할 수 있는 경로 반환
    
    checked[x][y] = 0 # 방문 표시 및 0으로 초기화
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx <= m-1 and 0 <= ny <= n-1:
            if road[nx][ny] < road[x][y]:
                checked[x][y] += dfs(nx, ny)
    
    return checked[x][y] # checked[x][y]에 쌓인 것을 그 전 depth로 갖다줌
        
dfs(0,0)
print(checked[0][0])
