import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

N, M, K, X = map(int, input().split()) # 도시 개수, 도로 개수, 최단 거리, 출발 도시 번호

graph = [[] for _ in range(N+1)] # 각 노드에 있는 정보를 담는 리스트 만들기
# 최단 거리 테이블을 무한으로 모두 초기화
distance = [INF] * (N+1)

# 모든 간선 정보를 입력받기
for i in range(M):
    a, b = map(int, input())
    graph[a].append([b, 1]) # graph (노드, 거리) a번 노드에서 b번 노드로 가는 비용이 1

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start]) # q (거리, 노드)
    distance[start] = 0
    
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for cn, cd in graph[now]: # (노드, 거리)
            # 현재까지 누적된 최단 거리 + 인접노드까지의 거리
            cost = dist + cd
            if cost < distance[cn]:
                distance[cn] = cost
                heapq.heappush(q, [cost, cn])
                

dijkstra(X)

flag = False
for i in range(len(distance)):
    if distance[i] == K: # 최단 거리일 때
        print(i)
        flag = True
        
if not flag:
    print(-1)