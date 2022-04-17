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
    
    # 0으로 만들어줘야 하는 좌표 리스트
    rlist = []
    notzero = 0
    while queue :
        x, y = queue.popleft()
        notzero += 1
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
    
    print('0이 아닌것의 개수',notzero)
    return notzero
    # return N*M - notzero
    
        
# 총 사이클 도는 횟수 
result = 0            
c = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] != 0: # 사이클을 구하기 위해 not visited[i][j] | 이미 방문한 곳끼리 덩어리면 visited가 True이기 때문!
            zero = bfs(i, j)
            print('들어온 0이 아닌 것의 개수', zero)
            visited = [[False for _ in range(M)] for _ in range(N)]
            print('그래프',graph)
            # print(graph.count(0))
            # if graph.count(0) != zero:
            #        print(graph.count(0), zero)
            # result += 1

