# 남의 풀이
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solution(n):
    lst = [sorted(list(map(int, input().split()))) for i in range(n)] # sorted로 받아서 오름차순으로 받음
    lst.sort(key=lambda x: x[1]) # 본인의 원소 중 큰 원소를 기준으로 오름차순 정렬
    d = int(input())
    
    print(lst)

solution(int(input()))