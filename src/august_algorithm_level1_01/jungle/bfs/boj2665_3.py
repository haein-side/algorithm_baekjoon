import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
bang = [[] for i in range(N+1)]

for i in range(1, N+1):
    bang[i] = [1] + list(map(int, input().strip())) # 이어져 있는 문자열을 int형으로 하나씩 넣기 (but 0번째 방은 임의의 수 1을 주기)

visited = [[False for _ in range(N+1)] for _ in range(N+1)]

# 좌표 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 다익스트라
def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y)) # 벽을 뿌실 때마다 발생하는 비용, x좌표, y좌표

    while q: # 큐가 비어있지 않으면
        # 거리, 방 위치 
        cost, r, c = heapq.heappop(q) # dist는 현재까지 0의 개수
        
        # 목적지에 도달했을 경우
        if r == N and c == N:
            return cost
        
        if visited[r][c]: # 이미 방문했었으면 더이상 따지지 않음
            continue
        
        visited[r][c] = True
        
        # 동서남북으로 이동하면서 0인 것의 개수 세기
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if dr <= 0 or dr > N or dc <= 0 or dc > N:
                continue
            
            if bang[dr][dc] == 1:
                heapq.heappush(q, (cost, dr, dc)) # 기존에 꺼낸 것의 cost를 그대로 넣어줌 (벽을 뿌시지 않았기 때문)
            else:
                heapq.heappush(q, (cost+1, dr, dc)) # 검은방이었으면 cost에 1을 더해서 넣어줌
                
            
        

answer = dijkstra(1,1)

print(answer)

