import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
# visited = [False for _ in range(K+1)]

dx = [-1, 1, 2]

def bfs(cnt, x):
    heap = []
    heapq.heappush(heap, (cnt, x)) # 시간, 수빈이 위치
    # visited[x] = True
    
    while heap:
        cnt, x = heapq.heappop(heap)
        if x == K:
            print(cnt)
            break
        for i in range(3):
            if i == 0 or i == 1:
                nx = x + dx[i]
            else:
                nx = x * dx[i]
            # if not visited[x]:
            # print('현재 수빈이 위치',nx)
            heapq.heappush(heap, (cnt+1, nx))
            # visited[nx] = True
    
bfs(0, N) # 시간, 수빈이 위치
