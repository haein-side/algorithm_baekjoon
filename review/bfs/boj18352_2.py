import sys
import heapq

N, M, K, X = map(int, sys.stdin.readline().split())
# N 도시 개수, M 도로 개수, K 거리 정보, X 출발 도시 번호
road = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    road[a].append((b, 1)) # 노드, 비용
start = X
distance = [1e9 for _ in range(N+1)] # 최단경로 테이블

def dijkstra(start):
    heap = []
    distance[start] = 0
    heap.append((0, start)) # 비용, 노드
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
        
        for city, curc in road[now]: # 노드, 비용
            cost = dist + curc
            if cost < distance[city]:
                distance[city] = cost
                heapq.heappush(heap, (cost, city))
                
dijkstra(start)                
           
flag = True      
for i in range(1, len(distance)):
    if distance[i] == K:
        print(i)
        flag = False

if flag:
    print(-1)
    
