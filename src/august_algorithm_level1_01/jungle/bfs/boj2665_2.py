# 다익스트라 사용한 풀이
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
bang = [[] for i in range(N+1)]

for i in range(1, N+1):
    bang[i] = [1] + list(map(int, input().strip())) # 이어져 있는 문자열을 int형으로 하나씩 넣기 (but 0번째 방은 임의의 수 1을 주기)

# 좌표 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [[INF for _ in range(N+1)] for _ in range(N+1)]

# 다익스트라
def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, (x, y))) # 거리, 방 위치, 현재 0 의 개수 0
    distance[x][y] = 0 # 현재 0 의 개수 0
    
    # 0의 개수
    zero_cnt = 0
    
    while q: # 큐가 비어있지 않으면
        # 거리, 방 위치 
        dist, now = heapq.heappop(q) # dist는 현재까지 0의 개수
        a, b = now
        print(dist, a, b)

        if distance[a][b] < dist:
            continue
        
        # 동서남북으로 이동하면서 0인 것의 개수 세기
        for i in range(4):
            c, d = x + dx[i], y + dy[i]
            if 1 <= c <= N and 1 <= d <= N: # 동서남북 좌표가 범위 안에 들 때
                if bang[c][d] == 0: # 검은 방
                    zero_cnt += 1
                    
                cost = dist + zero_cnt
                # print('가격', cost)
                print(dist, cost, distance[c][d])
                
                if cost <= distance[c][d]:
                    distance[c][d] = cost
                    heapq.heappush(q, (cost, (c, d)))
                    
                # if visited[a][b] == False:
                #     visited[a][b] = True
                #     queue.append((a, b))
        
        

dijkstra(1,1)

print(distance)

