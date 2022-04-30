import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split()) # m 행, n 열
w = []

for _ in range(m):
    w.append(list(map(int, input().split())))

# 방문 여부    
v = [[-1 for _ in range(n)] for _ in range(m)]

# 경로 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == m-1 and y == n-1: # 목적지에 도달했을 때
        return 1
    
    if v[x][y] != -1: # 방문한 적이 있었을 때
        return v[x][y] # 해당 점에서 목적지까지 갈 수 있는 경로 반환
    
    v[x][y] = 0
    
    for i in range(4):
        a, b = x + dx[i], y + dy[i] 
        
        if 0 <= a <= m-1 and 0 <= b <= n-1: # 범위 안에 있을 때
            if w[x][y] > w[a][b]: # 이동한 점의 높이가 더 낮을 때
                v[x][y] += dfs(a, b) 
                
    return v[x][y] # for문이 다 끝난 다음 그 전 위치로 경로 수 리턴

print(dfs(0, 0))