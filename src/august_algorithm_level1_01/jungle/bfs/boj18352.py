import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

N, M, K, X = map(int, input().split()) # N: 도시 개수, M: 도로 개수, K: 최단거리, X: 출발도시 번호
road = [[] for i in range(N+1)] # 각 도시 당 인접 도시를 넣어주기 위해 N+1
for i in range(M):
    a, b = map(int, input().split())
    road[a].append(b)
    # road[b].append(a) : a에서 b로 가는 단방향 그래프 이므로 거꾸로의 경우는 넣어주지 않음!
visited = [False] * (N+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)

def bfs(start):
    # 1에서 1로 가는 최단 거리는 0
    distance[start] = 0
    queue = deque()
    queue.append(start)
    # visited[start] = True : 방문 여부가 중요하지 않음. 
    # 방문했더라도 다른 인접노드를 통해 도달했을 때의 거리가 최단 거리인지 봐주면 됨
    
    while queue:
        q = queue.popleft()
        d = distance[q] # 현재 뽑은 것까지의 거리
        
        for adj_node in road[q]: # q도시와 연결되어 있는 인접 노드
            dist = d + 1 # 현재 뽑은 것까지 거리 + 1
            if distance[adj_node] > dist: # 최단거리 테이블에 있던 거리보다 지금 노드에서 이동했을 때 거리가 더 짧을 경우
                distance[adj_node] = dist # 최단거리 테이블 갱신
                queue.append(adj_node)

# 시작도시는 X! (실수한 부분)
bfs(X)

cnt = 0
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)
