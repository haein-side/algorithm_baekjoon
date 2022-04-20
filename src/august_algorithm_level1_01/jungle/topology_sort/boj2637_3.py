# 기존 풀이 수정
import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
node = [[] for _ in range(N+1)] # N+1개의 부품들을 만들어둠 (연결정보)
basic = [] # 기본 부품
mid = [] # 중간 부품
final = N # 완제품

# 진입차수 테이블
indegree = [0 for _ in range(N+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(M):
    x, y, k = map(int, sys.stdin.readline().split())
    node[x].append([y, k]) # x번 부품을 만드는 데 y번 부품이 k개 필요함 [y번 부품, k 가중치]
    indegree[y] += 1
    
    if x != final :
        mid.append(x) # 중간재 번호 적어두기

# 기본 부품들 입력해주기    
for i in range(1, N+1):
    if i not in mid and i != final:
        basic.append(i)

# 중간 부품들 중복 제거
mid = list(set(mid))

# 위상 정렬 함수로 필요한 기본 부품 수 구하기
def topology_sort():
    # 기본 부품 수 테이블
    needs = [[0 for _ in range(N+1)] for _ in range(N+1)]
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 원소의 인접 노드와 가중치         
        for next_node, next_cost in node[now]:
            
            if now in basic: # 현재 노드가 기본 부품이면 가중치만 더해줌 
                needs[next_node][now] += next_cost
            else: # 현재 노드가 중간제이면 기존에 가지고 있는 것에 부품 * 가중치 더해줌
                for i in range(1, N+1):
                    needs[next_node][i] += needs[now][i] * next_cost
                            
            indegree[next_node] -= 1 # 연결된 노드의 진입차수 1 빼기
            if indegree[next_node] == 0:
                q.append(next_node)
        print(needs)
        
    return needs
    
    

print(topology_sort())