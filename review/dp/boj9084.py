import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    k = int(input())
    
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    
    for coin in coins:
        for j in range(coin, k+1): # coin은 coin부터 k까지 합을 만들 수 있음 
            dp[j] += dp[j-coin]    # 윗부분에 "range"로 coin부터 k까지 1씩 커지게 해야 함! (저번에도 실수함..)
            
    print(dp[k])