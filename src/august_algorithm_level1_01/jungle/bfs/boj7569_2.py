# 민성님 풀이
import sys
from collections import deque
M,N,H = map(int,input().split()) # mn크기, h상자수

queue = deque([])
 
graph = [] 
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(M):
            if tmp[j][k]==1:
                queue.append([i,j,k]) # 큐에 1인 것들을 넣어주면 먼저 처리됨!
    graph.append(tmp)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<H and 0<=b<N and 0<=c<M and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1                   # 원래 1이었던 애들 주변을 2로만든다. 2었던 애들이 0인 애들을 익게하면 3으로만들고...
            
day = 0
for i in graph:                 # level
    for j in i:                 # row
        for k in j:             # column
            if k==0:
                print(-1)       # while문이 끝나도 0인애가 있다면 -1 출력
                exit(0)
        day = max(day,max(j))   # 가장 나중에 익은 과일의 수를 불러옴
print(day-1)