import sys
import collections

N = int(sys.stdin.readline()) # N * N
K = int(sys.stdin.readline()) # 사과의 개수
board = [[0 for i in range(N)] for j in range(N)] # N * N의 정사각 행렬

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = -1 # x행 y열에 사과가 있으면 -1을 둠

L = int(sys.stdin.readline()) # 뱀의 방향 변환 횟수
change = [[0,0] for i in range(L)] # 변환 횟수 L행 이차원 배열

for i in range(L):
    x, y = sys.stdin.readline().split()
    change[i] = [int(x), y]

# board [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# change [[3, 'D'], [15, 'L'], [17, 'D']]

cnt = 0 # 총 시간
dir = 1 # 현재 방향
x, y = 0, 0 # 현재 위치
body = collections.deque([[0,0]]) # 현재 몸 좌표
while 0 <= x <= N-1 and 0 <= y <= N-1:
    
    # 움직이기 전에 사과가 있는지 확인하고 몸 좌표 갱신해주기
    if board[x][y] == -1:
        body.appendleft([x, y])
        board[x][y] = 0
    else:
        body.pop()
        body.appendleft([x, y])
    
    # 기존 방향과 change 리스트 안에 걸린 시간이 있는지에 따라 다음으로 이동
    for i in range(L):
        if cnt == change[i][0]:
            if change[i][1] == "D":
                if dir == 1:
                    x += 1
                    dir = 2
                elif dir == 2:
                    y -= 1
                    dir = 3
                elif dir == 3:
                    x -= 1
                    dir = 4
                else:
                    y += 1
                    dir = 1
            else: # 왼쪽으로 change
                if dir == 1:
                    x -= 1
                    dir = 4
                elif dir == 2:
                    y += 1
                    dir = 1
                elif dir == 3:
                    x += 1
                    dir = 2
                else:
                    y -= 1
                    dir = 3
            cnt += 1
            break
    else: # for문 안에서 break가 발생하지 않았을 경우 else문을 적어줌 (change가 적용되지 않는 경우)
        if dir == 1:
            y += 1
        elif dir == 2:
            x += 1
        elif dir == 3:
            y -= 1
        else:
            x -= 1
        cnt += 1
    
    if [x,y] in body:
        break
    
    

print(cnt)