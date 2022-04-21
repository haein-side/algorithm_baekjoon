import sys
input = sys.stdin.readline
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)] # N+1개의 부품 만들어줌 (연결 정보)
# 진입 차수 테이블 초기화
indegree = [0] * (N+1)
mid = [] # 중간재
# 방향 그래프의 모든 간선 정보 입력받기
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a를 만드는 데 b부품이 c개 필요
    indegree[a] += 1 # a에 대한 진입차수가 1 더해짐
    
    if a != N:
        mid.append(a)

mid = list(set(mid)) # 중간재 중복 제거
basic = []
for i in range(1, N):
    if i != mid:
        basic.append(i)

# 위상정렬 함수
def topology_sort():
    needs = [[0 for _ in range(N+1)] for _ in range(N+1)]
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        cur = q.popleft() # 큐에서 원소 꺼내기
        
        # 연결된 인접 노드를 파악
        for next_node, next_cost in graph[cur]:
            if cur in basic:
                needs[next_node][cur] += next_cost
            else:
                for i in range(1, N+1):
                    needs[next_node][i] = needs[cur][i] * next_cost
                    
        
        
        
