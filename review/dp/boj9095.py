import sys
input = sys.stdin.readline

t = int(input())

dp = [0 for _ in range(11)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

# dp[4] = dp[3] + dp[2] + dp[1]
# 3을 만들 수 있는 경우의 수에 +1 한 것
# 2를 만들 수 있는 경우의 수에 +2 한 것
# 1을 만들 수 있는 경우의 수에 +3 한 것
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])
    