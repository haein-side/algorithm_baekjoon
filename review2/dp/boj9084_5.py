import sys
input = sys.stdin.readline

t = int(input())

def sol():
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m+1)] # 합이 m원이 되는 경우의 수
    dp[0] = 1 # 동전이 하나만 필요할 경우 고려

    for coin in coins:
        for hap in range(coin, m+1):
            dp[hap] += dp[hap - coin]
    
    print(dp[m])

for _ in range(t):
    sol()