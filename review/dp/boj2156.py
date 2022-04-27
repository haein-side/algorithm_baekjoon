import sys
input = sys.stdin.readline

n = int(input())
w = [0]
for _ in range(n):
    w.append(int(input()))
dp = [0 for _ in range(n+1)]

if n == 1:
    print(w[1])
else:
    dp[1] = w[1]
    dp[2] = w[1] + w[2]
    
    # dp[n]은 n번째 와인까지 따졌을 때 마실 수 있는 최대 와인의 양
    # max() 경우의 수
    # n번째 와인 먹고 + 그 전 꺼 안 먹은 경우: dp[n] = w[n] + dp[n-2]
    # n번째 와인 먹고 + 그 전 꺼 먹은 경우 : dp[n] = w[n] + w[n-1] + dp[n-3]
    # 이렇게만 하면 => 계단 오르기처럼 n번째 와인을 무조건 먹어줘야 ! (즉 마지막 계단을 꼭 밟고 끝나게 됨)
    
    # 그러나 여기선, n번째 와인을 안 먹는 경우를 고려해줘야 : dp[n] = dp[n-1]
    # 점화식
    # dp[n] = max(w[n] + dp[n-2], w[n] + w[n-1] + dp[n-3], dp[n-1])
    
    for i in range(3, n+1):
        dp[i] = max(w[i] + dp[i-2], w[i] + w[i-1] + dp[i-3], dp[i-1])

    print(dp[-1])