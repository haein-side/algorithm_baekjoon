import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    miro[i] = [0] + list(map(int, list(input().strip())))
visited = [[False for _ in range(M+1)] for _ in range(N+1)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(cnt, x, y):
    heap = []
    heapq.heappush(heap, (1, (x, y))) # 비용, 노드 좌표
    visited[x][y] = True
    while heap:
        cnt, (x, y) = heapq.heappop(heap)
        if x == N and y == M:
            print(cnt)
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 1 or ny < 1 or nx > N or ny > M:
                continue
            if miro[nx][ny] == 1 and not visited[nx][ny]:
                heapq.heappush(heap, (cnt+1, (nx, ny)))
                visited[nx][ny] = True

bfs(1, 1, 1)