import heapq
import sys
input = sys.stdin.readline

n = int(input())
numlist = []
numrlist = []

for _ in range(n):
    num = int(input())
    heapq.heappush(numlist, (num, num)) # 제거 시 작은 수부터 정렬됨
    heapq.heappush(numrlist, (-num, num)) # 제거 시 큰 수부터 정렬됨

for i in range(n//2):
    heapq.heappop(numlist)
    heapq.heappop(numrlist)

print(numlist)