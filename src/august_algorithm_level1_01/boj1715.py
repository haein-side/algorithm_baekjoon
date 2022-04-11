import sys
import heapq
N = int(sys.stdin.readline())
card = []

for i in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(card, num)
    
if N == 1:
    print(0) # 생각하지 못했던 부분 (카드가 한 묶음일 땐 비교할 필요가 없으므로 0)
elif N == 2:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    print(a+b)
else:
    answer = 0
    while len(card) > 1:
        print(card)
        # 최소인 값을 최대한 더 많이 더하는 게 중요
        # 입력값이 4 // 10 15 20 23 인 경우
        # [10, 15, 20, 23]
        # [20, 23, 25] <= 여기서 원래대로 생각했던 로직이라면 25(마지막 값) + 20을 더했어야 하지만, 최소값을 구해야 하므로 20 + 23 카드를 먼저 합치는 게 최소이다.
        # [25, 43]
        a = heapq.heappop(card)
        b = heapq.heappop(card)
        answer += a + b
        heapq.heappush(card, a+b)
    
    print(answer)
    