import sys
input = sys.stdin.readline

t = int(input())

def sol():
    n = int(input()) # n: 동전의 갯수
    coins = list(map(int, input().split()))
    k = int(input())

    dp = [0 for _ in range(k + 1)]
    dp[0] = 1 # 동전 1개만 필요할 경우를 고려하기 위해

    for coin in coins: # 동전의 종류별로 만들 수 있는 합 (j)
        for j in range(coin, k+1): #coin은 coin부터 k까지 합을 만들 수 있음
            dp[j] += dp[j-coin]
           

    print(dp[k])

for _ in range(t):
    sol()