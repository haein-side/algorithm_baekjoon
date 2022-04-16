# 이 풀이는 따로 부모 테이블 같은 걸 두지 않고 풀었다.
# 자식노드가 2개 이상일 때 성립하지 않는 코드..
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
node = [[] for i in range(N+1)] # 0번째 노드는 비워두기
one = []
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a) # 2차원 행렬 이외에 리스트로 받는 방안 or 딕셔너리로 받는 방안도 구현해보기

visited = [False] * (N+1)
dic = {} # dic[자식 노드] = 부모 노드 (부모 노드는 자식 노드별로 한 개!)

for i in range(N):
    dic[i] = 0

def dfs(i):
    visited[i] = True
    
    for j in node[i]: # i 노드와 인접한 노드 j            
        if not visited[j]:
            dic[j] = i # dic[자식 노드] = 부모 노드 | {0: 0, 1: 0, 2: 4, 3: 6, 4: 1, 5: 3, 6: 1, 7: 4}
            dfs(j)
    
for i in range(1, N+1): # 1부터 N까지 노드
    if not visited[i]:
        dfs(i)

# print(dic)
for i in dic.values():
    if i > 0:
        print(i)
