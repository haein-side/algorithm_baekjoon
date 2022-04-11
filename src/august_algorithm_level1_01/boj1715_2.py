import sys
import heapq
N = int(sys.stdin.readline())
card = []

for i in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(card, num)
    
if N == 1:
    print(0)
elif N == 2:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    print(a+b)
else:
    cnt = 2
    arr = []
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    arr.append(a + b)
    
    while cnt <= N-1:
        arr.append(arr[-1] + heapq.heappop(card))
        cnt += 1
    
    print(sum(arr))