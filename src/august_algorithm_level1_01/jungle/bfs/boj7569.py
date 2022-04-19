from collections import deque
import sys
input = sys.stdin.readline

# 의문 1. visited 처리를 해줘야 하나? - no no

M, N, H = map(int, input().split())
box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

# 좌표 이동
dx = [-1, +1, 0, 0, 0, 0]
dy = [0, 0, -1, +1, 0 ,0]
dz = [0, 0, 0, 0, -1, +1]

ok = 0 # 익은 토마토 개수 1 
notyet = 0 # 익지 않은 토마토 개수 0
nothing = 0 # 아무것도 없는 토마토 개수 -1

onelist = []
for i in range(H):
    for j in range(N):
            num = list(map(int, input().split()))
            ok += num.count(1)
            notyet += num.count(0)
            nothing += num.count(-1)
            box[i][j] = num

total = M * N * H

# 저장될 때부터 모든 토마토가 익어있는 상태인 경우 0 출력
if total == (ok + nothing):
    print(0)
    exit(0)

# 1인 것의 좌표를 넣는 리스트
onelist = []
for a in range(H):
    for b in range(N):
        for c in range(M):
            if box[a][b][c] == 1:
                onelist.append((a, b, c))
                
# BFS 함수
def bfs(onelist):
    queue = deque()
    
    # 1로 만들어줘야 하는 좌표 리스트
    clist = []
    
    for d, e, f in onelist: # 1인 것들의 좌표
        queue.append((d, e, f))
        
        while queue:
            z, y, x = queue.popleft()
            exist = box[z][y][x]
          
            for k in range(6):
                p, l, m =  z + dz[k], y + dy[k], x + dx[k] # 이동했을 때 좌표 (층  H, 열 N, 행 M)
                if 0 <= p <= H-1 and 0 <= l <= N-1 and 0 <= m <= M-1: # 범위 안에 들 때
                    
                    if box[p][l][m] == 0:
                        clist.append((p, l, m))
                       

    for q, w, e in clist:
        box[q][w][e] = exist + 1
    
    if len(clist) == 0:
        print(-1)
        exit(0)
    
    for g in range(H):
        for h in range(N):
            if box[g][h].count(0) >= 1:
                bfs(clist)
    

# 1인 좌표의 리스트를 넣고 너비 우선 탐색
bfs(onelist)

maxNum = -1

for a in range(H):
    for b in range(N):
        for c in range(M):
            maxNum = max(maxNum, box[a][b][c])

print(maxNum-1)