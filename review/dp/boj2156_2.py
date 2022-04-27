import sys
input = sys.stdin.readline

n = int(input())
w = [0]
for _ in range(n):
    w.append(int(input()))
dp = [0 for _ in range(n+1)]

# 마지막 꺼가 최대 양이라는 보장 X -> dp리스트에서 max값을 골라내면 최대 값임

if n == 1:
    print(w[1])
else:
    dp[1] = w[1]
    dp[2] = w[1] + w[2]
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], w[i] + w[i-1] + dp[i-3], w[i] + dp[i-2])
    
    print(max(dp))