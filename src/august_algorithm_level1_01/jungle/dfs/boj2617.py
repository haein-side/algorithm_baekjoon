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

print(light_g) 

count = 0  
def light(i, cnt):
    global count
    
    for j in light_g[i]: # 현재 i보다 가벼운 것들
        count += light(j, cnt + 1)
    
    return count

# def heavy(i, cnt):
#     visited[i] = True
    
#     for j in heavy_g[i]: # 현재 i보다 가벼운 것들
#         if visited[j] == False:
#             visited[j] = True
#             light(j, cnt + 1)
    
#     return cnt
    
result = 0

for i in range(1, N+1):
    tmp = light(i, 0)
    if tmp >= (N+1)//2:
        result += 1
    # print(i, count)
    count = 0
print(result)
            
# visited = [False] * (N+1)
            
# for i in range(1, N+1):
#     if visited[i] == False:
#         tmp = heavy(i, 0)
#         if tmp >= (N+1)//2:
#             result += 1
            
# print(result)