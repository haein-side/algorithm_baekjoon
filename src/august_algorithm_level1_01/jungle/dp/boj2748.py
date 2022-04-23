# import sys
# num = int(sys.stdin.readline())
# pibo = [0, 1]
# result = 0

# for i in range(num-1):
#     pibo.append(pibo[i] + pibo[i+1])

# print(pibo[-1])

### 다른 풀이 (메모이제이션: 이전에 계산된 결과를 일시적으로 저장해놓는 것)
n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1): # n+1으로 해야 n까지 i가 돌 수 있다.
    dp[i] = dp[i-1] + dp[i-2]

print(dp[i])