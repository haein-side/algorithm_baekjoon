import sys
input = sys.stdin.readline

t = int(input())

def sol():
    n = int(input())
    coins = list(map(int, input().split()))
    k = int(input())

    dp = [0] * (k+1)
    dp[0] = 1 # 동전이 1개만 필요할 때 고려

    for coin in coins:
        for j in range(coin, k+1):
            dp[j] += dp[j-coin]

    print(dp[k])

for _ in range(t):
    sol()