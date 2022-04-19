import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
bang = [[] for i in range(N+1)]

for i in range(1, N+1):
    bang[i] = [1] + list(map(int, input().strip())) # 이어져 있는 문자열을 int형으로 하나씩 넣기
    
# 좌표 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 기록을 안 남겨도 되는 것 같음..? -> 아님!! 
visited = [[False for _ in range(N+1)] for _ in range(N+1)]

# BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    # 검은방 -> 흰방 개수 리스트
    clist = []
    
    while queue:
        x, y = queue.popleft()
        print("(",x,y,")")
        # 검은방 -> 흰방 개수
        cnt = 0
        
        # 동서남북으로 이동하면서 0인 것의 개수 세기
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 1 <= a <= N and 1 <= b <= N: # 동서남북 좌표가 범위 안에 들 때
                if bang[a][b] == 0: # 검은 방
                    cnt += 1
                    print('0 나옴 (', a, b, ')', cnt)
                if visited[a][b] == False:
                    visited[a][b] = True
                    queue.append((a, b))
        print("-------------")     
    clist.append(cnt)
    # print('개수',clist)
        
    return clist

result = bfs(1,1)
print(min(result))


