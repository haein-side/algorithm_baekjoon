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
    selected = 0
    # 0으로 만들어줘야 하는 좌표 리스트
    rlist = []
    while queue :
        x, y = queue.popleft()
        selected += 1
        # print(graph[x][y], click)

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
    
    return selected
    
        
# 총 사이클 도는 횟수 
result = 0
# 빙산
artic = []

# 현재 빙산의 개수 파악            
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] != 0: # 사이클을 구하기 위해 not visited[i][j] | 이미 방문한 곳끼리 덩어리면 visited가 True이기 때문!
            artic.append((i, j))
            
while True:
    for i in range(N):
        for j in range(M):
        # 덩어리가 2개 이상인 경우
            if len(artic) != bfs(i, j): # 현재 그래프의 빙산의 개수와 bfs()에서 거쳐간 빙산의 개수가 다를 때
                print(result)
                exit(0)
    
    result += 1
    
print(result)


            
            # # print('cl값', cl)      
            # number = bfs(i, j)
            # # print(number)
            # visited = [[False for _ in range(M)] for _ in range(N)]
            
            # # print(number, cl)
            # if number != cl:
            #    print(c)
            #    exit(0)
            # c += 1

    # else: 
    #     print(0)
    #     break
