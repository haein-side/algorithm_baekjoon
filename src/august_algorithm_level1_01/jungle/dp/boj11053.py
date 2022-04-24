import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [1 for _ in range(n)] # n개의 숫자에 대해 적어도 길이가 1인 부분수열은 만들 수 있으므로 1로 초기화

# num에 있는 숫자들이 자기 자신보다 인덱스가 작은 숫자들을 돌며 
# 대소비교를 하고, 각각의 숫자들로 부분수열을 만들 수 있는지 따지며
# 가장 큰 부분수열 길이를 dp 테이블에 넣어준다.

for i in range(n):
    for j in range(i): # i보다 작은 원소들을 돎
        if num[i] > num[j]: # 현재 숫자 > 이전 숫자이면 부분수열 만들 수 있음
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))