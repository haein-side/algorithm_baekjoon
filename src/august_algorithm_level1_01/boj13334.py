import sys
import heapq
n = int(sys.stdin.readline())
rail = [sorted(list(map(int, sys.stdin.readline().split()))) for i in range(n)]
rail.sort(key = lambda x:x[1])
d = int(sys.stdin.readline())
heap = []
result = -1

for s, e in rail:
    lim = e - d
    
    if lim <= s: # 일단 자기 자신을 넣어줌 (시작점이 lim 이상이기만 하면!)
        heapq.heappush(heap, s)
    
    while heap and heap[0] < lim: # heap에 값이 있을 때 끝까지 돌면서 계속 lim보다 작은 s가 있으면 pop을 시켜줌
        heapq.heappop(heap)
    
    result = max(result, len(heap))

print(result)
    