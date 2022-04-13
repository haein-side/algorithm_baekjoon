import sys
import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)
    
answer = 0
while len(heap) >= 2:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    answer += (a + b) # 가장 작은 거 두 개를 계속 더해주면 쌓이게 됨
    heapq.heappush(heap, a+b)

print(answer)