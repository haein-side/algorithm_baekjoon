from collections import deque 

N, M = map(int, input().split())
miro = []
for _ in range(N):
    miro.append(list(map(int, input())))

# miro : [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    num = 1
    while queue:
        x, y = queue.popleft()
        num = miro[x][y]
        # for i in  miro[x][y]: # k의 인접노드 for문 : 인접노드를 돈다기 보단, 상하좌우 -> 1이면 queue에 append
        #     if visited[i] == False:
        #         queue.append(i)
        #         visited[i] = True
        for i in range(4):
            a, b = x + dx[i], y + dy[i] # a, b는 이동할 경우의 점의 좌표
            if 0 <= a <= N-1 and 0 <= b <= M-1:
                if miro[a][b] == 1:
                    queue.append((a,b))
                    miro[a][b] = num + 1
    return miro[N-1][M-1]
        
        
print(bfs(0,0))