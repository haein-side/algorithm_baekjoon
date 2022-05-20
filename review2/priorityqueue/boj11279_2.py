import heapq
import sys
input = sys.stdin.readline

n = int(input())
numlist = []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(numlist) == 0:
            print(0)
        else:
            print(heapq.heappop(numlist)[1])
    else: # x가 자연수라면
        heapq.heappush(numlist, (-num, num))

