# 민성님 코드
import heapq
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
distance = [[int(10e9)]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

min_path = 2500

def bfs():              # 사실 다익스트라
    heap = []
    heapq.heappush(heap, (0,0,0))
    while heap:
        cost, r, c = heapq.heappop(heap)

        if distance[r][c] <= cost:
            continue
        else:
            distance[r][c] = cost 
            # 한개씩 pop을 하면서 distance 테이블의 값을 갱신해줌

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if nx >=0 and nx < N and ny >=0 and ny < N:
                if not matrix[nx][ny]:
                    heapq.heappush(heap, (cost+1, nx, ny))
                else:
                    heapq.heappush(heap, (cost, nx, ny))

bfs()

print(distance[N-1][N-1])