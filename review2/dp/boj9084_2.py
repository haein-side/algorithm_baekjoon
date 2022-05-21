import sys
input = sys.stdin.readline

t = int(input())

def sol():
    n = int(input()) # n: 동전의 갯수
    coins = list(map(int, input().split()))
    total = int(input())
    dp = [0 for _ in range(total + 1)]
    dp[0] = 1 # 동전 1개만 필요할 경우를 고려하기 위해

    for i in range(total+1):
        for coin in coins:
            if i > coin:
                dp[i] += dp[i-coin]
            elif i == coin:
                dp[i] += dp[i-coin] + 1 

    print(dp)

for _ in range(t):
    sol()