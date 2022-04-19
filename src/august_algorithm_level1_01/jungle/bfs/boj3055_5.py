import sys
from collections import deque

r,c=map(int,input().split())
maps=[list(p for p in sys.stdin.readline().strip()) for _ in range(r)]
visit=[[0]*c for _ in range(r)]

dr=[1,0,-1,0]
dc=[0,-1,0,1]

queue=deque()

# 고슴도치, 물 위치 queue에 담기
# 고슴도치 먼저 움직이고 물을 이동시키고 (번갈아서 이동시켜주기 위해)
# 굴의 위치는 target에 저장
for i in range(r):
    for j in range(c):
        if maps[i][j] == '*':
            queue.append([i, j])
        elif maps[i][j] == 'S':
            queue.appendleft([i, j])
        elif maps[i][j] == 'D': # 비버의 굴 (도착지)
            target_r = i
            target_c = j

flag = False
# 물과 고슴도치 위치에서 BFS 탐색
while queue:
    # 만약 굴에 도착해서 flag가 True가 되면 break
    if flag:
        break
    
    # 고슴도치 움직이고 물이 움직이고의 구조!
    pr, pc = queue.popleft() # 원래 위치
    for i in range(4):
        nr, nc = pr + dr[i], pc + dc[i] # 이동할 위치
        if nr < 0 or nr >= r or nc < 0 or nc >= c: # 범위 안에 들지 못해서 continue
            continue
        
        # 물
        if maps[pr][pc] == '*': # 큐에서 pop한 원래 위치가 물이면..
            if maps[nr][nc] == '.' or maps[nr][nc] == 'S': # 물이 빈 공간과 고슴도치를 만나면
                maps[nr][nc] = '*' # 물로 변경시킴
                queue.append([nr, nc]) # 새로운 물의 좌표를 queue에 넣어줌
                
        # 고슴도치
        elif maps[pr][pc] == 'S': # 원래 위치가 고슴도치라면..
            if maps[nr][nc] == '.': # 빈 공간을 만나면
                maps[nr][nc] = 'S' # 이동하고 S라는 흔적을 남겨둠 why? : 그래야 다음에 현 위치를 왔을 때 좌표값 S로 고슴도치인지 판별
                visit[nr][nc] = visit[pr][pc] + 1
                queue.append([nr, nc])
            elif maps[nr][nc] == 'D': # 굴을 만나면
                flag = True
                visit[nr][nc] = visit[pr][pc] + 1
                break

if visit[target_r][target_c] == 0:
    print('KAKTUS') 
else:
    print(visit[target_r][target_c])               