import sys

input = sys.stdin.readline

n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

dp = [0 for _ in range(n+1)]

if n == 1:
    print(stairs[0])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2] # max를 구하는 것이므로 두 개 합해줌
    
    for i in range(3, n+1): # 인덱스 2인 계단부터 인덱스 n인 계단까지 더툼
        # 한칸 건너뛴 계단 n-2
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])
        
print(dp[-1])