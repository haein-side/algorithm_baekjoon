import sys
input = sys.stdin.readline

t = int(input())

def sol():
    n = int(input()) # n: 동전의 갯수
    coins = list(map(int, input().split()))
    total = int(input())
    dp = [1 for _ in range(total + 1)]
    cnt = 0
    for i in range(total+1):
        for coin in coins:
            if total[i] > coin:
                dp[total] = dp[total[i]-coin] + 1
            else:
                total[i] = dp[total[i]-coin]


for _ in range(t):
    sol()
