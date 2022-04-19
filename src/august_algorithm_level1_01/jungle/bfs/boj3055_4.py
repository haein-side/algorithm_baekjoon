# 민성님 코드
# 물 먼저
import sys
from collections import deque

r,c=map(int,input().split())
maps=[list(p for p in sys.stdin.readline().strip()) for _ in range(r)]
visit=[[0]*c for _ in range(r)]

dr=[1,0,-1,0]
dc=[0,-1,0,1]

queue=deque()

#물,고슴도치 위치 queue에 담기 (고슴도치 - 물)
#굴의 위치는 target에 저장
for i in range(r):
    for j in range(c):
        if maps[i][j]=='*':             # 물 위치
            queue.append([i,j])
        elif maps[i][j]=='S':           # 고슴도치 위치 
            queue.appendleft([i,j])
        elif maps[i][j]=='D':           # 비버의 굴 ( 도착지 )
            target_r=i
            target_c=j

flag=False
#물과 고슴도치 위치에서 BFS탐색
while queue:
    # 굴에 도착하고 나면 while문 탈출
    # flag가 True가 되면 break
    if flag:
        break
    
    # 고슴도치 위치 -> 물의 위치
    pr, pc = queue.popleft()
    for i in range(4):                   
        nr,nc=pr+dr[i],pc+dc[i]
        if nr<0 or nr>=r or nc<0 or nc>=c:
            continue

        #물
        if maps[pr][pc]=='*':
            if maps[nr][nc]=='.' or maps[nr][nc]=='S':      # 물이 빈 공간과 고슴도치를 만나면
                maps[nr][nc]='*'                            # 물로 변경시킨다.
                queue.append([nr,nc])                       # 새로운 물의 좌표를 queue에 넣어줌

        #고슴도치
        elif maps[pr][pc] == 'S':                           # 고슴도치라면 
            if maps[nr][nc] == '.':                         # 빈 공간을 만나면 이동한다.
                maps[nr][nc] = 'S'                          # 이동하고 S라는 흔적을 남겨둠
                visit[nr][nc] = visit[pr][pc] + 1           # 해당 장소에 몇 번째(몇 분)에 도착했는지 기록한다.
                queue.append([nr,nc])                       # 그 장소가 최적의 시간이 아니라면 물에 잡아먹힐 것.
            #굴에 도착하면 탈출
            elif maps[nr][nc] == 'D':                       # 만약 굴에 도착했다면 (움직이려는 위치가 굴이면)
                flag=True
                visit[nr][nc]=visit[pr][pc]+1               # 전 방문 수 + 1 을 기록하고 while문을 빠져나온다.
                break

#굴에 도착하지 못하면 visit[굴]이 0이므로
if visit[target_r][target_c]==0:
    print('KAKTUS')
else: print(visit[target_r][target_c])