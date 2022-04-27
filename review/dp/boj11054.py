import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
rnum = num[::-1]
dp = [1 for _ in range(n)]
rdp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[i] > num[j]: # 현재원소가 더 크면.. 증가 부분 수열 만들 수 있음
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(n):
    for j in range(i):
        if rnum[i] > rnum[j]:
            rdp[i] = max(rdp[i], rdp[j] + 1)

rdp = rdp[::-1]
sumdp = []
for i in range(n):
    sumdp.append(dp[i] + rdp[i])

print(max(sumdp) - 1)