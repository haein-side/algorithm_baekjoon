import sys

V, E = map(int, sys.stdin.readline().split())

parent = [0] * (V+1)

edges = []
result = 0

# 부모 테이블 상에서 자기 자신으로 부모를 초기화
for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
    
edges.sort() # 간선 비용 순으로 정렬

# find 함수 : 특정 원소의 루트 원소 찾기 (속한 집합 찾기)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
# 간선을 하나씩 확인하며 최소 신장 트리에 넣어줄 수 있는지 확인
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b): # 둘이 다른 루트 원소 가질 때 == 사이클이 만들어지지 않을 때
        union_parent(parent, a, b) # 간선 하나에 연결된 점은 두 개 (하나의 집합으로 만들어줌)
        result += cost # 간선 하나 당 비용은 하나

print(result)
        