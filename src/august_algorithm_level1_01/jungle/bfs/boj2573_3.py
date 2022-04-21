# 73점 풀이
from collections import deque
import sys 
N, M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
# 방문 기록
visited = [[False for _ in range(M)] for _ in range(N)]

# 좌표 이동
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    selected = 0 # bfs에서 너비 우선 탐색을 진행한 빙하 수
    
    # 0으로 만들어줘야 하는 좌표 리스트
    rlist = []
    
    while queue :
        x, y = queue.popleft()
        selected += 1 # 빙하 수에 + 1

        # 0의 개수
        cnt = 0
        # 해당 점의 동서남북 보기
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a <= N-1 and 0 <= b <= M-1 : # 동서남북 좌표가 범위 안에 들 때만 고려
                if graph[a][b] == 0:
                    cnt += 1
                else:
                    if visited[a][b] == False:
                        queue.append((a, b))
                        visited[a][b] = True
                    
        # 동서남북의 0 개수가 노드값 이상일 때 -> 노드값을 0으로 만들어줘야 (리스트에 인덱스 추가)
        if cnt >= graph[x][y]:
            rlist.append((x,y))
        elif cnt < graph[x][y]:
            graph[x][y] = graph[x][y] - cnt
    
    # 마지막에 노드값을 0으로 만들어줌
    for x, y in rlist:
        graph[x][y] = 0
    
    print(graph)
    
    return selected # bfs로 너비 우선 탐색된 빙하의 수를 리턴해줌
    
        

year = 0           
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] != 0: # 사이클을 구하기 위해 not visited[i][j] | 이미 방문한 곳끼리 덩어리면 visited가 True이기 때문!
            
            # exist: 기존 그래프에 존재하는 0이 아닌 곳
            exist = 0
            for z in range(N):
                for y in range(M):
                    if graph[z][y] != 0:
                        exist += 1
            
            # selected: bfs를 돌면서 거쳐간 0이 아닌 곳 
            selected = bfs(i, j)
            
            # bfs 종료 시 year를 하나씩 올림
            year += 1
            visited = [[False for _ in range(M)] for _ in range(N)]

            # 기존 그래프에 존재하는 0이 아닌 곳을 bfs가 다 거쳐가지 않았을 때 (selected와 exist가 다름)
            if selected != exist:
               print(year-1) # 이전에 더해준 연도 - 1
               exit(0) # 프로그램 종료
               

print(0) # 끝까지 한 덩어리일 경우 print(0)