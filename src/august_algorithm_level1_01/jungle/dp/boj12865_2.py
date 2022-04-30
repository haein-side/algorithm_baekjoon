import sys
input = sys.stdin.readline
# dp[i][j] : i번째 물건까지 고려했을 때 무게가 j가 되는 것의 최대 가치합

n, k = map(int, input().split())
stuff = [[0,0]] # 0번째는 더미

for _ in range(n):
    stuff.append(list(map(int, input().split())))

dp = [[0 for col in range(k+1)] for row in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = stuff[i][0], stuff[i][1]
        
        if weight <= j: # 현재무게 <= 총 무게라면
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])
        else: # 현재무게 > 총 무게라면 나 안 넣고 동일 무게의 최대 가치 합 가져옴
            dp[i][j] = dp[i-1][j]

print(dp[n][k])