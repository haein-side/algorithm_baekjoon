import sys

# 노드의 개수, 간선의 개수
V, E = map(int, sys.stdin.readline().split())

# 부모 테이블 초기화
parent = [0] * (V + 1) # 왜 V + 1?

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, V + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for i in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    # 비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# find 함수 : 특정 원소의 루트 원소 찾기 (속한 집합 찾기)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 함수 : 두 원소의 루트 원소를 하나로 합치기 (노드를 연결)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a # 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가
    else:
        parent[a] = b
    
# 간선을 하나씩 확인하며 최소 신장 트리에 넣어줄 수 있는지 확인
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b): # 둘이 다른 루트 원소 가질 때 == 사이클이 만들어지지 않을 때
        union_parent(parent, a, b) # 간선 하나에 연결된 점은 두 개 (하나의 집합으로 만들어줌)
        result += cost # 간선 하나 당 비용은 하나

print(result)
        
        