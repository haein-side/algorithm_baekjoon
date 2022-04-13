import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    
    if num != 0:
        heapq.heappush(heap, (-num, num))

    else:
        if len(heap) > 0:   
            max = heapq.heappop(heap)[1]
            print(max)
        else:
            print(0)
    