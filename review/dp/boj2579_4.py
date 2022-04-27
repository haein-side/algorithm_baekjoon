import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]

for i in range(n):
    stairs.append(int(input()))

dp = [0 for _ in range(n+1)]

if n == 1:
    print(stairs[1])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    
    for i in range(3, n+1): # 3부터 n까지
        dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])
    
    print(dp[-1])