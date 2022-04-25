from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
test = [] # 전체 맵 정보 
data = [] # 바이러스 정보 : 바이러스 숫자, x 좌표, y 좌표, 시간
for i in range(n):
    test.append(list(map(int, input().split())))
    for j in range(n):
        if test[i][j] != 0:
            # 바이러스 숫자, x좌표, y좌표, 시간 입력받음
            data.append((test[i][j], i, j, 0))
rs, rx, ry = map(int, input().split())
# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

data.sort()
q = deque(data) # 바이러스 정보가 들어있는 리스트를 deque에 넣어줘서 deque 자료형으로 만들어줌!

while q:
    virus, x, y, time = q.popleft()
    if time == rs:
        break
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        
        if mx <0 or my <0 or mx >=n or my >=n:
            continue
        
        if test[mx][my] == 0:
            test[mx][my] = virus
            q.append((virus, mx, my, time+1))
        
print(test[rx-1][ry-1])

