import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)] # dp[i]는 i번째 수까지 최대 합을 넣어줌 
# 음수가 뒤에 있을 수 있으므로 맨 뒤 숫자가 항상 최댓값인 건 아님! -> 그래서 max를 또 해줘야 함!

# 점화식
# dp[i] = max(num[i], dp[i-1] + num[i])
# 나만 넣어서 새로 시작하는 합 vs. 나 + 나 이전 것들까지 최대합

for i in range(1, n+1):
    dp[i] = max(num[i], dp[i-1] + num[i])
    
print(max(dp[1:])) # dp[0]을 0으로 초기화해둬서 음수만 입력 받을 경우 첫번째 원소인 0을 제외하고 max를 따져줘야 함