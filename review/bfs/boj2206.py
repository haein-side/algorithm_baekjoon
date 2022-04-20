import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

heap = [(0, 0, 0, 0)] # 현재까지 이동횟수, x좌표, y좌표, 1을 만났을 때 횟수

while heap:
    (cnt, zcnt, cx, cy) = heapq.heappop(heap)
    
    if cx == N-1 and cy == M-1:
        print(cnt)
        break
    
    map[cx][cy] = cnt
    onecnt = 0
    totalcnt = 0
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            totalcnt += 1
            # 이동할 수 있는 곳인 경우
            if map[nx][ny] == 0 and not visited[nx][ny]:
                heapq.heappush(heap, (cnt+1, zcnt, nx, ny))
            
            elif map[nx][ny] == 1 and not visited[nx][ny]:
                onecnt += 1
    
    if totalcnt == onecnt:
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            heapq.heappush(heap, (cnt+1, zcnt+1, nx, ny))