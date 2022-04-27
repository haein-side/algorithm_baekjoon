# 가장 긴 증가하는 부분 수열 3
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [num[0]] # dp 배열에 증가 원소들 담는 것

def find(target):
    start = 0
    end = len(dp) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if dp[mid] < target:
            mid = start + 1
        elif dp[mid] > target:
            mid = end - 1
        else:
            return mid
    return start
        
for i in range(1, len(num)):
    if dp[-1] < num[i]:
        dp.append(num[i])
    else:
        index = find(num[i])
        dp[index] = num[i]

print(len(dp))