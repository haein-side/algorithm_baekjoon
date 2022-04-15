# 서로소 집합을 활용한 사이클 판별
import sys

N, M = map(int, sys.stdin.readline().split())
parent = [0] * (N + 1) # 부모 테이블 초기화 | 왜 N + 1개?

# 부모 테이블상에서, 부모를 자기 자신으로 초기화 | 왜 1부터 N개?
for i in range(1, N+1):
    parent[i] = i

cycle = False

# 루트 원소 파악
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(x)
    return parent[x]

# 합집합
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print('하이',find_parent(a), find_parent(b))
    # 루트 노드가 같으면 사이클인 것
    if find_parent(a) == find_parent(b):
        cycle = True
        break
    else:
        union_parent(a, b)
print(cycle)
        
    
    