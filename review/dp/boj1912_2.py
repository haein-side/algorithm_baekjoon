import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = max(dp[i-1] + num[i], num[i])

print(max(dp[1:]))