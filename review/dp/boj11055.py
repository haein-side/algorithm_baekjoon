# 가장 큰 증가 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
dp = []

# 아무리 못해도 자기 자신으로 부분 수열 만들 수 있어서 스스로의 값을 dp에 초기화해준다.
for i in num:
    dp.append(i)

for i in range(1, n+1):
    for j in range(1, i):
        if num[i] > num[j]:
            # dp[i]는 i번째 원소까지 고려했을 때 만들 수 있는 증가 부분수열의 최대합
            dp[i] = max(dp[i], dp[j] + num[i])

print(max(dp))