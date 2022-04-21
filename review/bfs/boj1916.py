import sys
input = sys.stdin.readline
import heapq # 가중치가 다 다르므로 다익스트라 활용

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)] # graph[출발도시] = [도착도시, 가중치]
visited = [[False] for _ in range(N+1)]
distance = [1e9] * (N+1) # 현재 노드까지 최단 거리를 갱신해줄 최단거리 테이블 초기화

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c]) # 노드, 가중치 a에서 b노드로 갈 때 비용이 c

start, end = map(int, input().split())

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (distance[start], start)) # 가중치, 노드
    
    while heap:
        dist, now = heapq.heappop(heap) # dist: 현재까지 힙에 있는 최단 경로
        if distance[now] < dist:
            continue
        for cur, curc in graph[now]: # 현재 노드의 인접노드를 돌며 확인 (인접노드, 비용)
            cost = dist + curc # 현재까지 힙에 있는 최단 경로와 인접노드까지 합이 cost
            if cost < distance[cur]: 
                distance[cur] = cost # 최단거리테이블 갱신
                heapq.heappush(heap, (distance[cur], cur))

dijkstra(start)

print(distance[end])

