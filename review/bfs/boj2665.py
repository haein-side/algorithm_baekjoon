# 미로 만들기
# BFS, heap
import sys
input = sys.stdin.readline
import heapq

n = int(input())
bang = [[] for _ in range(n)]
# 흰방 1, 검은방 0
for i in range(n):
    bang[i] = list(map(int, list(input().strip())))

visited = [[False for _ in range(n)] for _ in range(n)]

heap = []
heap.append([0,0,0]) # cnt: 검은방갯수, x, y
visited[0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = False
while heap:
    cnt, x, y = heapq.heappop(heap)
    
    if x == n-1 and y == n-1:
        print(cnt)
        flag = True
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if bang[nx][ny] == 0 and not visited[nx][ny]: # 검은방
            heapq.heappush(heap, (cnt+1, nx, ny))
            visited[nx][ny] = True
        elif bang[nx][ny] == 1 and not visited[nx][ny]: # 흰방
            heapq.heappush(heap, (cnt, nx, ny))
            visited[nx][ny] = True

if not flag:
    print(-1)