import sys
import heapq

n = int(sys.stdin.readline())
p = []
for i in range(n):
    p.append(sorted(list(map(int, sys.stdin.readline().split()))))
p = sorted(p, key = lambda x : x[1])
d = int(sys.stdin.readline())
heap = []
result = -1

for s, e in p:
    lim = e - d
    
    if lim <= s:
        heapq.heappush(heap, s)
    
    while heap and heap[0] < lim:
        heapq.heappop(heap)

    result = max(result, len(heap))

print(result)