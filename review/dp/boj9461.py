import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    
    if n == 1:
        print(1)
    else: # n이 2이상이면
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-3]

        print(dp[n])