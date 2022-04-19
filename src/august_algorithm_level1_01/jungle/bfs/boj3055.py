# 혼자 풀어본 풀이
# 물을 1분 단위로 끊어서 도출해내는 것까지 성공했으나
# 그 물을 가지고 어떻게 1분 단위로 끊어서 탐색해낼지는 찾아내지 못함

import sys
from collections import deque
import heapq
input = sys.stdin.readline

R, C = map(int, input().split()) # R: 행, C: 열
queue = deque()

forest = [[] for _ in range(R)]
go = []
bi = []

for i in range(R):
    forest[i] = list(input().strip())
    for j in range(C):
        if forest[i][j] == '*': # 물이 차 있는 곳
            queue.append((i, j)) # 물이 차 있는 곳 좌표를 큐에 넣어줌
        if forest[i][j] == 'S': # 고슴도치
            go.append(i)
            go.append(j)
        if forest[i][j] == 'D': # 비버
            bi.append(i)
            bi.append(j)

print('큐', '고슴도치', '비버', queue, go, bi)     

# forest [['D', '.', '.', '.', '*', '.'], ['.', 'X', '.', 'X', '.', '.'], ['.', '.', '.', '.', 'S', '.']]   

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문여부
visited = [[False for _ in range(C)] for _ in range(R)]
visited[go[0]][go[1]] = True

# 시작하는 시간, 고슴도치 위치 넣어줌
heap = [(0, go[0], go[1])]

# . 비어있는 곳, * 물 차 있는 곳, X 돌 있는 곳, D 비버, S 고슴도치

# 물이 차도록 해주는 함수
def water():
    # 몇 번 append 됐는지 세 주는 변수
    cnt = 0
    while(queue): # queue : 물이 현재 차 있는 곳의 좌표 (이후에 한 번 돌면서 물이 되어야 하는 부분을 append해주고 for문 돌림)
        x, y = queue.popleft() # 처음에 물이 차 있던 곳 좌표를 받아줌
        
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < R and 0 <= b < C and forest[a][b] == '.': # 범위 안에 들고 비어있는 곳이라면
                queue.append((a, b))
                forest[a][b] = '*'
                cnt += 1
                
        # 그 전에 append 해준 횟수만큼 for문을 돌면 1분동안 만들어지는 물 웅덩이
        # 물 웅덩이가 만들어지면 물 웅덩이를 빼고 S(고슴도치)가 움직여야 함!
        
        if cnt == len(queue): # 1분 지날 때 물 웅덩이가 만들어진 상태
            print('한번 끊기', forest)
            cnt = 0  # cnt 한번 초기화
            # (time, cx, cy) = heapq.heappop(heap)
            
            # # 비버굴에 도착했을 경우
            # if cx == go[0] and cy == go[1]:
            #     print(time)
            #     exit(0)
            
            # for i in range(4):
            #     nx = cx + dx[i]
            #     ny = cy + dy[i]
                
            #     if 0 <= nx < R and 0 <= ny < C:
            #         # 비어있는 곳일 경우
            #         if forest[nx][ny] == '.':
            #             heapq.heappush(heap, (time+1, nx, ny))
            
            # print(heap)
            
            
            
        
water()



# bfs(bi[0], bi[1])
            


