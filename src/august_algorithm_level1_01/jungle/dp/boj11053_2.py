import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i): # 0부터 비교해주면 안 됨! 할 거면 1부터 비교해줘야!
        if num[i] > num[j]: # 현재 값 > 그 전 값
            # 현재값, 그 전 값으로 만들 수 있는 부분 수열의 길이 + 1
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))