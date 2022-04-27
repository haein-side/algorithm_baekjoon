# 가장 긴 증가하는 부분 수열 3
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [num[0]] # dp 배열에 증가 원소들 담는 것

for i in range(1, len(num)):
    if dp[-1] < num[i]:
        dp.append(num[i])
    else:
        # 이진탐색
        # bisect_left(dp, num[i])
        # 정렬된 dp에 num[i]를 삽입할 위치를 리턴해줌
        # num[i]가 dp에 이미 있으면 기존 항목의 앞(왼쪽)의 위치 반환
        index = bisect_left(dp, num[i])
        dp[index] = num[i]

print(len(dp))