# visited 처리를 해줘야 파고 들어서 인접노드로 들어갔을 때 똑같은 수가 있는 경우
# 이미 visited True 상태이기 때문에 count를 하나 더 올리지 않을 수가 있다.

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
light_g = [[] for _ in range(N+1)]
heavy_g = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    light_g[a].append(b)
    heavy_g[b].append(a)

count = 0  
def light(i):
    global count
    visited[i] = True
    for j in light_g[i]: # 현재 i보다 가벼운 것들
        if not visited[j]: 
            count += 1 # 인접노드를 돌 때마다 count를 1 올려줌
            visited[j] = True
            light(j)
    
    return count

def heavy(i):
    global count
    visited[i] = True
    for j in heavy_g[i]:
        if not visited[j]: 
            count += 1
            visited[j] = True
            heavy(j)
    
    return count

result = 0
for i in range(1, N+1):
    tmp = light(i)
    visited = [False] * (N+1)
    if tmp >= (N+1)//2:
        result += 1
        
    count = 0
            
for i in range(1, N+1):
    tmp = heavy(i)
    visited = [False] * (N+1)
    if tmp >= (N+1)//2:
        result += 1
    
    count = 0
            
print(result)