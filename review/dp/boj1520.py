import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split()) # m이 행, n이 열

road = [[0 for _ in range(n+1)]]

for i in range(m):
    road.append([0] + list(map(int, input().split())))

c = [[-1 for _ in range(n+1)] for _ in range(m+1)]

# 좌표 이동
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def dfs(x, y):
    # print(x, y, c)
    if x == m and y == n: # 목적지에 도달했을 때 1 리턴하고 재귀 종료
        return 1
    if c[x][y] != -1: # 이미 한 번 방문했던 곳 -> 1을 리턴 (이미 방문했던 곳(ex.0 or 그 이상의 수)은 dfs를 못 돌도록 해준 것)
        return c[x][y] # 거기서 갈 수 있는 경로의 수를 리턴
    
    # 위에서 처음 방문한 곳이 아닌 곳들은 다 걸러짐
    # 처음 방문했을 때 0을 넣어줘서 방문표시 겸 아직 방문할 수 있는 경로 수가 0이라고 해줌
    c[x][y] = 0 
    
    for i in range(4):
        a, b = x + dx[i], y + dy[i] # a, b는 이동하는 좌표
        if 1 <= a <= m and 1 <= b <= n: # 이동한 좌표가 범위 안에 든다면
            if road[x][y] > road[a][b]: # 값이 적을 때
                
                c[x][y] += dfs(a, b) 
                # 재귀 호출하고 c[4][5]가 되어 종료됐을 때 
                # dfs(4, 5)를 호출한 depth인 c[4][4]로 돌아와서 리턴된 1을 넣어줌
                # c[4][4]에 1을 넣어준 이후에 for문이 4번 아직 다 돌지 않은 상태에서 dfs가 돌았다면
                # 나머지 for문을 다 돌고 난 이후에 37라인 실행 후, c[4][4]를 들고 불러준 depth으로 돌아감
                
    return c[x][y]
    # for문이 다 끝나고 c[4][4]를 line 29로 리턴해줌 
    # dfs(4, 4)를 호출한 depth인 c[4][3]으로 돌아와서 리턴된 1을 넣어줌
                
# for i in range(1, m+1): # 행
#     for j in range(1, n+1): # 열
#         if not visited[i][j]: # [i,j]인 곳을 방문한 적 없었다면
#             cnt += dfs(i, j)
print(dfs(1,1))
