import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n 물품 수 k 최대 무게
stuff = [[0,0]]
for _ in range(n):
    stuff.append(list(map(int, input().split()))) # stuff[0][0] = 무게, stuff[0][1] = 가치
dp = [[0 for _ in range(k+1)] for _ in range(n+1)] # dp 테이블 

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0] 
        value = stuff[i][1]
        
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j]) # i가 행으로 i-1 아직 내꺼 안 넣었을 때 j는 무게
# print(dp)
print(dp[n][k])