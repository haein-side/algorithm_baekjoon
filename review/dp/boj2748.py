import sys
input = sys.stdin.readline

n = int(input())
# dp = [0 for _ in range(n+1)] # 뒤에 숫자가 n으로 끝나려면 n+1개의 원소 필요

# dp[0] = 0
# if n == 1:
#     dp[1] = 1
#     print(1)
# elif n >= 2:
#     dp[1] = 1
#     i = 2
#     while i <= n:
#         dp[i] = dp[i-1] + dp[i-2]
#         i += 1
#     print(dp[n])

# 더 간단하게 푸는 법
pibo = [0, 1] # 이렇게 선언해놓고 for문으로 append해주는 것

# 수가 2이면 수 한 개만 들어가면 됨 -> for문의 횟수는 n-1
for i in range(n-1): # 0
    pibo.append(pibo[i] + pibo[i+1])
    
print(pibo[-1])