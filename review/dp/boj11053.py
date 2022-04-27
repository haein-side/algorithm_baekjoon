import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
dp = [1 for _ in range(n+1)] # 아무리 못해도 자기 자신으로 부분 수열을 만들 수 있으므로 1로 초기화

for i in range(1, n+1):
    for j in range(1, i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) # 가장 마지막에 있는 원소의 값이 max가 아닐 수도 있음! -> 그래서 max(dp)를 해줘야 최장 길이를 구할 수 있음