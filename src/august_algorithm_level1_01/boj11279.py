import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    a = int(sys.stdin.readline())
    
    if a != 0:
        heapq.heappush(heap, (-a, a)) # (우선순위, 값) : 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성됨
    
    else: # a가 0이라면 가장 큰 값 출력, 그 값을 배열에서 제거
        if len(heap) == 0: # 배열이 비어 있는 경우
            print(0)
        else:
            print(heapq.heappop(heap)[1]) # index 1 : 우선순위가 높은(작은) 것부터 먼저 실행됨

