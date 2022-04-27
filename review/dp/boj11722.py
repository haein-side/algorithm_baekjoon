# 가장 긴 감소하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        if num[i] < num[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))