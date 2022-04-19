import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)] # 도시의 개수+1 만큼 그래프가 필요
for i in range(1, M+1):
    a, city, d = map(int, input().split())
    graph[a].append((city, d)) # (도시, 거리)

# 출발 도시, 도착 도시
start, end = map(int, input().split())

# 최단 거리 테이블
distance = [INF] * (N+1) # 무한으로 초기화

def dijkstra(start):
    queue = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 초기화하여 큐에 삽입
    heapq.heappush(queue, (0, start)) # (거리, 도시)
    distance[start] = 0 # 방문했던 증표로 최단 거리 테이블 갱신 (visited 대신)
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        # 기존 최단거리 테이블 < 우선순위 큐 : 이미 최단거리로 처리된 적 있는 노드이면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 인접한 노드 확인
        for city, d in graph[now]: # 도시, 거리
            cost = dist + d # cost : 기존 꺼낸 노드까지의 최단 거리 + 인접 도시까지의 거리
            
            if cost < distance[city]:
                distance[city] = cost
                heapq.heappush(queue, (distance[city], city)) # 큐에 거리, 도시 순으로 삽입
                # 최단 거리를 최단 거리 테이블에 갱신해준 도시의 인접노드에서 또 최단 거리를 찾아 나섬
            

dijkstra(start) # "출발 도시"에서 "각 노드들"에 대한 "최단 거리"를 최단 거리 테이블에 갱신해줌

print(distance[end]) # 갱신된 최단 거리 테이블의 값을 출력해줌!